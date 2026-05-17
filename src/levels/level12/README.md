# 第十二关: for 循环

> 前置回顾: 第11关 if 是"选择性执行", for 是"重复执行"。第5关 列表。

## 循环是什么?

```python
# 不用循环 -- 重复写10次
print(1); print(2); print(3); ...

# 用循环 -- 3行搞定
for i in range(1, 11):
    print(i)
```

> 回顾第11关: if 让代码分支, for 让代码重复。

## range() 函数

```python
range(5)          # 0, 1, 2, 3, 4           (从0到n-1)
range(1, 6)       # 1, 2, 3, 4, 5           (从start到end-1)
range(1, 10, 2)   # 1, 3, 5, 7, 9           (步长=2)
range(10, 0, -1)  # 10,9,8,7,6,5,4,3,2,1   (倒数)
```

> range 不包含终点: `range(1,10)` 是 1 到 9。

## for 遍历各种类型

```python
# 遍历列表 (第5关)
for fruit in ["苹果", "香蕉", "橘子"]:
    print(fruit)

# 遍历字符串 (第4关)
for char in "Python":
    print(char)          # P y t h o n 每个字符一行

# 遍历字典 (第8关)
for k, v in {"name":"小明", "age":18}.items():
    print(f"{k}: {v}")
```

## 累加求和 -- 经典模式

```python
total = 0                  # 1. 初始化累加器
for i in range(1, 11):    # 2. 遍历
    total += i             # 3. 累加
print(total)               # 4. 输出: 55
```

> 这个模式很重要: 初始化 -> 遍历 -> 累加 -> 输出。以后反复出现。

## 常见错误

- 忘记冒号或缩进
- range 边界: `range(1,10)` 只有1到9, 不含10

## 你的任务

用 for 循环计算 1+2+...+10 的和并打印。

预期输出:
```
55
```
