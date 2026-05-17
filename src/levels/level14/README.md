# 第十四关: 自定义函数

> 前置回顾: 你一直在用内置函数 -- print(), len(), type()。现在自己写函数!

## 为什么需要函数?

看这段重复代码:
```python
# 三个学生的平均分 -- 同样逻辑写了三次!
avg1 = (85 + 90 + 78) / 3
avg2 = (92 + 88 + 95) / 3
avg3 = (76 + 82 + 80) / 3
```

用函数消除重复:
```python
def avg(a, b, c):
    return (a + b + c) / 3

print(avg(85, 90, 78))   # 一行调用, 不再重复
print(avg(92, 88, 95))
```

> 回顾第2关: 变量是把值存起来复用。函数是把逻辑存起来复用!

## 定义和调用

```python
def 函数名(参数1, 参数2):    # 定义
    函数体
    return 返回值

result = 函数名(值1, 值2)     # 调用
```

## 完整示例

```python
def greet(name):
    """向指定的人问好"""       # 文档字符串
    return f"你好, {name}!"

print(greet("小明"))          # 你好, 小明!
print(greet("小红"))          # 你好, 小红!
```

## 参数和返回值

- 参数: 函数需要的输入, 写在 `()` 里
- return: 函数的输出, 调用处收到这个值
- 没有 return: 函数返回 None

```python
def add(a, b):
    return a + b      # 有返回值

def say_hi():
    print("Hi!")       # 无返回值, 返回 None
```

## 命名规范

- 小写+下划线: `calculate_total`, `get_user`
- 动词开头: get, set, calc, find, create
- 见名知意: `avg` 比 `f` 好

## 常见错误

- 忘了调用: `greet` 是函数本身, `greet("小明")` 才是调用
- 忘了 return: 函数返回 None
- 参数数量不对: 调用时参数个数必须匹配

## 你的任务

定义 `greet(name)` 函数, 返回 "你好, {name}!"。用 "小明" 和 "小红" 调用。

预期输出:
```
你好, 小明!
你好, 小红!
```
