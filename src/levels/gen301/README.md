# 第301关: 定义模块的公共 API

> 真实案例：psf/requests 的 `src\requests\__init__.py` 中使用了这个模式。

## 概念介绍

__all__ 是 Python 模块的公共接口声明，控制 `from module import *` 的行为。

源文件 __init__.py 暴露了 25 个公开符号。

请仿照此模式，为以下符号定义 __all__ 列表。

## 代码示例

```python
__all__ = [
    "ConnectionError",
    "ConnectTimeout",
    "HTTPError",
    "JSONDecodeError",
    "PreparedRequest",
    "ReadTimeout",
]
```

## 关键点

__all__ = ['Name1', 'Name2', ...] —— 字符串列表

## 你的任务

定义 __all__ 列表，包含以下 6 个公开符号: ConnectionError, ConnectTimeout, HTTPError, JSONDecodeError, PreparedRequest, ReadTimeout

预期行为：参考上方代码示例的输出。
