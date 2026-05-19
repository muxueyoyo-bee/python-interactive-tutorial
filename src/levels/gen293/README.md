# 第293关: 编写带类型标注的函数: get_relationship_to

> 真实案例：tiangolo/sqlmodel 的 `sqlmodel\_compat.py` 中使用了这个模式。

## 概念介绍

类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 _compat.py（tiangolo/sqlmodel）中 `get_relationship_to` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

## 代码示例

```python
def get_relationship_to(name: str, rel_info: 'RelationshipInfo', annotation: Any) -> Any:
    return f'get_relationship_to result'
```

## 关键点

def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型

## 常见陷阱

- 类型标注只是提示，Python 运行时不做类型检查
- `from typing import List, Dict, Optional` 在 Python 3.9+ 可用内置 `list`, `dict` 替代
- 返回值类型用 `->` 箭头

## 你的任务

编写函数 get_relationship_to(name: str, rel_info: 'RelationshipInfo', annotation: Any) -> Any，返回格式化字符串。

预期行为：参考上方代码示例的输出。
