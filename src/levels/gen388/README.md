# 第388关: 编写带类型标注的函数: create_proxy_methods

> 真实案例：sqlalchemy/sqlalchemy 的 `tools\generate_proxy_methods.py` 中使用了这个模式。

## 概念介绍

类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 generate_proxy_methods.py（sqlalchemy/sqlalchemy）中 `create_proxy_methods` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

## 代码示例

```python
def create_proxy_methods(target_cls: Type[Any], target_cls_sphinx_name: str, proxy_cls_sphinx_name: str, classmethods: Iterable[str], methods: Iterable[str], attributes: Iterable[str], use_intermediate_variable: Iterable[str]) -> Callable[[Type[_T]], Type[_T]]:
    return f'create_proxy_methods result'
```

## 关键点

def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型

## 常见陷阱

- 类型标注只是提示，Python 运行时不做类型检查
- `from typing import List, Dict, Optional` 在 Python 3.9+ 可用内置 `list`, `dict` 替代
- 返回值类型用 `->` 箭头

## 你的任务

编写函数 create_proxy_methods(target_cls: Type[Any], target_cls_sphinx_name: str, proxy_cls_sphinx_name: str, classmethods: Iterable[str], methods: Iterable[str], attributes: Iterable[str], use_intermediate_variable: Iterable[str]) -> Callable[[Type[_T]], Type[_T]]，返回格式化字符串。

预期行为：参考上方代码示例的输出。
