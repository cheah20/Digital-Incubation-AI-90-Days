# Digital Incubation: AI 90 Days

90 天 AI Engineer 学习计划：每日打卡（GitHub Issues）+ 学习系统 Logbook（GitHub Pages）+ 练习代码。

| 位置 | 用途 |
|---|---|
| `docs/index.html` | **Logbook**：每天的中英讲解、视频、资料、最新研究、电子书库、考试与验收（GitHub Pages 网址：`https://<用户名>.github.io/ai-engineer-90-days/`） |
| **Issues** | **每日打卡**：90 个 Issue，每个带任务清单；做完勾选，留言写时数与收获，**Close = 完成** |
| **Milestones** | 7 个阶段，带截止日期，自动显示完成百分比 |
| `phase1/`…`phase7/` | 每天的练习代码，`phaseN/dayNNN/` |
| `dsa/` | 刷题记录 |
| `logs/` | 实验记录、Bug 记录 |
| `progress/` | Logbook 进度备份 `progress.json` |
| `plan/` | Excel 版计划 |

## 第一次设置（约 10 分钟）

**最简单：** 在 VS Code 打开这个文件夹，对 Claude 说：「读 CLAUDE.md，从第 4 节 S0 开始，一步步帮我把仓库连接到 GitHub。」

或者手动运行：

```bash
# WSL Ubuntu 里（不需要动现有 conda 环境）
type gh || sudo apt install gh        # 没有 gh 就安装；Ubuntu 20.04 若找不到，按 https://cli.github.com 的说明安装
gh auth login                         # 选 GitHub.com → HTTPS → 浏览器登录
cd ~/projects                         # 放在你喜欢的目录
unzip ai-engineer-90-days.zip && cd ai-engineer-90-days
git init -b main && git add . && git commit -m "chore: init 90-day plan"
gh repo create ai-engineer-90-days --public --source=. --push
python3 scripts/setup_github.py --start 2026-11-01   # 改成你的 Day 1 日期
```

## 每天怎么用

1. 打开今天的 Issue（Issues → 筛选 `milestone`/`label:daily`，或手机 GitHub App）。
2. 点 Issue 里的 Logbook 链接，看讲解、视频和资料。
3. 在 VS Code 打开这个文件夹写代码，放进 `phaseN/dayNNN/`，commit 信息里写 `#Issue编号`：
   `git commit -m "feat(day012): ruff + mypy config #12"`
4. 在 Issue 里勾任务，留言写打卡（时数 / 理解 1–5 / 收获 / 问题），然后 **Close issue**。
5. 复盘日、验收日在 Logbook 的「周复盘小测」「考试与验收」完成，成绩截图贴回 Issue。
