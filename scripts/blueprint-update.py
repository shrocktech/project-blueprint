#!/usr/bin/env python3
"""Prepare a bounded Blueprint proposal; never execute incoming project/release code."""
import argparse
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import tempfile
import time

SHA = re.compile(r"[0-9a-f]{40}\Z")
REPO = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z")
TAG = re.compile(r"v?(\d+)\.(\d+)\.(\d+)\Z")


def run(*args, cwd=None, check=True):
    return subprocess.run(args, cwd=cwd, check=check, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, timeout=120)


def git(root, *args):
    return run("git", "-C", str(root), *args).stdout


def api(path, payload=None, method=None):
    args = ["gh", "api", path]
    if method:
        args += ["--method", method]
    if payload is not None:
        args += ["--input", "-"]
    for attempt in range(3):
        result = subprocess.run(args, input=json.dumps(payload).encode() if payload is not None else None,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60)
        if result.returncode == 0:
            return json.loads(result.stdout) if result.stdout else None
        # GET retries only: mutation timeouts are reconciled by the next run.
        if payload is not None or attempt == 2:
            raise RuntimeError("GitHub request failed; see repository access and service health")
        time.sleep(2 ** attempt)


def pages(path):
    result = []
    for page in range(1, 101):
        items = api(f"{path}{'&' if '?' in path else '?'}per_page=100&page={page}")
        if not isinstance(items, list):
            raise ValueError("Invalid list response")
        result.extend(items)
        if len(items) < 100:
            return result
    raise ValueError("Pagination limit reached; review manually")


def config(root, source):
    p = root / ".github/blueprint-update.json"
    if p.is_symlink() or not p.is_file():
        raise ValueError("Configure .github/blueprint-update.json before activation")
    cfg = json.loads(p.read_text())
    if not REPO.fullmatch(source) or cfg.get("source") != source:
        raise ValueError("Source mismatch")
    if not SHA.fullmatch(cfg.get("adopted", {}).get("commit", "")):
        raise ValueError("Record a verified adoption commit")
    if not TAG.fullmatch(cfg["adopted"].get("tag", "")):
        raise ValueError("Record a stable adoption tag")
    branch = cfg.get("integrationBranch", "")
    if not isinstance(branch, str) or branch.startswith("-") or not branch:
        raise ValueError("Record the integration branch")
    run("git", "check-ref-format", "--branch", branch)
    return cfg


def tree(root, commit):
    files = {}
    for entry in git(root, "ls-tree", "-rz", commit).split(b"\0"):
        if not entry:
            continue
        meta, raw = entry.split(b"\t", 1)
        mode, kind, oid = meta.decode().split()
        name = raw.decode("utf-8")
        files[name] = (mode, kind, oid)
    return files


def mapped(name):
    # Fixed scope, not an allowlist supplied by an incoming release.
    if re.fullmatch(r"template/standards/[a-z][a-z0-9-]*\.md", name):
        return name.removeprefix("template/")
    if name.startswith("skills/"):
        p = PurePosixPath(name)
        if len(p.parts) >= 3 and re.fullmatch(r"[a-z][a-z0-9-]*", p.parts[1]):
            if all(re.fullmatch(r"[A-Za-z0-9_.-]+", s) and s not in (".", "..") for s in p.parts):
                return ".agents/" + name
    return None


def proposal(source, base, latest, target):
    old, new = tree(source, base), tree(source, latest)
    writes, review = {}, []
    for name in sorted(set(old) | set(new)):
        if old.get(name) == new.get(name):
            continue
        destination = mapped(name)
        if destination is None:
            review.append(name + " (agent-managed)")
            continue
        path = target / destination
        if any(p.is_symlink() for p in [path, *path.parents] if p != target):
            review.append(destination + " (symlink)")
            continue
        entries = [entry for entry in (old.get(name), new.get(name)) if entry]
        if any(mode != "100644" or kind != "blob" for mode, kind, _ in entries):
            review.append(destination + " (non-regular source)")
            continue
        if destination.startswith(".agents/skills/"):
            skill = destination.split("/")[2]
            if not (target / ".agents/skills" / skill / "SKILL.md").is_file():
                review.append(destination + " (skill selection/installation)")
                continue
        before = git(source, "cat-file", "blob", old[name][2]) if name in old else None
        after = git(source, "cat-file", "blob", new[name][2]) if name in new else None
        if any(data and (len(data) > 1024 * 1024 or b"\0" in data) for data in (before, after)):
            review.append(destination + " (binary/oversized)")
            continue
        if path.exists() and not path.is_file():
            review.append(destination + " (occupied destination)")
            continue
        current = path.read_bytes() if path.is_file() else None
        if current == after:
            continue
        if current != before:
            review.append(destination + " (local content)")
            continue
        writes[destination] = after
    return writes, review


def apply(target, writes):
    for name, data in writes.items():
        p = target / name
        if data is None:
            p.unlink()
        else:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--target", type=Path, required=True)
    args = parser.parse_args()
    target = args.target.resolve()
    cfg = config(target, args.source)
    repo = os.environ["GITHUB_REPOSITORY"]
    if not REPO.fullmatch(repo):
        raise ValueError("Invalid target repository")
    if git(target, "status", "--porcelain").strip():
        raise ValueError("Use a clean disposable checkout")
    # Configuration on the default branch determines the integration target.
    git(target, "fetch", "origin", cfg["integrationBranch"])
    git(target, "checkout", "--detach", "FETCH_HEAD")
    if config(target, args.source) != cfg:
        raise ValueError("Default/integration adoption records disagree")
    releases = pages(f"repos/{args.source}/releases")
    stable = [r for r in releases if not r["draft"] and not r["prerelease"] and TAG.fullmatch(r["tag_name"])]
    if not stable:
        print("No stable release; adoption unchanged")
        return
    release = max(stable, key=lambda r: r["published_at"])
    tag = release["tag_name"]
    with tempfile.TemporaryDirectory(prefix="blueprint-source-") as tmp:
        source = Path(tmp)
        run("git", "-c", "credential.helper=!gh auth git-credential", "clone", "--bare", f"https://github.com/{args.source}.git", tmp)
        base = cfg["adopted"]["commit"]
        recorded = git(source, "rev-parse", f"refs/tags/{cfg['adopted']['tag']}^{{commit}}").decode().strip()
        latest = git(source, "rev-parse", f"refs/tags/{tag}^{{commit}}").decode().strip()
        if recorded != base:
            raise ValueError("Adopted tag integrity mismatch")
        if latest == base:
            print("Stable guidance current; inspect existing maintenance issues for pending work")
            return
        if run("git", "-C", tmp, "merge-base", "--is-ancestor", base, latest, check=False).returncode:
            raise ValueError("Divergence/rollback: owner review required")
        new_version = tuple(map(int, TAG.fullmatch(tag).groups()))
        old_version = tuple(map(int, TAG.fullmatch(cfg["adopted"]["tag"]).groups()))
        if new_version <= old_version:
            raise ValueError("Non-increasing release: review integrity")
        marker = f"<!-- blueprint-update:{latest} -->"
        issues = pages(f"repos/{repo}/issues?state=all")
        matches = [i for i in issues if "pull_request" not in i and marker in (i.get("body") or "") and i["user"]["login"] == "github-actions[bot]"]
        if len(matches) > 1:
            raise ValueError("Duplicate maintenance issues require reconciliation")
        writes, review = proposal(source, base, latest, target)
        major = new_version[0] != old_version[0]
        if major:
            review.insert(0, "Major release: agent migration assessment; ask owner only for actual authority/product decisions.")
        body = (f"{marker}\nBlueprint source: `{args.source}`\n\nVerified adoption: `{cfg['adopted']['tag']}` / `{base}`\n"
                f"Candidate: `{tag}` / `{latest}`\n\nReview the release and diff under the project's existing instructions. "
                "No adoption, merge, deployment or new tool activation is certified by this proposal. "
                "Complete relevant application changes, verify skills and checks, then record adoption and close the issue.\n\n"
                f"Release: https://github.com/{args.source}/releases/tag/{tag}\n\n"
                "Agent reconciliation:\n" + "\n".join("- `" + p + "`" for p in review[:150]) +
                ("\n- Full diff required; additional paths omitted." if len(review) > 150 else "") +
                "\n\nPR candidates contain only unchanged-source standards and already-installed skills. Local decisions remain authoritative.")
        if matches:
            issue = matches[0]
            if issue["state"] == "closed":
                raise ValueError("Closed maintenance issue with stale adoption record; reconcile before retry")
        else:
            issue = api(f"repos/{repo}/issues", {"title": f"Review Blueprint {tag}", "body": body, "labels": ["TO DO"]})
        print("Maintenance issue:", issue["html_url"])
        if major or not writes:
            return
        branch = f"blueprint/{tag}"
        apply(target, writes)
        git(target, "add", "--", *writes)
        git(target, "diff", "--cached", "--check")
        candidate_tree = git(target, "write-tree").strip()
        remote = git(target, "ls-remote", "--heads", "origin", f"refs/heads/{branch}")
        if remote.strip():
            git(target, "fetch", "origin", f"refs/heads/{branch}")
            if git(target, "rev-parse", "FETCH_HEAD^{tree}").strip() != candidate_tree:
                raise ValueError("Existing proposal differs or base advanced; agent owns reconciliation, no force push")
        else:
            git(target, "-c", "user.name=Blueprint updater", "-c", "user.email=blueprint@users.noreply.github.com",
                "-c", "core.hooksPath=/dev/null", "-c", "commit.gpgsign=false", "commit", "-m", f"Prepare Blueprint {tag} (#{issue['number']})")
            git(target, "push", "origin", f"HEAD:refs/heads/{branch}")
        prs = pages(f"repos/{repo}/pulls?state=all&head={repo.split('/')[0]}:{branch}")
        if prs:
            if len(prs) != 1 or prs[0]["state"] != "open" or prs[0]["base"]["ref"] != cfg["integrationBranch"]:
                raise ValueError("Existing PR requires agent reconciliation")
            print("Existing PR:", prs[0]["html_url"])
        else:
            pr = api(f"repos/{repo}/pulls", {"title": f"Prepare Blueprint {tag}", "base": cfg["integrationBranch"],
                      "head": branch, "body": f"Tracks {issue['html_url']}\n\n{body}"})
            print("Prepared PR:", pr["html_url"])


if __name__ == "__main__":
    main()
