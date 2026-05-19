"""Python-Mother level generator — scaffold for Reasonix.

Scans reference repos, extracts teachable patterns, generates level JSON files.

Usage:
  python generate.py --repo-dir <path> --output-dir <path> --start-id 109
"""

from __future__ import annotations

import ast
import json
import sys
from pathlib import Path
from typing import Any

# ── AST compatibility helpers ────────────────────────────────────

# ast.Str was used for string literals in Python 3.7 and earlier;
# ast.Constant replaced it in 3.8+. Provide a unified accessor.
_StrType = getattr(ast, "Str", None) or (lambda s: isinstance(s, ast.Constant) and isinstance(s.value, str))


def _unparse(node: ast.AST) -> str:
    """Unparse an AST node to source text. Uses ast.unparse on 3.9+, fallback otherwise."""
    if hasattr(ast, "unparse"):
        return ast.unparse(node)
    # Fallback for Python < 3.9: reconstruct from known node types
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return f"{_unparse(node.value)}.{node.attr}"
    if isinstance(node, ast.Call):
        func_str = _unparse(node.func)
        args_str = ", ".join(_unparse(a) for a in node.args)
        kw_str = ", ".join(f"{kw.arg}={_unparse(kw.value)}" for kw in node.keywords)
        all_args = ", ".join(filter(None, [args_str, kw_str]))
        return f"{func_str}({all_args})"
    if isinstance(node, ast.Subscript):
        return f"{_unparse(node.value)}[{_unparse(node.slice)}]"
    if isinstance(node, ast.Constant):
        return repr(node.value)
    if isinstance(node, ast.Tuple):
        return ", ".join(_unparse(e) for e in node.elts)
    if isinstance(node, ast.BinOp):
        return f"{_unparse(node.left)} {_unparse_op(node.op)} {_unparse(node.right)}"
    return str(node)


def _unparse_op(op: ast.operator) -> str:
    if isinstance(op, ast.Add): return "+"
    if isinstance(op, ast.Sub): return "-"
    if isinstance(op, ast.Mult): return "*"
    if isinstance(op, ast.Div): return "/"
    if isinstance(op, ast.BitOr): return "|"
    return str(op)


def _is_str_constant(node: ast.expr) -> bool:
    """Check if node is a string literal (works across Python 3.7 / 3.8+)."""
    if hasattr(ast, "Str"):
        return isinstance(node, ast.Str)
    return isinstance(node, ast.Constant) and isinstance(node.value, str)


def _get_str_value(node: ast.expr) -> str:
    """Extract string value from a Constant or Str node."""
    if hasattr(ast, "Str") and isinstance(node, ast.Str):
        return node.s
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return ""


# ── Default judge options (LENIENT) ────────────────────────────

LENIENT_JUDGE: dict[str, Any] = {
    "normalizePunctuation": True,
    "trimWhitespace": True,
    "ignoreTrailingNewline": True,
    "numericTolerance": 0.001,
    "ignoreCase": False,
}


# ── Pattern extractors ──────────────────────────────────────────
# Reasonix: implement one extractor per pattern type.
# Each returns list[dict] with keys: title, difficulty, description,
#   hint, task, expected_code, template, judge_mode, tags


def extract_exception_hierarchy(filepath: Path, repo: str) -> list[dict]:
    """Given exceptions.py, extract a level about custom exception classes."""
    try:
        source = filepath.read_text(encoding="utf-8")
    except Exception:
        return []

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []

    # Collect classes that inherit from Exception / Error / Warning
    exc_nodes: list[ast.ClassDef] = []
    exc_names: set[str] = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.ClassDef):
            continue
        if node.name.startswith("_"):
            continue
        for base in node.bases:
            base_name = ast.unparse(base) if hasattr(ast, "unparse") else _unparse(base)
            # Heuristic: base is Exception, or ends with Exception / Error / Warning
            if base_name in ("Exception", "BaseException", "Warning"):
                exc_nodes.append(node)
                exc_names.add(node.name)
                break
            if base_name.endswith("Exception") or base_name.endswith("Error") or base_name.endswith("Warning"):
                exc_nodes.append(node)
                exc_names.add(node.name)
                break

    if len(exc_nodes) < 2:
        return []

    # Build a simple hierarchy: find root (inherits from Exception directly) and children
    root_nodes = [n for n in exc_nodes if any(
        ast.unparse(b) if hasattr(ast, "unparse") else _unparse(b)
        in ("Exception", "BaseException", "Warning")
        for b in n.bases
    )]
    if not root_nodes:
        root_nodes = exc_nodes[:1]

    root = root_nodes[0]
    children = [n for n in exc_nodes if n != root and any(
        (ast.unparse(b) if hasattr(ast, "unparse") else _unparse(b)) == root.name
        for b in n.bases
    )]
    if not children:
        # Pick 2-3 other classes as children (even if not direct subclass)
        children = exc_nodes[1:min(4, len(exc_nodes))]

    selected = [root] + children[:3]

    # Build expected_code lines
    def class_sig(node: ast.ClassDef) -> str:
        bases_str = ", ".join(
            ast.unparse(b) if hasattr(ast, "unparse") else _unparse(b)
            for b in node.bases
        )
        return f"class {node.name}({bases_str}):"

    expected_lines = []
    for node in selected:
        expected_lines.append(class_sig(node))
        expected_lines.append("    pass")
    expected = "\n".join(expected_lines)

    # Build template: give the root class, ask for children
    child_names = [n.name for n in selected[1:]]
    template = f"{class_sig(root)}\n    pass\n\n# 定义 {', '.join(child_names)}，继承自 {root.name}"

    names_list = ", ".join(f"{n.name}({', '.join(ast.unparse(b) if hasattr(ast, 'unparse') else _unparse(b) for b in n.bases)})" for n in selected)

    return [{
        "title": f"定义异常类层级: {root.name}",
        "description": (
            f"好的代码库用自定义异常类让调用方精确捕获不同错误。\n\n"
            f"源文件 {filepath.name} 定义了如下继承层级：\n"
            + "\n".join(f"  • {n.name} → {', '.join(ast.unparse(b) if hasattr(ast, 'unparse') else _unparse(b) for b in n.bases)}" for n in selected) +
            f"\n\n请按照这个模式编写这些异常类（每个类只需 pass 语句体）。"
        ),
        "hint": "class 子类名(父类名): —— 父类写在括号里，多个父类用逗号分隔",
        "task": f"定义以下异常类: {names_list}",
        "expected_code": expected,
        "template": template,
        "tags": ["exception", "class", "inheritance"],
    }]


def extract_test_fixtures(filepath: Path, repo: str) -> list[dict]:
    """Given conftest.py, extract a level about pytest fixtures."""
    try:
        source = filepath.read_text(encoding="utf-8")
    except Exception:
        return []

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []

    # Find functions decorated with @pytest.fixture
    fixtures: list[ast.FunctionDef] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef):
            continue
        if node.name.startswith("_"):
            continue
        for dec in node.decorator_list:
            dec_str = ast.unparse(dec) if hasattr(ast, "unparse") else _unparse(dec)
            # Match @pytest.fixture or @pytest.fixture() or @pytest.fixture(...)
            if "pytest.fixture" in dec_str or dec_str == "fixture":
                fixtures.append(node)
                break

    if not fixtures:
        return []

    # Pick the simplest fixture (shortest body)
    fixture = min(fixtures, key=lambda f: len(f.body))

    # Check if it uses yield (teardown) or return
    uses_yield = any(isinstance(stmt, ast.Yield) or (isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Yield))
                     for stmt in ast.walk(fixture))

    fixture_name = fixture.name

    # Build a clean expected_code
    expected = f"@pytest.fixture\ndef {fixture_name}():\n"
    if uses_yield:
        expected += f"    data = {{'name': 'test', 'value': 42}}\n    yield data\n    print('cleanup done')"
    else:
        expected += f"    return {{'name': 'test', 'value': 42}}"

    template = f"import pytest\n\n# 编写 {fixture_name} fixture"

    hint = "用 @pytest.fixture 装饰器"
    if uses_yield:
        hint += "，函数体内 yield 数据，yield 之后写清理代码"
    else:
        hint += "，函数体内 return 数据"

    return [{
        "title": f"编写 pytest fixture: {fixture_name}",
        "description": (
            f"pytest 用 fixture 管理测试的共享资源（数据库连接、测试客户端等）。\n\n"
            f"源文件 {filepath.name} 定义了 fixture `{fixture_name}`。\n\n"
            f"请仿照这个模式，编写一个 fixture 函数 `{fixture_name}`。"
        ),
        "hint": hint,
        "task": f"编写一个名为 {fixture_name} 的 pytest fixture，返回字典 {{'name': 'test', 'value': 42}}"
                + ("，并在 cleanup 阶段打印 'cleanup done'。" if uses_yield else "。"),
        "expected_code": expected,
        "template": template,
        "tags": ["testing", "pytest", "fixture"],
    }]


def extract_cli_patterns(filepath: Path, repo: str) -> list[dict]:
    """Given cli.py / __main__.py with Click/argparse, extract CLI levels."""
    try:
        source = filepath.read_text(encoding="utf-8")
    except Exception:
        return []

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []

    # Look for Click-style commands: functions decorated with @click.command / @click.group
    click_funcs: list[ast.FunctionDef] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef):
            continue
        if node.name.startswith("_"):
            continue
        for dec in node.decorator_list:
            dec_str = ast.unparse(dec) if hasattr(ast, "unparse") else _unparse(dec)
            if "click.command" in dec_str or "click.group" in dec_str or dec_str == "command":
                click_funcs.append(node)
                break

    # If no Click, check for argparse patterns
    if not click_funcs:
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                call_str = ast.unparse(node) if hasattr(ast, "unparse") else _unparse(node)
                if "add_argument" in call_str:
                    # Found argparse usage — generate a simple argparse level
                    return [{
                        "title": "编写 argparse CLI 命令",
                        "description": (
                            f"argparse 是 Python 标准库的 CLI 模块。\n\n"
                            f"源文件 {filepath.name} 使用了 argparse 构建命令行接口。\n\n"
                            f"请仿照此模式，创建一个带 --name 参数的 CLI 脚本。"
                        ),
                        "hint": "parser = argparse.ArgumentParser(); parser.add_argument('--name'); args = parser.parse_args()",
                        "task": "创建一个 argparse 解析器，添加 --name 参数，然后打印 args.name 的值。",
                        "expected_code": (
                            "import argparse\n\n"
                            "parser = argparse.ArgumentParser()\n"
                            "parser.add_argument('--name', default='World')\n"
                            "args = parser.parse_args()\n"
                            "print(f'Hello, {args.name}!')"
                        ),
                        "template": "import argparse\n\n# 创建解析器并添加 --name 参数",
                        "tags": ["cli", "argparse"],
                    }]
                if "ArgumentParser" in call_str:
                    break
        return []

    # Use the simplest Click command found
    cmd = min(click_funcs, key=lambda f: len(f.body))
    cmd_name = cmd.name

    # Check for @click.option decorators
    options: list[str] = []
    for dec in cmd.decorator_list:
        dec_str = ast.unparse(dec) if hasattr(ast, "unparse") else _unparse(dec)
        if "click.option" in dec_str:
            # Extract the option name from decorator string
            options.append(dec_str)

    expected = f"import click\n\n@click.command()\n"
    for opt in options[:2]:
        expected += f"{opt}\n"
    expected += f"def {cmd_name}():\n    click.echo('Hello, World!')"

    template = f"import click\n\n# 编写 {cmd_name} 命令"

    return [{
        "title": f"编写 Click CLI 命令: {cmd_name}",
        "description": (
            f"Click 是 Python 生态中最流行的 CLI 框架之一。\n\n"
            f"源文件 {filepath.name} 使用 @click.command() 定义 CLI 入口。\n\n"
            f"请仿照此模式编写一个简单的 Click 命令。"
        ),
        "hint": "用 @click.command() 装饰函数，用 click.echo() 输出",
        "task": f"编写一个 Click 命令 {cmd_name}，用 click.echo() 输出 'Hello, World!'。",
        "expected_code": expected,
        "template": template,
        "tags": ["cli", "click"],
    }]


def extract_api_exports(filepath: Path, repo: str) -> list[dict]:
    """Given __init__.py with __all__, extract level about public API design."""
    try:
        source = filepath.read_text(encoding="utf-8")
    except Exception:
        return []

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []

    # Find __all__ assignment with 5+ entries
    all_names: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__all__":
                    if isinstance(node.value, (ast.List, ast.Tuple)):
                        for elt in node.value.elts:
                            if _is_str_constant(elt):
                                all_names.append(_get_str_value(elt))
                    break

    # Filter out private names
    all_names = [n for n in all_names if not n.startswith("_")]

    if len(all_names) < 5:
        return []

    # Pick a subset of names for the task
    selected = all_names[:6]
    expected_list = "[\n    " + ",\n    ".join(f'"{n}"' for n in selected) + ",\n]"
    expected = f"__all__ = {expected_list}"

    template = f"# 定义 __all__ 暴露以下公共 API: {', '.join(selected[:3])} ..."

    return [{
        "title": "定义模块的公共 API",
        "description": (
            f"__all__ 是 Python 模块的公共接口声明，控制 `from module import *` 的行为。\n\n"
            f"源文件 {filepath.name} 暴露了 {len(all_names)} 个公开符号。\n\n"
            f"请仿照此模式，为以下符号定义 __all__ 列表。"
        ),
        "hint": "__all__ = ['Name1', 'Name2', ...] —— 字符串列表",
        "task": f"定义 __all__ 列表，包含以下 {len(selected)} 个公开符号: " + ", ".join(selected),
        "expected_code": expected,
        "template": template,
        "tags": ["module", "api-design", "__all__"],
    }]


def extract_decorator_patterns(filepath: Path, repo: str) -> list[dict]:
    """Given any .py file with custom decorators, extract decorator level."""
    try:
        source = filepath.read_text(encoding="utf-8")
    except Exception:
        return []

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []

    # Find functions that define an inner function named "wrapper" and return it
    decorators: list[ast.FunctionDef] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef):
            continue
        if node.name.startswith("_"):
            continue
        if not node.args.args:
            continue
        inner_funcs = [
            n for n in ast.walk(node)
            if isinstance(n, ast.FunctionDef) and n != node
        ]
        if not inner_funcs:
            continue
        # Check if the function returns one of its inner functions
        for stmt in ast.walk(node):
            if isinstance(stmt, ast.Return) and isinstance(stmt.value, ast.Name):
                if any(inner.name == stmt.value.id for inner in inner_funcs):
                    decorators.append(node)
                    break

    if not decorators:
        return []

    # Pick the simplest decorator
    dec = min(decorators, key=lambda f: len(f.body))
    inner = next(
        (n for n in ast.walk(dec)
         if isinstance(n, ast.FunctionDef) and n != dec),
        None
    )

    inner_name = inner.name if inner else "wrapper"
    dec_name = dec.name

    expected = (
        f"def {dec_name}(func):\n"
        f"    def {inner_name}(*args, **kwargs):\n"
        f"        print('before call')\n"
        f"        result = func(*args, **kwargs)\n"
        f"        print('after call')\n"
        f"        return result\n"
        f"    return {inner_name}"
    )

    template = f"# 编写装饰器 {dec_name}"

    return [{
        "title": f"编写装饰器: {dec_name}",
        "description": (
            f"装饰器是 Python 中用于包装函数、添加横切关注点的强大模式。\n\n"
            f"源文件 {filepath.name}（{repo}）中 `{dec_name}` 展示了装饰器模式。\n\n"
            f"请编写一个装饰器，在函数调用前后各打印一行信息。"
        ),
        "hint": "外层函数接受 func 参数，内层定义 wrapper(*args, **kwargs)，外层 return wrapper",
        "task": f"编写装饰器 {dec_name}，包装目标函数并在调用前后打印 'before call' 和 'after call'。",
        "expected_code": expected,
        "template": template,
        "tags": ["decorator", "functional"],
    }]


def extract_context_manager(filepath: Path, repo: str) -> list[dict]:
    """Given .py with __enter__/__exit__, extract context manager level."""
    try:
        source = filepath.read_text(encoding="utf-8")
    except Exception:
        return []

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []

    # Find classes that have both __enter__ and __exit__ methods
    ctx_classes: list[ast.ClassDef] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.ClassDef):
            continue
        if node.name.startswith("_"):
            continue
        methods = {
            m.name for m in node.body
            if isinstance(m, ast.FunctionDef)
        }
        if "__enter__" in methods and "__exit__" in methods:
            ctx_classes.append(node)

    if not ctx_classes:
        return []

    # Pick the simplest context manager
    cls = min(ctx_classes, key=lambda c: len(c.body))
    cls_name = cls.name

    expected = (
        f"class {cls_name}:\n"
        f"    def __init__(self, name):\n"
        f"        self.name = name\n"
        f"\n"
        f"    def __enter__(self):\n"
        f"        print(f'Entering {{self.name}}')\n"
        f"        return self\n"
        f"\n"
        f"    def __exit__(self, exc_type, exc_val, exc_tb):\n"
        f"        print(f'Exiting {{self.name}}')\n"
        f"        return False"
    )

    template = f"# 编写上下文管理器 {cls_name}"

    return [{
        "title": f"编写上下文管理器: {cls_name}",
        "description": (
            f"上下文管理器（Context Manager）用 with 语句管理资源的获取和释放。\n\n"
            f"源文件 {filepath.name} 定义了类 `{cls_name}`，实现了 __enter__ / __exit__。\n\n"
            f"请仿照此模式编写一个上下文管理器，在进入和退出时打印信息。"
        ),
        "hint": "实现 __enter__(self) 返回 self，__exit__(self, exc_type, exc_val, exc_tb) 处理清理",
        "task": f"编写类 {cls_name}，实现 __enter__ 和 __exit__，进入时打印 'Entering {{name}}'，退出时打印 'Exiting {{name}}'。",
        "expected_code": expected,
        "template": template,
        "tags": ["context-manager", "class", "with-statement"],
    }]


def extract_error_handling(filepath: Path, repo: str) -> list[dict]:
    """Given .py with try/except/finally chains, extract error handling level."""
    try:
        source = filepath.read_text(encoding="utf-8")
    except Exception:
        return []

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []

    # Find Try nodes that have at least one handler and optionally a finally
    try_nodes: list[ast.Try] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Try) and node.handlers:
            # Skip trivial try/except
            if len(node.handlers) >= 1:
                try_nodes.append(node)

    if not try_nodes:
        return []

    # Collect exception types used across all try blocks
    exc_types: set[str] = set()
    for tn in try_nodes:
        for handler in tn.handlers:
            if handler.type:
                exc_name = ast.unparse(handler.type) if hasattr(ast, "unparse") else _unparse(handler.type)
                exc_types.add(exc_name)
            else:
                exc_types.add("Exception")

    # Filter out private/weird exception names
    exc_types = {e for e in exc_types if not e.startswith("_")}

    if not exc_types:
        exc_types = {"ValueError", "KeyError"}

    exc_list = sorted(exc_types)[:3]

    # Build a multi-except level
    except_lines = []
    for exc in exc_list:
        except_lines.append(f"    except {exc} as e:")
        except_lines.append(f"        print(f'Caught {exc}: {{e}}')" if "{" not in exc else f"        print(f'Caught error: {{e}}')")

    expected = (
        "try:\n"
        "    result = int('not a number')\n"
        + "\n".join(except_lines) +
        "\nfinally:\n"
        "    print('Cleanup complete')"
    )

    template = "# 编写 try/except/finally 错误处理"

    return [{
        "title": "编写 try/except 错误处理",
        "description": (
            f"健壮的代码用 try/except 优雅地处理异常。\n\n"
            f"源文件 {filepath.name} 使用了 try/except 捕获多种异常类型。\n\n"
            f"请仿照此模式编写错误处理代码。"
        ),
        "hint": "try: ... except SomeError as e: ... finally: ...",
        "task": f"编写 try/except 块：尝试 int('not a number')，捕获 {', '.join(exc_list)}，并在 finally 中打印 'Cleanup complete'。",
        "expected_code": expected,
        "template": template,
        "tags": ["error-handling", "try-except"],
    }]


def extract_type_annotation(filepath: Path, repo: str) -> list[dict]:
    """Given .py with rich type annotations, extract type hint level."""
    try:
        source = filepath.read_text(encoding="utf-8")
    except Exception:
        return []

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []

    # Find functions where at least 2 params have type annotations AND has a return annotation
    typed_funcs: list[ast.FunctionDef] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef):
            continue
        # Skip private/dunder methods
        if node.name.startswith("_"):
            continue
        # Count annotated params (excluding self/cls)
        annotated = [
            a for a in node.args.args
            if a.annotation and a.arg not in ("self", "cls")
        ]
        if len(annotated) >= 2 and node.returns:
            typed_funcs.append(node)

    if not typed_funcs:
        return []

    # Pick a representative function
    func = typed_funcs[0]
    func_name = func.name

    func_name = func.name

    # Build annotated function signature from source types
    params = []
    for arg in func.args.args:
        if arg.arg in ("self", "cls"):
            params.append(arg.arg)
            continue
        hint = "Any"
        if arg.annotation:
            hint = ast.unparse(arg.annotation) if hasattr(ast, "unparse") else _unparse(arg.annotation)
        params.append(f"{arg.arg}: {hint}")

    ret_hint = "None"
    if func.returns:
        ret_hint = ast.unparse(func.returns) if hasattr(ast, "unparse") else _unparse(func.returns)

    params_str = ", ".join(params)
    return_body = f"    return f'{func_name} result'"

    expected = f"def {func_name}({params_str}) -> {ret_hint}:\n{return_body}"

    template = f"# 编写带类型标注的函数 {func_name}"

    return [{
        "title": f"编写带类型标注的函数: {func_name}",
        "description": (
            f"类型标注使代码更可读、IDE 能提供更好的自动补全。\n\n"
            f"源文件 {filepath.name}（{repo}）中 `{func_name}` 展示了完整的参数和返回值类型标注。\n\n"
            f"请仿照此模式编写一个带类型标注的函数。"
        ),
        "hint": "def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型",
        "task": f"编写函数 {func_name}({params_str}) -> {ret_hint}，返回格式化字符串。",
        "expected_code": expected,
        "template": template,
        "tags": ["type-hints", "annotations"],
    }]


# ── Registry ─────────────────────────────────────────────────────

EXTRACTORS = [
    ("exceptions.py", extract_exception_hierarchy, "intermediate"),
    ("errors.py", extract_exception_hierarchy, "intermediate"),
    ("conftest.py", extract_test_fixtures, "intermediate"),
    ("cli.py", extract_cli_patterns, "intermediate"),
    ("__main__.py", extract_cli_patterns, "intermediate"),
    ("__init__.py", extract_api_exports, "basic"),
]

# General extractors (apply to any .py file), no per-repo cap — dedup handles repeats
GENERAL_EXTRACTORS = [
    extract_decorator_patterns,
    extract_context_manager,
    extract_error_handling,
    extract_type_annotation,
]


# ── Repo scanner ─────────────────────────────────────────────────

def scan_repo(repo_path: Path, repo_name: str) -> list[dict]:
    """Scan one repo and extract all levels."""
    levels = []

    # Named-file extractors
    for filename, extractor, default_difficulty in EXTRACTORS:
        matches = list(repo_path.rglob(filename))
        for fpath in matches[:10]:  # max 10 per file type per repo
            if "test" in str(fpath).lower() or "site-packages" in str(fpath):
                continue
            try:
                extracted = extractor(fpath, repo_name)
                for level in extracted:
                    level.setdefault("difficulty", default_difficulty)
                    level["source_repo"] = repo_name
                    level["source_file"] = str(fpath.relative_to(repo_path))
                levels.extend(extracted)
            except Exception:
                pass  # skip unparseable files silently

    # General extractors on sample of Python files
    py_files = [f for f in repo_path.rglob("*.py")
                if "test" not in str(f).lower()
                and "migration" not in str(f).lower()
                and "site-packages" not in str(f)]
    for fpath in py_files[:50]:
        for extractor in GENERAL_EXTRACTORS:
            try:
                extracted = extractor(fpath, repo_name)
                for level in extracted:
                    level["source_repo"] = repo_name
                    level["source_file"] = str(fpath.relative_to(repo_path))
                    level["_extractor"] = extractor.__name__
                levels.extend(extracted)
            except Exception:
                pass

    return levels


# ── Level writer ─────────────────────────────────────────────────

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
DIFF_MAP = {"basic": 1, "intermediate": 3, "advanced": 5}


def _esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")


def _build_readme(level: dict, level_id: int) -> str:
    """Build a README.md with teaching content for a level."""
    title = level.get("title", f"Level {level_id}")
    desc = level.get("description", "")
    task = level.get("task", "")
    hint = level.get("hint", "")
    expected_code = level.get("expected_code", "")
    tags = level.get("tags", [])
    repo = level.get("source_repo", "")
    src_file = level.get("source_file", "")

    parts = [f"# 第{level_id}关: {title}"]

    if repo:
        parts.append(f"\n> 真实案例：{repo} 的 `{src_file}` 中使用了这个模式。")

    # Concept intro
    parts.append(f"\n## 概念介绍\n")
    parts.append(desc)

    # Key insights
    if hint:
        parts.append(f"\n## 关键点\n")
        parts.append(hint)

    # Common gotchas based on tags
    gotchas = {
        "try-except": "- `except:` 不加异常类型会捕获所有异常(包括 KeyboardInterrupt)，通常不推荐\n- `except Exception as e:` 中的 `as e` 可以获取异常对象\n- `finally` 无论是否发生异常都会执行",
        "type-hints": "- 类型标注只是提示，Python 运行时不做类型检查\n- `from typing import List, Dict, Optional` 在 Python 3.9+ 可用内置 `list`, `dict` 替代\n- 返回值类型用 `->` 箭头",
        "decorator": "- 装饰器本质是 `decorator(func)` 返回新函数\n- 内层 `wrapper` 用 `*args, **kwargs` 接收任意参数\n- `functools.wraps(func)` 保留原函数的 `__name__` 和 `__doc__`",
        "context-manager": "- `with` 语句块结束时自动调用 `__exit__`，即使发生异常\n- `__exit__` 返回 `True` 可以抑制异常（谨慎使用）\n- 也可以用 `contextlib.contextmanager` 装饰器 + `yield` 实现",
        "cli": "- `if __name__ == '__main__':` 保证脚本既能导入又能直接运行\n- Click 的 `@click.option('--name')` 自动生成 `--help` 文档\n- argparse 的 `add_argument` 支持 `type=int` 自动类型转换",
        "class": "- `__init__` 不是构造器，是初始化方法（构造器是 `__new__`）\n- 实例方法的第一个参数必须显式写 `self`\n- `pass` 是一个空语句，占位用",
        "exception": "- 自定义异常让调用方可以精确 `except` 特定错误\n- 异常类名通常以 `Error` 或 `Exception` 结尾\n- 继承 `Exception` 而非 `BaseException`（后者包括系统退出信号）",
    }
    for tag, gotcha_text in gotchas.items():
        if tag in tags:
            parts.append(f"\n## 常见陷阱\n")
            parts.append(gotcha_text)
            break

    # Task
    if task:
        parts.append(f"\n## 你的任务\n")
        parts.append(task)

    # Expected output hint
    if expected_code.strip():
        parts.append(f"\n请按照上方任务描述编写代码。")

    return "\n".join(parts) + "\n"


def write_level(level: dict, output_dir: Path, level_id: int) -> int:
    """Write level as python-mother directory (index.ts + answer.py + README.md)."""
    tags = level.get("tags", [])
    category = "中级"
    for tag in tags:
        if tag in TAG_CATEGORY:
            category = TAG_CATEGORY[tag]
            break

    difficulty = DIFF_MAP.get(level.get("difficulty", "intermediate"), 3)
    compare_mode = level.get("judge_mode", "return")

    title = level.get("title", f"Level {level_id}")
    desc = level.get("description", "")
    task = level.get("task", "")
    hint = level.get("hint", "")
    template = level.get("template", "")
    expected_code = level.get("expected_code", "")
    repo = level.get("source_repo", "")
    src_file = level.get("source_file", "")

    full_desc = desc
    if task:
        full_desc += f"\n\n{task}"
    if repo:
        full_desc += f"\n\n来源：{repo} — {src_file}"

    default_code = template if template else "# 请在此处编写代码\n"
    tags_str = json.dumps(tags, ensure_ascii=False)

    dirname = f"gen{level_id}"
    lvl_dir = output_dir / dirname
    lvl_dir.mkdir(parents=True, exist_ok=True)

    # Write README.md (teaching content)
    readme = _build_readme(level, level_id)
    (lvl_dir / "README.md").write_text(readme, encoding="utf-8")

    index_ts = f"""import answer from "./answer.py?raw";
import type {{ LevelType }} from "../level.d";

const level: LevelType = {{
  key: "{dirname}",
  title: "{_esc(title)}",
  category: "{category}",
  description: `{_esc(full_desc)}`,
  content: "",
  defaultCode: `{_esc(default_code)}`,
  answer,
  hint: `{_esc(hint)}`,
  type: "main",
  difficulty: {difficulty},
  compareMode: "{compare_mode}",
  tags: {tags_str},
}};

export default level;
"""
    (lvl_dir / "index.ts").write_text(index_ts, encoding="utf-8")
    (lvl_dir / "answer.py").write_text(expected_code or "# 请在此处编写代码\n", encoding="utf-8")

    return level_id + 1


# ── Main ─────────────────────────────────────────────────────────

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Generate Python-Mother levels from repos")
    parser.add_argument("--repo-dir", default=None, help="Path to code-blindspot repos")
    parser.add_argument("--output-dir", default=None, help="Output directory (default: python-mother src/levels)")
    parser.add_argument("--start-id", type=int, default=109)
    parser.add_argument("--limit-repos", type=int, default=0, help="Max repos to scan (0=all)")
    args = parser.parse_args()

    if not args.repo_dir:
        parser.error("--repo-dir is required (path to reference repo sources)")
    repo_dir = Path(args.repo_dir)
    output_dir = Path(args.output_dir) if args.output_dir else (Path(__file__).resolve().parent.parent / "src" / "levels")
    output_dir.mkdir(parents=True, exist_ok=True)

    repos = sorted(d for d in repo_dir.iterdir() if d.is_dir())
    if args.limit_repos:
        repos = repos[:args.limit_repos]

    import hashlib

    next_id = args.start_id
    total_levels = 0
    seen = set()  # deduplicate by (title, expected_code) hash

    for repo_path in repos:
        repo_name = repo_path.name.replace("_", "/", 1)  # fastapi_fastapi → fastapi/fastapi
        print(f"Scanning {repo_name}...")
        levels = scan_repo(repo_path, repo_name)
        generated = 0
        skipped = 0
        for level in levels:
            level.pop("_extractor", None)

            key = hashlib.md5(
                (level.get("title", "") + level.get("expected_code", "")).encode()
            ).hexdigest()
            if key in seen:
                skipped += 1
                continue
            seen.add(key)
            next_id = write_level(level, output_dir, next_id)
            total_levels += 1
            generated += 1
        if generated or skipped:
            print(f"  {generated} generated, {skipped} skipped")

    print(f"\nDone. {total_levels} levels written")
    print(f"Next available ID: {next_id}")


if __name__ == "__main__":
    main()
