# Digital Incubation: AI Engineer Path

[![Live Demo](https://img.shields.io/badge/Logbook-Open-2ea44f?logo=githubpages&logoColor=white)](https://cheah20.github.io/DigitalIncubation/)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Plan](https://img.shields.io/badge/plan-90%20lessons-3f6fb6)
![Path](https://img.shields.io/badge/path-542%20lessons-3f6fb6)
![GitHub Issues](https://img.shields.io/badge/check--in-GitHub%20Issues-181717?logo=github&logoColor=white)

My self-study path to becoming an AI engineer, open to anyone who wants to follow the same route.

- **90-lesson plan**: each lesson has notes, matching university lectures, exercises and a self-test, with a daily check-in on GitHub Issues.
- **Learning path**: all 20 phases and 542 lessons of [AI Engineering from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch), in English and Chinese, with code, quizzes, phase exams and a results page.

There is no deadline. Go at your own pace; your progress stays in your own browser.

**Start learning:** https://cheah20.github.io/DigitalIncubation/

## Table of Contents

- [What Is Inside](#what-is-inside)
- [Using the Learning Path](#using-the-learning-path)
- [Using the 90-Lesson Plan](#using-the-90-lesson-plan)
- [Follow Along in Your Own Repo](#follow-along-in-your-own-repo)
- [Updating the Path](#updating-the-path)
- [Repository Structure](#repository-structure)
- [Licence](#licence)
- [Notices](#notices)

## What Is Inside

| Part | What it gives you |
|---|---|
| Logbook site | Lessons, lectures, reading, e-books, exams and weekly reviews, in English, Chinese or both |
| Learning path | 542 lessons with text, diagrams, runnable code and quizzes, from setup and maths to LLMs, agents and production |
| Scores and exams | Quiz scores are saved per lesson, every phase has a 20-question exam, and one page sums up your results |
| Daily check-in | One GitHub Issue per lesson with a task list; close it when you are done |
| Backup | Download your progress as `progress.json` and restore it on another computer |

The 20 phases of the path: setup and tooling, maths, machine learning, deep learning, computer vision, NLP, speech and audio, transformers, generative AI, reinforcement learning, LLMs from scratch, LLM engineering, multimodal AI, tools and protocols, agent engineering, autonomous systems, multi-agent systems, infrastructure and production, ethics and safety, and capstone projects.

## Using the Learning Path

1. Open the [learning path](https://cheah20.github.io/DigitalIncubation/#path) and start from Phase 0.
2. Read the lesson, write the code yourself, then take the quiz. Each lesson's `code/` folder holds a full reference solution, so look at it only after you have tried.
3. Press **Mark as done**. Your best quiz score shows next to the lesson.
4. At the end of a phase, take the **phase exam**: 20 random questions from that phase. The best score and its date are kept.
5. Open **More → Path results** to see every phase's progress, quiz average and exam score.

## Using the 90-Lesson Plan

1. Open today's lesson in the [logbook](https://cheah20.github.io/DigitalIncubation/).
2. Watch the lecture and read the notes, then do the exercises in `phaseN/dayNNN/`.
3. Answer the self-test and save your check-in. Review days and checkpoints use the weekly quiz and the exams pages.

## Follow Along in Your Own Repo

To get your own daily check-in issues and milestones, fork this repo, then run:

```bash
gh auth login
python3 scripts/setup_github.py --start 2026-11-01
```

Change the date to your Day 1. Add `--project` to also create a GitHub Project board. Commit your exercise code with the issue number, for example `git commit -m "feat(day012): add ruff and mypy config #12"`, and close the issue when the lesson is done.

## Updating the Path

The path lessons are copied from upstream with a script, so they can be refreshed when the course changes:

```bash
python3 scripts/sync_curriculum.py <path to ai-engineering-from-scratch> <path to ai-engineering-from-scratch-zh>
```

The phases to copy are listed in `curriculum.json`.

## Repository Structure

```text
DigitalIncubation/
├── docs/
│   ├── index.html          # logbook site
│   ├── data.json           # the 90-lesson plan
│   ├── courses.json        # university lectures
│   ├── curriculum/         # 542 path lessons (en.md, zh.md, code, quizzes)
│   └── vendor/aiefs/       # lesson figure scripts
├── scripts/
│   ├── setup_github.py     # daily issues and milestones
│   └── sync_curriculum.py  # copy the path lessons from upstream
├── phase1/ … phase7/       # my exercise code, one folder per lesson
├── dsa/                    # practice problems
├── logs/                   # experiment and bug logs
├── progress/               # progress.json backups
├── plan/                   # the plan as an Excel sheet
├── curriculum.json         # phases copied into the path
└── ATTRIBUTION.md
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
- If anything is missing or wrong, or you have a copyright or intellectual property concern, please [report a problem](../../issues/new?template=report-a-problem.yml). I will fix or remove it quickly. Thank you.
