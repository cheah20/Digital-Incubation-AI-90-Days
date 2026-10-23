#!/usr/bin/env python3
"""一次性把 90 天计划变成 GitHub Issues + Milestones + Labels，并开启 GitHub Pages。
用法（在仓库根目录）：
    python3 scripts/setup_github.py --start 2026-11-01            # 必做
    python3 scripts/setup_github.py --start 2026-11-01 --project  # 另外建一个 Project 看板（可选）
可以重复运行：已存在的 Issue / Label / Milestone 会跳过。需要先安装并登录 gh（gh auth login）。"""
import argparse, json, subprocess, sys, time, datetime, pathlib

def gh(*args, check=True, inp=None):
    r = subprocess.run(["gh", *args], capture_output=True, text=True, input=inp)
    if check and r.returncode != 0:
        sys.exit(f"gh {' '.join(args[:3])} 失败：\n{r.stderr.strip()}")
    return r

ap = argparse.ArgumentParser(); ap.add_argument("--start", required=True, help="Day 1 日期，例如 2026-11-01")
ap.add_argument("--project", action="store_true", help="另外创建 GitHub Project 看板"); a = ap.parse_args()
start = datetime.date.fromisoformat(a.start)
repo = gh("repo", "view", "--json", "nameWithOwner", "-q", ".nameWithOwner").stdout.strip()
owner = repo.split("/")[0]
data = json.loads(pathlib.Path(__file__).with_name("issues.json").read_text(encoding="utf-8"))
print(f"仓库：{repo}  Day 1 = {start}")

print("① Labels")
for name, color, desc in [("daily","1E6E58","每日打卡"),("review","B7790F","复盘日"),("checkpoint","B4412F","阶段验收")] + \
        [(f"phase-{i}","5E6C67",f"Phase {i}") for i in range(1,8)]:
    gh("label", "create", name, "--color", color, "--description", desc, "--force")

print("② Milestones（每个阶段一个，带截止日期）")
have = {m["title"]: m["number"] for m in json.loads(gh("api", f"repos/{repo}/milestones?state=all&per_page=100").stdout)}
for first, last, code, zh in data["phases"]:
    if code in have: continue
    due = (start + datetime.timedelta(days=last-1)).isoformat() + "T23:59:59Z"
    gh("api", "-X", "POST", f"repos/{repo}/milestones", "-f", f"title={code}", "-f", f"description={zh} · Day {first}–{last}", "-f", f"due_on={due}")

print("③ Issues（90 个，约 2–3 分钟）")
existing = set()
for page in range(1, 4):
    out = json.loads(gh("api", f"repos/{repo}/issues?state=all&labels=daily&per_page=100&page={page}").stdout)
    existing |= {i["title"][:7] for i in out}
    if len(out) < 100: break
urls = []
for it in data["issues"]:
    key = f"Day {it['n']:03d}"
    if key in existing: continue
    date = (start + datetime.timedelta(days=it["n"]-1)).isoformat()
    body = it["body"].replace("OWNER", owner).replace("REPO", repo.split("/")[1]) + f"\n\n> 📅 计划日期：{date}"
    r = gh("issue", "create", "--title", it["title"], "--body-file", "-", "--milestone", it["milestone"],
           *sum((["--label", l] for l in it["labels"]), []), inp=body)
    urls.append(r.stdout.strip()); print("  ", key, r.stdout.strip()); time.sleep(1.2)

print("④ GitHub Pages（main 分支 /docs）")
r = gh("api", "-X", "POST", f"repos/{repo}/pages", "-f", "source[branch]=main", "-f", "source[path]=/docs", check=False)
print("   已开启" if r.returncode == 0 else "   已开启过或需要手动开启：Settings → Pages → Branch: main /docs")
print(f"   Logbook 网址：https://{owner}.github.io/{repo.split('/')[1]}/  （首次部署约 1–2 分钟）")

if a.project:
    print("⑤ Project 看板（需要 project 权限：gh auth refresh -s project）")
    r = gh("project", "create", "--owner", owner, "--title", "AI Engineer 90 Days", "--format", "json", check=False)
    if r.returncode != 0: print("   创建失败：", r.stderr.strip()); sys.exit(0)
    num = str(json.loads(r.stdout)["number"])
    allurls = [i["html_url"] for p in range(1,3) for i in json.loads(gh("api", f"repos/{repo}/issues?state=all&labels=daily&per_page=100&page={p}").stdout)]
    for u in sorted(allurls, key=lambda u: int(u.rsplit("/",1)[1])):
        gh("project", "item-add", num, "--owner", owner, "--url", u, check=False); time.sleep(0.5)
    print(f"   完成：https://github.com/users/{owner}/projects/{num}")
print("全部完成 ✅")
