# 第174关: 编写装饰器: to_raw_response_wrapper

> 真实案例：anthropics/anthropic-sdk-python 的 `src\anthropic\_legacy_response.py` 中使用了这个模式。

## 概念介绍

装饰器是 Python 中用于包装函数、添加横切关注点的强大模式。

源文件 _legacy_response.py（anthropics/anthropic-sdk-python）中 `to_raw_response_wrapper` 展示了装饰器模式。

请编写一个装饰器，在函数调用前后各打印一行信息。

## 关键点

外层函数接受 func 参数，内层定义 wrapper(*args, **kwargs)，外层 return wrapper

## 常见陷阱

- 装饰器本质是 `decorator(func)` 返回新函数
- 内层 `wrapper` 用 `*args, **kwargs` 接收任意参数
- `functools.wraps(func)` 保留原函数的 `__name__` 和 `__doc__`

## 你的任务

编写装饰器 to_raw_response_wrapper，包装目标函数并在调用前后打印 'before call' 和 'after call'。

请按照上方任务描述编写代码。
