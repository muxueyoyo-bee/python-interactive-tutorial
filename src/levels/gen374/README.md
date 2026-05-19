# 第374关: 编写带类型标注的函数: get_request_handler

> 真实案例：fastapi/fastapi 的 `fastapi\routing.py` 中使用了这个模式。

## 概念介绍

类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 routing.py（fastapi/fastapi）中 `get_request_handler` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

## 关键点

def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型

## 常见陷阱

- 类型标注只是提示，Python 运行时不做类型检查
- `from typing import List, Dict, Optional` 在 Python 3.9+ 可用内置 `list`, `dict` 替代
- 返回值类型用 `->` 箭头

## 你的任务

编写函数 get_request_handler(dependant: Dependant, body_field: ModelField | None, status_code: int | None, response_class: type[Response] | DefaultPlaceholder, response_field: ModelField | None, response_model_include: IncEx | None, response_model_exclude: IncEx | None, response_model_by_alias: bool, response_model_exclude_unset: bool, response_model_exclude_defaults: bool, response_model_exclude_none: bool, dependency_overrides_provider: Any | None, embed_body_fields: bool, strict_content_type: bool | DefaultPlaceholder, stream_item_field: ModelField | None, is_json_stream: bool) -> Callable[[Request], Coroutine[Any, Any, Response]]，返回格式化字符串。

请按照上方任务描述编写代码。
