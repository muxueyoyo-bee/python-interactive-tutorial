# 第十六关: 列表推导式

列表推导式(List Comprehension)是 Python 的标志性特性 -- 用一行代码生成新列表.

## 基本语法

```python
[表达式 for 变量 in 可迭代对象 if 条件]
```

## 对比: 传统方式 vs 推导式

```python
# 传统方式
squares = []
for x in range(1, 11):
    squares.append(x**2)

# 列表推导式 -- 一行搞定
squares = [x**2 for x in range(1, 11)]
```

## 带条件过滤

```python
# 只保留偶数
evens = [x for x in range(1, 21) if x % 2 == 0]
```

## 你的任务

用列表推导式生成 1-10 的平方列表, 再用第二个推导式生成 1-20 内所有偶数. 分别打印.

预期输出:
```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```
