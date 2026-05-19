"""Regenerate all gen README.md files from index.ts data, without answer code leak."""
import json, re, sys
from pathlib import Path

GOTCHAS: dict[str, str] = {
    "try-except": "- `except:` 不加异常类型会捕获所有异常(包括 KeyboardInterrupt)，通常不推荐\n- `except Exception as e:` 中的 `as e` 可以获取异常对象\n- `finally` 无论是否发生异常都会执行",
    "type-hints": "- 类型标注只是提示，Python 运行时不做类型检查\n- `from typing import List, Dict, Optional` 在 Python 3.9+ 可用内置 `list`, `dict` 替代\n- 返回值类型用 `->` 箭头",
    "decorator": "- 装饰器本质是 `decorator(func)` 返回新函数\n- 内层 `wrapper` 用 `*args, **kwargs` 接收任意参数\n- `functools.wraps(func)` 保留原函数的 `__name__` 和 `__doc__`",
    "context-manager": "- `with` 语句块结束时自动调用 `__exit__`，即使发生异常\n- `__exit__` 返回 `True` 可以抑制异常（谨慎使用）\n- 也可以用 `contextlib.contextmanager` 装饰器 + `yield` 实现",
    "cli": "- `if __name__ == '__main__':` 保证脚本既能导入又能直接运行\n- Click 的 `@click.option('--name')` 自动生成 `--help` 文档\n- argparse 的 `add_argument` 支持 `type=int` 自动类型转换",
    "class": "- `__init__` 不是构造器，是初始化方法（构造器是 `__new__`）\n- 实例方法的第一个参数必须显式写 `self`\n- `pass` 是一个空语句，占位用",
    "exception": "- 自定义异常让调用方可以精确 `except` 特定错误\n- 异常类名通常以 `Error` 或 `Exception` 结尾\n- 继承 `Exception` 而非 `BaseException`（后者包括系统退出信号）",
}

LEVELS_DIR = Path(__file__).resolve().parent.parent / "src" / "levels"


def extract_fields(ts: str) -> dict:
    """Parse key fields from generated index.ts."""
    out: dict = {}
    m = re.search(r'title:\s*"([^"]*)"', ts)
    if m:
        out["title"] = m.group(1)
    m = re.search(r"description:\s*`((?:[^`]|\\`)*)`", ts)
    if m:
        out["desc_raw"] = m.group(1).replace("\\`", "`").replace("\\n", "\n").strip()
    m = re.search(r"hint:\s*`((?:[^`]|\\`)*)`", ts)
    if m:
        out["hint"] = m.group(1).replace("\\`", "`").replace("\\n", "\n").strip()
    m = re.search(r"tags:\s*(\[[^\]]*\])", ts)
    if m:
        out["tags"] = json.loads(m.group(1))
    return out


def rebuild_readme(data: dict, key: str) -> str:
    title = data.get("title", key)
    lid = int(key.replace("gen", ""))
    desc_raw = data.get("desc_raw", "")
    hint = data.get("hint", "")
    tags = data.get("tags", [])

    # Split desc into: intro + task + source
    lines = desc_raw.split("\n")
    desc_lines: list[str] = []
    task = ""
    repo = ""
    src_file = ""
    for line in lines:
        if line.startswith("来源："):
            src = line.replace("来源：", "").strip()
            parts_src = src.split(" — ", 1)
            if len(parts_src) == 2:
                repo, src_file = parts_src
            break
        if line.startswith("编写") or line.startswith("定义") or line.startswith("创建"):
            task = line.strip()
            continue
        desc_lines.append(line)

    desc_clean = "\n".join(desc_lines).strip()

    parts = [f"# 第{lid}关: {title}"]
    if repo:
        parts.append(f"\n> 真实案例：{repo} 的 `{src_file}` 中使用了这个模式。")
    parts.append(f"\n## 概念介绍\n")
    parts.append(desc_clean)
    if hint:
        parts.append(f"\n## 关键点\n")
        parts.append(hint)
    for tag, gotcha_text in GOTCHAS.items():
        if tag in tags:
            parts.append(f"\n## 常见陷阱\n")
            parts.append(gotcha_text)
            break
    if task:
        parts.append(f"\n## 你的任务\n")
        parts.append(task)
    parts.append("\n请按照上方任务描述编写代码。")
    return "\n".join(parts) + "\n"


def main():
    count = 0
    for d in sorted(LEVELS_DIR.glob("gen*")):
        ts_path = d / "index.ts"
        if not ts_path.exists():
            continue
        ts_content = ts_path.read_text(encoding="utf-8")
        data = extract_fields(ts_content)
        readme = rebuild_readme(data, d.name)
        (d / "README.md").write_text(readme, encoding="utf-8")
        count += 1
    print(f"Fixed {count} README.md files")


if __name__ == "__main__":
    main()
