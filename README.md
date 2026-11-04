# Digital Incubation: AI Engineer Path

[![Live Demo](https://img.shields.io/badge/Logbook-Open-2ea44f?logo=githubpages&logoColor=white)](https://cheah20.github.io/DigitalIncubation/)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Plan](https://img.shields.io/badge/plan-90%20lessons-3f6fb6)
![Path](https://img.shields.io/badge/path-542%20lessons-3f6fb6)
![GitHub Issues](https://img.shields.io/badge/check--in-GitHub%20Issues-181717?logo=github&logoColor=white)

我的 AI Engineer 自学路线，也开放给任何想走同一条路的人：

- **90 课学习计划**：每课有讲解、名校公开课、练习和自测，配合每日打卡（GitHub Issues）。
- **课程路线（Path）**：从 [AI Engineering from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch) 完整搬进 20 个阶段、542 课，有中英文课文、练习代码和测验，在 Logbook 里直接学。

没有截止日，按自己的节奏走。进度只存在你自己的浏览器。

| 位置 | 用途 |
|---|---|
| `docs/index.html` | **Logbook**：每天的中英讲解、视频、资料、最新研究、电子书库、考试与验收（GitHub Pages 网址：`https://<用户名>.github.io/ai-engineer-90-days/`） |
| **Issues** | **每日打卡**：90 个 Issue，每个带任务清单；做完勾选，留言写时数与收获，**Close = 完成** |
| **Milestones** | 7 个阶段，带截止日期，自动显示完成百分比 |
| `docs/curriculum/` | **课程路线**：542 课的课文（`docs/en.md`、`docs/zh.md`）、代码和测验，来自 AI Engineering from Scratch |
| `curriculum.json` | 搬进了哪些阶段 |
| `scripts/sync_curriculum.py` | 上游更新后，用来重新同步课程 |
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

## 课程路线怎么用

1. 打开 [Logbook](https://cheah20.github.io/DigitalIncubation/#path)，选上方的「课程路线」。
2. 从阶段 0 开始，一课一课往下。右上角可以切换中文、English 或双语。
3. 先读课文，再自己写代码，最后做测验。练习代码在每课的 `code/` 里。
4. 做完按「标记为完成」。测验分数会自动保存，可以重做，路线页会显示每课的最高分。
5. 每个阶段最后有「阶段考」：从整个阶段的测验随机抽 20 题，记录最高分和日期。
6. 「更多 → 路线成果」一页列出每个阶段的完成度、测验平均和阶段考成绩。
7. 进度和分数存在浏览器，到「设置与备份」下载 `progress.json`，换电脑时恢复。

20 个阶段：环境与工具、数学基础、机器学习基础、深度学习核心、计算机视觉、NLP、语音与音频、Transformer、生成式 AI、强化学习、从零构建 LLM、LLM 工程、多模态、工具与协议、Agent 工程、自主系统、多 Agent 与群体、基础设施与生产、伦理安全与对齐、综合项目。

上游更新后，重新同步：

```bash
python scripts/sync_curriculum.py <ai-engineering-from-scratch 路径> <ai-engineering-from-scratch-zh 路径>
```

## Licence

- **Code** (the site, scripts and workflows): [MIT](LICENSE).
- **Study content** written for this repo (the 90-lesson plan, tasks, quizzes, exams, rubrics and notes): [CC BY-NC-SA 4.0](LICENSE-CONTENT). You may share and adapt it for non-commercial use with credit, under the same licence.
- **Path lessons** in `docs/curriculum/` and figure scripts in `docs/vendor/aiefs/` are copied from [AI Engineering from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch) by Rohit Ghumare and contributors, and the Chinese text from [ai-engineering-from-scratch-zh](https://github.com/fancyboi999/ai-engineering-from-scratch-zh). They stay under their [MIT licence](docs/curriculum/LICENSE). See [ATTRIBUTION.md](ATTRIBUTION.md).
- **Linked material** (lectures, slides, videos, books, courses) is not part of this repo and is not covered by any of these licences. It belongs to its authors and institutions. Only free, official links are listed; nothing else is copied or re-hosted.

## Notices

- This is a personal study plan. It is not affiliated with or endorsed by MIT, Stanford, CMU, Harvard or any other school, or by any platform it links to. Names and trademarks belong to their owners.
- Lessons were matched to lectures by hand and may be wrong. The course's own site is the source of truth.
- Some links need a free account (for example Kaggle) or are free to read online only. These are marked next to the link. Links can break or change their terms later.
- If anything is missing or wrong, or you have a copyright or intellectual property concern, please [open an issue](../../issues). I will fix or remove it quickly. Thank you.
