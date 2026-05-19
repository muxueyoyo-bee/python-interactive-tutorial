# 第196关: 编写带类型标注的函数: jsonable_encoder

> 真实案例：fastapi/fastapi 的 `fastapi\encoders.py` 中使用了这个模式。

## 概念介绍

类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 encoders.py（fastapi/fastapi）中 `jsonable_encoder` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

## 代码示例

```python
def jsonable_encoder(obj: Annotated[Any, Doc('\n            The input object to convert to JSON.\n            ')], include: Annotated[IncEx | None, Doc("\n            Pydantic's `include` parameter, passed to Pydantic models to set the\n            fields to include.\n            ")], exclude: Annotated[IncEx | None, Doc("\n            Pydantic's `exclude` parameter, passed to Pydantic models to set the\n            fields to exclude.\n            ")], by_alias: Annotated[bool, Doc("\n            Pydantic's `by_alias` parameter, passed to Pydantic models to define if\n            the output should use the alias names (when provided) or the Python\n            attribute names. In an API, if you set an alias, it's probably because you\n            want to use it in the result, so you probably want to leave this set to\n            `True`.\n            ")], exclude_unset: Annotated[bool, Doc("\n            Pydantic's `exclude_unset` parameter, passed to Pydantic models to define\n            if it should exclude from the output the fields that were not explicitly\n            set (and that only had their default values).\n            ")], exclude_defaults: Annotated[bool, Doc("\n            Pydantic's `exclude_defaults` parameter, passed to Pydantic models to define\n            if it should exclude from the output the fields that had the same default\n            value, even when they were explicitly set.\n            ")], exclude_none: Annotated[bool, Doc("\n            Pydantic's `exclude_none` parameter, passed to Pydantic models to define\n            if it should exclude from the output any fields that have a `None` value.\n            ")], custom_encoder: Annotated[dict[Any, Callable[[Any], Any]] | None, Doc("\n            Pydantic's `custom_encoder` parameter, passed to Pydantic models to define\n            a custom encoder.\n            ")], sqlalchemy_safe: Annotated[bool, Doc("\n            Exclude from the output any fields that start with the name `_sa`.\n\n            This is mainly a hack for compatibility with SQLAlchemy objects, they\n            store internal SQLAlchemy-specific state in attributes named with `_sa`,\n            and those objects can't (and shouldn't be) serialized to JSON.\n            ")]) -> Any:
    return f'jsonable_encoder result'
```

## 关键点

def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型

## 常见陷阱

- 类型标注只是提示，Python 运行时不做类型检查
- `from typing import List, Dict, Optional` 在 Python 3.9+ 可用内置 `list`, `dict` 替代
- 返回值类型用 `->` 箭头

## 你的任务

编写函数 jsonable_encoder(obj: Annotated[Any, Doc('\n            The input object to convert to JSON.\n            ')], include: Annotated[IncEx | None, Doc("\n            Pydantic's `include` parameter, passed to Pydantic models to set the\n            fields to include.\n            ")], exclude: Annotated[IncEx | None, Doc("\n            Pydantic's `exclude` parameter, passed to Pydantic models to set the\n            fields to exclude.\n            ")], by_alias: Annotated[bool, Doc("\n            Pydantic's `by_alias` parameter, passed to Pydantic models to define if\n            the output should use the alias names (when provided) or the Python\n            attribute names. In an API, if you set an alias, it's probably because you\n            want to use it in the result, so you probably want to leave this set to\n            `True`.\n            ")], exclude_unset: Annotated[bool, Doc("\n            Pydantic's `exclude_unset` parameter, passed to Pydantic models to define\n            if it should exclude from the output the fields that were not explicitly\n            set (and that only had their default values).\n            ")], exclude_defaults: Annotated[bool, Doc("\n            Pydantic's `exclude_defaults` parameter, passed to Pydantic models to define\n            if it should exclude from the output the fields that had the same default\n            value, even when they were explicitly set.\n            ")], exclude_none: Annotated[bool, Doc("\n            Pydantic's `exclude_none` parameter, passed to Pydantic models to define\n            if it should exclude from the output any fields that have a `None` value.\n            ")], custom_encoder: Annotated[dict[Any, Callable[[Any], Any]] | None, Doc("\n            Pydantic's `custom_encoder` parameter, passed to Pydantic models to define\n            a custom encoder.\n            ")], sqlalchemy_safe: Annotated[bool, Doc("\n            Exclude from the output any fields that start with the name `_sa`.\n\n            This is mainly a hack for compatibility with SQLAlchemy objects, they\n            store internal SQLAlchemy-specific state in attributes named with `_sa`,\n            and those objects can't (and shouldn't be) serialized to JSON.\n            ")]) -> Any，返回格式化字符串。

预期行为：参考上方代码示例的输出。
