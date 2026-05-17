# 第五关: 列表 -- 有序的集合

> 前置回顾: 第2关 变量只能存一个值, 第4关 字符串是一串字符

## 为什么需要列表?

之前学的变量每次只能存一个值:
```python
fruit1 = "苹果"
fruit2 = "香蕉"
fruit3 = "橘子"    # 三个变量, 很麻烦!
```

用列表可以一个变量存多个值:
```python
fruits = ["苹果", "香蕉", "橘子"]   # 一个变量, 三个值!
```

## 创建列表

```python
empty = []                        # 空列表
nums = [1, 2, 3, 4, 5]          # 数字列表
mixed = [1, "hello", 3.14]      # 混合列表(Python允许但不推荐)
```

## 索引访问

列表每个元素有索引, 从 0 开始:

```python
fruits = ["苹果", "香蕉", "橘子", "葡萄"]

print(fruits[0])    # "苹果" -- 第一个
print(fruits[1])    # "香蕉" -- 第二个
print(fruits[-1])   # "葡萄" -- 最后一个, 负数倒着数
print(fruits[-2])   # "橘子" -- 倒数第二个
```

> 索引从 0 开始是几乎所有编程语言的惯例。

## 基本操作

```python
fruits = ["苹果", "香蕉"]

print(len(fruits))                # 2
print("苹果" in fruits)           # True
print("西瓜" in fruits)           # False
```

> 回顾: len() 对字符串和列表都用, 第4关学过 `len("Python")` -> 6。

## 常见错误

- 索引越界: 列表只有4个元素, `fruits[10]` 报 IndexError
- `fruits.len()` 是错的, 正确是 `len(fruits)`

## 你的任务

创建包含四种水果的列表, 输出第一个、最后一个元素、列表长度。

预期输出:
```
苹果
葡萄
4
```
