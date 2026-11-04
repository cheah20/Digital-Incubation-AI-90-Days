# Attribution

The lessons in `docs/curriculum/` and the figure scripts in `docs/vendor/aiefs/` are copied from these projects. They are not my work.

| Part | From | Licence | Copied at |
|---|---|---|---|
| English lessons, code, quizzes, figures | [AI Engineering from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch) by Rohit Ghumare and contributors | MIT | `ddaad269bc5ae3c9c1e73251e0500b9fabd9181b` |
| Chinese lessons (`docs/zh.md`) and quizzes (`quiz.zh.json`) | [ai-engineering-from-scratch-zh](https://github.com/fancyboi999/ai-engineering-from-scratch-zh) | MIT | `65c81837d6768d4036a3833f7494822fbb02d8f7` |

The MIT licence text is kept in [docs/curriculum/LICENSE](docs/curriculum/LICENSE).

The phases copied in are listed in [curriculum.json](curriculum.json). To update them:

```bash
python scripts/sync_curriculum.py <path to ai-engineering-from-scratch> <path to ai-engineering-from-scratch-zh>
```

My own work in this repo is the 90-lesson plan, the logbook site, the exams, the daily check-ins and my exercise code in `phase1/` to `phase7/`.
