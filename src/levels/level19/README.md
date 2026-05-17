# 第十九关: map 与 filter

map() 和 filter() 是 Python 的高阶函数 -- 接收一个函数和一个可迭代对象, 批量处理数据.

## map() -- 对每个元素应用函数

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared = list(map(lambda x: x**2, nums))
print(squared)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## filter() -- 筛选满足条件的元素

```python
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  # [2, 4, 6, 8, 10]
```

> 注意: map() 和 filter() 返回的是迭代器, 需要用 list() 转换.

## 你的任务

对列表 [1..10]: 用 map 求每个元素的平方, 用 filter 筛选偶数. 分别打印.

预期输出:
```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[2, 4, 6, 8, 10]
```
