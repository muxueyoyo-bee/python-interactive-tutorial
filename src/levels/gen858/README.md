# 第858关: 编写带类型标注的函数: handle_exception

> 真实案例：sphinx-doc/sphinx 的 `sphinx\cmd\build.py` 中使用了这个模式。

## 概念介绍

类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 build.py（sphinx-doc/sphinx）中 `handle_exception` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

## 关键点

def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型

## 常见陷阱

- 类型标注只是提示，Python 运行时不做类型检查
- `from typing import List, Dict, Optional` 在 Python 3.9+ 可用内置 `list`, `dict` 替代
- 返回值类型用 `->` 箭头

## 你的任务

编写函数 handle_exception(app: Sphinx | None, args: Any, exception: BaseException, stderr: TextIO) -> None，返回格式化字符串。

请按照上方任务描述编写代码。
