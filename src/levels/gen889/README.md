# 第889关: 编写带类型标注的函数: configure

> 真实案例：sqlalchemy/alembic 的 `alembic\runtime\environment.py` 中使用了这个模式。

## 概念介绍

类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 environment.py（sqlalchemy/alembic）中 `configure` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

## 代码示例

```python
def configure(self, connection: Optional[Connection], url: Optional[Union[str, URL]], dialect_name: Optional[str], dialect_opts: Optional[Dict[str, Any]], transactional_ddl: Optional[bool], transaction_per_migration: bool, output_buffer: Optional[TextIO], starting_rev: Optional[str], tag: Optional[str], template_args: Optional[Dict[str, Any]], render_as_batch: bool, target_metadata: Union[MetaData, Sequence[MetaData], None], include_name: Optional[IncludeNameFn], include_object: Optional[IncludeObjectFn], include_schemas: bool, process_revision_directives: Optional[ProcessRevisionDirectiveFn], compare_type: Union[bool, CompareType], compare_server_default: Union[bool, CompareServerDefault], render_item: Optional[RenderItemFn], literal_binds: bool, upgrade_token: str, downgrade_token: str, alembic_module_prefix: str, sqlalchemy_module_prefix: str, user_module_prefix: Optional[str], on_version_apply: Optional[OnVersionApplyFn], autogenerate_plugins: Sequence[str] | None) -> None:
    return f'configure result'
```

## 关键点

def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型

## 常见陷阱

- 类型标注只是提示，Python 运行时不做类型检查
- `from typing import List, Dict, Optional` 在 Python 3.9+ 可用内置 `list`, `dict` 替代
- 返回值类型用 `->` 箭头

## 你的任务

编写函数 configure(self, connection: Optional[Connection], url: Optional[Union[str, URL]], dialect_name: Optional[str], dialect_opts: Optional[Dict[str, Any]], transactional_ddl: Optional[bool], transaction_per_migration: bool, output_buffer: Optional[TextIO], starting_rev: Optional[str], tag: Optional[str], template_args: Optional[Dict[str, Any]], render_as_batch: bool, target_metadata: Union[MetaData, Sequence[MetaData], None], include_name: Optional[IncludeNameFn], include_object: Optional[IncludeObjectFn], include_schemas: bool, process_revision_directives: Optional[ProcessRevisionDirectiveFn], compare_type: Union[bool, CompareType], compare_server_default: Union[bool, CompareServerDefault], render_item: Optional[RenderItemFn], literal_binds: bool, upgrade_token: str, downgrade_token: str, alembic_module_prefix: str, sqlalchemy_module_prefix: str, user_module_prefix: Optional[str], on_version_apply: Optional[OnVersionApplyFn], autogenerate_plugins: Sequence[str] | None) -> None，返回格式化字符串。

预期行为：参考上方代码示例的输出。
