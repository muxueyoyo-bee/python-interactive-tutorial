# 第二十八关: 装饰器

装饰器(Decorator)是一种不修改原函数代码就能增强其功能的技术, 用 @ 语法.

## 示例

```python
def uppercase(func):            # 装饰器函数
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase                      # 使用装饰器
def greet(name):
    return f"hello, {name}"

print(greet("world"))           # HELLO, WORLD
```

*args 接收任意数量的位置参数, **kwargs 接收任意关键字参数.

## 你的任务

定义 uppercase 装饰器把返回值转为大写. 用 @uppercase 装饰 greet() 函数.

预期输出:
```
HELLO, WORLD
```
