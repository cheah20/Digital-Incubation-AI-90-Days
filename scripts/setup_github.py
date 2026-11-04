#!/usr/bin/env python3
"""Turn the 90-lesson plan into GitHub issues, milestones and labels, and turn on GitHub Pages.

usage (from the repo root):
    python3 scripts/setup_github.py --start 2026-11-01            # required
    python3 scripts/setup_github.py --start 2026-11-01 --project  # also make a Project board

Safe to run again: existing issues, labels and milestones are skipped. Needs gh, logged in with gh auth login.
"""
import argparse, json, subprocess, sys, time, datetime, pathlib

PHASES = {
    "Phase 1": "Python and Engineering Foundations",
    "Phase 2": "Math, Data and Classical ML",
    "Phase 3": "Deep Learning and GPU",
    "Phase 4": "LLMs, RAG and Agents",
    "Phase 5": "AI Backend and Databases",
    "Phase 6": "Engineering and Deployment",
    "Phase 7": "Integration and Final Assessment",
}

def gh(*args, check=True, inp=None):
    r = subprocess.run(["gh", *args], capture_output=True, text=True, input=inp)
    if check and r.returncode != 0:
        sys.exit(f"gh {' '.join(args[:3])} failed:\n{r.stderr.strip()}")
    return r

ap = argparse.ArgumentParser(); ap.add_argument("--start", required=True, help="Day 1 date, for example 2026-11-01")
ap.add_argument("--project", action="store_true", help="also create a GitHub Project board"); a = ap.parse_args()
start = datetime.date.fromisoformat(a.start)
repo = gh("repo", "view", "--json", "nameWithOwner", "-q", ".nameWithOwner").stdout.strip()
owner = repo.split("/")[0]
data = json.loads(pathlib.Path(__file__).with_name("issues.json").read_text(encoding="utf-8"))
print(f"Repo: {repo}  Day 1 = {start}")

print("1. Labels")
for name, color, desc in [("daily","1E6E58","Daily check-in"),("review","B7790F","Review day"),("checkpoint","B4412F","Phase checkpoint")] + \
        [(f"phase-{i}","5E6C67",f"Phase {i}") for i in range(1,8)]:
    gh("label", "create", name, "--color", color, "--description", desc, "--force")

print("2. Milestones (one per phase, with a due date)")
have = {m["title"]: m["number"] for m in json.loads(gh("api", f"repos/{repo}/milestones?state=all&per_page=100").stdout)}
for first, last, code, _ in data["phases"]:
    if code in have: continue
    due = (start + datetime.timedelta(days=last-1)).isoformat() + "T23:59:59Z"
    gh("api", "-X", "POST", f"repos/{repo}/milestones", "-f", f"title={code}", "-f", f"description={PHASES.get(code, code)}, Day {first}–{last}", "-f", f"due_on={due}")

print("3. Issues (90 of them, takes 2–3 minutes)")
existing = set()
for page in range(1, 4):
    out = json.loads(gh("api", f"repos/{repo}/issues?state=all&labels=daily&per_page=100&page={page}").stdout)
    existing |= {i["title"][:7] for i in out}
    if len(out) < 100: break
for it in data["issues"]:
    key = f"Day {it['n']:03d}"
    if key in existing: continue
    date = (start + datetime.timedelta(days=it["n"]-1)).isoformat()
    body = it["body"].replace("OWNER", owner).replace("REPO", repo.split("/")[1]) + f"\n\n> 📅 Planned date: {date}"
    r = gh("issue", "create", "--title", it["title"], "--body-file", "-", "--milestone", it["milestone"],
           *sum((["--label", l] for l in it["labels"]), []), inp=body)
    print("  ", key, r.stdout.strip()); time.sleep(1.2)

print("4. GitHub Pages (main branch, /docs)")
r = gh("api", "-X", "POST", f"repos/{repo}/pages", "-f", "source[branch]=main", "-f", "source[path]=/docs", check=False)
print("   turned on" if r.returncode == 0 else "   already on, or turn it on by hand: Settings → Pages → Branch: main /docs")
print(f"   Logbook: https://{owner}.github.io/{repo.split('/')[1]}/  (the first deploy takes 1–2 minutes)")

if a.project:
    print("5. Project board (needs the project scope: gh auth refresh -s project)")
    r = gh("project", "create", "--owner", owner, "--title", "AI Engineer Path", "--format", "json", check=False)
    if r.returncode != 0: print("   could not create it:", r.stderr.strip()); sys.exit(0)
    num = str(json.loads(r.stdout)["number"])
    allurls = [i["html_url"] for p in range(1,3) for i in json.loads(gh("api", f"repos/{repo}/issues?state=all&labels=daily&per_page=100&page={p}").stdout)]
    for u in sorted(allurls, key=lambda u: int(u.rsplit("/",1)[1])):
        gh("project", "item-add", num, "--owner", owner, "--url", u, check=False); time.sleep(0.5)
    print(f"   done: https://github.com/users/{owner}/projects/{num}")
print("All done ✅")
