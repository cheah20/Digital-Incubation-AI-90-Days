# Digital Incubation: AI 90 Days

[![Live Demo](https://img.shields.io/badge/Logbook-Open-2ea44f?logo=githubpages&logoColor=white)](https://cheah20.github.io/DigitalIncubation/)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Days](https://img.shields.io/badge/plan-90%20days-3f6fb6)
![GitHub Issues](https://img.shields.io/badge/check--in-GitHub%20Issues-181717?logo=github&logoColor=white)

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

手动运行：

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

## Licence

- **Code** (the site, scripts and workflows): [MIT](LICENSE).
- **Study content** written for this repo (the 90-lesson plan, tasks, quizzes, exams, rubrics and notes): [CC BY-NC-SA 4.0](LICENSE-CONTENT). You may share and adapt it for non-commercial use with credit, under the same licence.
- **Linked material** (lectures, slides, videos, books, courses) is not part of this repo and is not covered by either licence. It belongs to its authors and institutions. Only free, official links are listed; nothing is copied or re-hosted.

## Notices

- This is a personal study plan. It is not affiliated with or endorsed by MIT, Stanford, CMU, Harvard or any other school, or by any platform it links to. Names and trademarks belong to their owners.
- Lessons were matched to lectures by hand and may be wrong. The course's own site is the source of truth.
- Some links need a free account (for example Kaggle) or are free to read online only. These are marked next to the link. Links can break or change their terms later.
- If anything is missing or wrong, or you have a copyright or intellectual property concern, please [open an issue](../../issues). I will fix or remove it quickly. Thank you.
