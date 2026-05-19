"""Convert generated JSON levels to python-mother TypeScript format."""

import json
import shutil
from pathlib import Path

LEVELS_DIR = Path(__file__).resolve().parent / "levels"
TARGET_DIR = Path(__file__).resolve().parent.parent / "src" / "levels"

# Tag → category mapping
TAG_CATEGORY = {
    "exception": "进阶", "class": "进阶", "inheritance": "进阶",
    "testing": "中级", "pytest": "中级", "fixture": "中级",
    "cli": "中级", "click": "中级", "argparse": "中级",
    "module": "进阶", "api-design": "进阶", "__all__": "进阶",
    "decorator": "进阶", "functional": "进阶",
    "context-manager": "进阶", "with-statement": "进阶",
    "error-handling": "中级", "try-except": "中级",
    "type-hints": "中级", "annotations": "中级",
}

# difficulty string → number
DIFF_MAP = {"basic": 1, "intermediate": 3, "advanced": 5}


def escape_ts_string(s: str) -> str:
    return s.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")


def convert():
    json_files = sorted(LEVELS_DIR.glob("*.json"))
    print(f"Found {len(json_files)} JSON level files")

    created = 0
    for jf in json_files:
        try:
            data = json.loads(jf.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, KeyError):
            continue

        lid = data.get("id")
        if not lid:
            continue

        dirname = f"gen{lid}"
        target = TARGET_DIR / dirname
        target.mkdir(parents=True, exist_ok=True)

        # Determine category from tags
        tags = data.get("tags", [])
        category = "中级"
        for tag in tags:
            if tag in TAG_CATEGORY:
                category = TAG_CATEGORY[tag]
                break

        # Determine difficulty
        diff_str = data.get("difficulty", "intermediate")
        difficulty = DIFF_MAP.get(diff_str, 3)

        # Map judge_mode → compareMode
        judge_mode = data.get("judge_mode", "return")
        compare_mode = judge_mode  # "stdout" | "return" | "both"

        # Build index.ts
        title = data.get("title", f"Level {lid}")
        description = data.get("description", "")
        hint = data.get("hint", "")
        task = data.get("task", "")
        template = data.get("template", "")
        expected_code = data.get("expected_code", "")
        source_repo = data.get("source_repo", "")
        source_file = data.get("source_file", "")

        full_desc = description
        if task:
            full_desc += f"\n\n任务：{task}"
        if source_repo:
            full_desc += f"\n\n来源：{source_repo} — {source_file}"

        default_code = template if template else "# 请在此处编写代码\n"

        tags_str = json.dumps(tags, ensure_ascii=False)

        index_ts = f"""import type {{ LevelType }} from "../level.d";

const level: LevelType = {{
  key: "{dirname}",
  title: "{escape_ts_string(title)}",
  category: "{category}",
  description: `{escape_ts_string(full_desc)}`,
  content: "",
  defaultCode: `{escape_ts_string(default_code)}`,
  answer: "",
  hint: `{escape_ts_string(hint)}`,
  type: "main",
  difficulty: {difficulty},
  compareMode: "{compare_mode}",
  tags: {tags_str},
}};

export default level;
"""
        (target / "index.ts").write_text(index_ts, encoding="utf-8")

        # Write answer.py
        answer_py = expected_code if expected_code else "# 请在此处编写代码\n"
        (target / "answer.py").write_text(answer_py, encoding="utf-8")

        created += 1

    print(f"Created {created} level directories in {TARGET_DIR}")


if __name__ == "__main__":
    convert()
