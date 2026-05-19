# 第235关: 编写装饰器: allow_rasterization

> 真实案例：matplotlib/matplotlib 的 `lib\matplotlib\artist.py` 中使用了这个模式。

## 概念介绍

装饰器是 Python 中用于包装函数、添加横切关注点的强大模式。

源文件 artist.py（matplotlib/matplotlib）中 `allow_rasterization` 展示了装饰器模式。

请编写一个装饰器，在函数调用前后各打印一行信息。

## 代码示例

```python
def allow_rasterization(func):
    def draw_wrapper(*args, **kwargs):
        print('before call')
        result = func(*args, **kwargs)
        print('after call')
        return result
    return draw_wrapper
```

## 关键点

外层函数接受 func 参数，内层定义 wrapper(*args, **kwargs)，外层 return wrapper

## 常见陷阱

- 装饰器本质是 `decorator(func)` 返回新函数
- 内层 `wrapper` 用 `*args, **kwargs` 接收任意参数
- `functools.wraps(func)` 保留原函数的 `__name__` 和 `__doc__`

## 你的任务

编写装饰器 allow_rasterization，包装目标函数并在调用前后打印 'before call' 和 'after call'。

预期行为：参考上方代码示例的输出。
