"""Copy the chosen phases of AI Engineering from Scratch into docs/curriculum.

usage: python scripts/sync_curriculum.py <upstream clone> <zh clone>
"""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "curriculum"
VENDOR = ROOT / "docs" / "vendor" / "aiefs"


def commit(repo):
    return subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()


def heading(md):
    m = re.search(r"^# (.+)$", md, re.M)
    return m.group(1).strip() if m else ""


def minutes(md):
    m = re.search(r"\*\*(?:Time|预计时间)[:：]?\*\*[:：]?\s*~?\s*(\d+)", md)
    return int(m.group(1)) if m else None


def read(p):
    return p.read_text(encoding="utf-8") if p.exists() else ""


def main(up, zh):
    up, zh = Path(up), Path(zh)
    plan = json.loads((ROOT / "curriculum.json").read_text(encoding="utf-8"))
    providers = sorted(p for p in (up / "site").glob("figures*.js") if re.fullmatch(r"figures(-[a-z0-9-]+)?\.js", p.name))
    sources = {p.name: p.read_text(encoding="utf-8") for p in providers}

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    VENDOR.mkdir(parents=True, exist_ok=True)
    shutil.copy(up / "site" / "lesson-figures.js", VENDOR / "lesson-figures.js")

    index, used = [], set()
    for phase in plan["phases"]:
        src = up / "phases" / phase
        lessons = []
        for les in sorted(d for d in src.iterdir() if d.is_dir() and d.name[:2].isdigit()):
            dst = OUT / phase / les.name
            shutil.copytree(les, dst)
            # chinese text and quiz from the translation
            zles = zh / "phases" / phase / les.name
            if (zles / "docs" / "zh.md").exists():
                shutil.copy(zles / "docs" / "zh.md", dst / "docs" / "zh.md")
            if (zles / "quiz.json").exists() and (les / "quiz.json").exists():
                shutil.copy(zles / "quiz.json", dst / "quiz.zh.json")

            en, zmd = read(dst / "docs" / "en.md"), read(dst / "docs" / "zh.md")
            figs = re.findall(r"^```figure\n(\S+)", en, re.M)
            need = sorted({name for f in figs for name, s in sources.items() if re.search(rf"['\"]{re.escape(f)}['\"]", s)})
            used.update(need)
            lessons.append({
                "id": les.name,
                "en": heading(en),
                "zh": heading(zmd) or heading(en),
                "min": minutes(en),
                "quiz": (dst / "quiz.json").exists(),
                "code": sorted(str(p.relative_to(dst)) for p in (dst / "code").rglob("*") if p.is_file()) if (dst / "code").exists() else [],
                "figs": need,
            })
        index.append({
            "id": phase,
            "en": heading(read(src / "README.md")),
            "zh": heading(read(zh / "phases" / phase / "README.md")),
            "lessons": lessons,
        })

    for name in used:
        shutil.copy(up / "site" / name, VENDOR / name)
    shutil.copy(up / "LICENSE", OUT / "LICENSE")
    meta = {"upstream": plan["upstream"], "upstream_commit": commit(up),
            "translation": plan["translation"], "translation_commit": commit(zh)}
    (OUT / "index.json").write_text(json.dumps({"source": meta, "phases": index}, ensure_ascii=False, indent=1), encoding="utf-8")
    n = sum(len(p["lessons"]) for p in index)
    print(f"copied {n} lessons in {len(index)} phases, {len(used)} figure files")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(*sys.argv[1:])
