# 第395关: 编写带类型标注的函数: MergeMessageTo

> 真实案例：google/protobuf 的 `src\google\protobuf\util\python\field_mask_util.py` 中使用了这个模式。

## 概念介绍

类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 field_mask_util.py（google/protobuf）中 `MergeMessageTo` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

## 代码示例

```python
def MergeMessageTo(cls, source: _T, mask: field_mask_pb2.FieldMask, options: MergeOptions, destination: _T) -> _T:
    return f'MergeMessageTo result'
```

## 关键点

def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型

## 常见陷阱

- 类型标注只是提示，Python 运行时不做类型检查
- `from typing import List, Dict, Optional` 在 Python 3.9+ 可用内置 `list`, `dict` 替代
- 返回值类型用 `->` 箭头

## 你的任务

编写函数 MergeMessageTo(cls, source: _T, mask: field_mask_pb2.FieldMask, options: MergeOptions, destination: _T) -> _T，返回格式化字符串。

预期行为：参考上方代码示例的输出。
