# 第十五关: 函数的参数与返回值

> 前置回顾: 第14关 基本函数定义, 第2关 赋值和变量

## return 深度理解

return 做两件事:
1. 输出一个值给调用方
2. 立即结束函数 (后面的代码不执行)

```python
def check_age(age):
    if age < 0:
        return "无效"        # 到这里函数就结束了
    if age < 18:
        return "未成年"
    return "成年"            # 前面都没触发才到这里

print(check_age(-5))     # "无效"
print(check_age(15))     # "未成年"
print(check_age(25))     # "成年"
```

> 这种"多个 return 提前退出"叫 guard clause, 很常见。

## 多参数和多返回值

```python
# 默认参数
def power(base, exp=2):    # exp有默认值2
    return base ** exp

print(power(3))        # 9   (exp用默认值)
print(power(3, 3))     # 27  (exp=3)

# 多返回值 -- 本质是返回元组!
def divide(a, b):
    return a // b, a % b

q, r = divide(10, 3)   # 元组解包
print(q, r)             # 3 1
```

> 回顾第7关: 多个返回值是元组解包, 本质 `return (q, r)`。

## 参数类型

```python
# 位置参数: 按顺序传入
def describe(name, age):
    print(f"{name} is {age}")

describe("小明", 18)

# 关键字参数: 按名字传入
describe(age=18, name="小明")     # 可以不按顺序!

# 默认参数: 有默认值, 可以不传
def greet(name, greeting="你好"):
    print(f"{greeting}, {name}!")
```

## 综合示例: 计算器

```python
def calculator(a, b, op="add"):
    if op == "add":
        return a + b
    elif op == "multiply":
        return a * b

print(calculator(10, 5))              # 15 (默认add)
print(calculator(10, 5, "multiply"))  # 50
```

> 此例综合了: 第11关 if/elif, 第14关 函数定义, 第3关 数据类型。

## 你的任务

定义 add(a,b) 和 multiply(a,b), 分别用 3 和 5 调用并打印。

预期输出:
```
8
15
```
