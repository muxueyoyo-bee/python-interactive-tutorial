# 第525关: 编写上下文管理器: AppContext

> 真实案例：pallets/flask 的 `src\flask\ctx.py` 中使用了这个模式。

## 概念介绍

上下文管理器（Context Manager）用 with 语句管理资源的获取和释放。

源文件 ctx.py 定义了类 `AppContext`，实现了 __enter__ / __exit__。

请仿照此模式编写一个上下文管理器，在进入和退出时打印信息。

## 代码示例

```python
class AppContext:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f'Entering {self.name}')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Exiting {self.name}')
        return False
```

## 关键点

实现 __enter__(self) 返回 self，__exit__(self, exc_type, exc_val, exc_tb) 处理清理

## 常见陷阱

- `with` 语句块结束时自动调用 `__exit__`，即使发生异常
- `__exit__` 返回 `True` 可以抑制异常（谨慎使用）
- 也可以用 `contextlib.contextmanager` 装饰器 + `yield` 实现

## 你的任务

编写类 AppContext，实现 __enter__ 和 __exit__，进入时打印 'Entering {name}'，退出时打印 'Exiting {name}'。

预期行为：参考上方代码示例的输出。
