# 第八关: 字典 -- 键值对

> 前置回顾: 第5关 列表用数字索引, 第2关 变量给数据起名字

## 从列表到字典

列表的局限: 只能用数字索引, 没有语义:
```python
student = ["小明", 18, 95]
# student[0] 是名字? student[1] 是年龄? 容易忘
```

字典的优雅: 用有意义的键来索引:
```python
student = {"name": "小明", "age": 18, "score": 95}
print(student["name"])    # "小明" -- 一看就懂!
```

> 回顾第2关: 变量也是"给值起名字"。字典是"给一堆相关的值起名字"。

## 字典的结构

```python
{ "键1": "值1", "键2": "值2", "键3": "值3" }
```

- 键(key): 不可变类型(字符串/数字/元组)
- 值(value): 任意类型
- 键必须唯一, 值可以重复

## 基本操作

```python
student = {"name": "小明", "age": 18, "score": 95}

# 访问 -- 两种方式
print(student["name"])           # "小明" (键不存在报错)
print(student.get("gender"))     # None (更安全, 键不存在返回None)

# 所有键
print(list(student.keys()))      # ['name', 'age', 'score']

# 所有值
print(list(student.values()))    # ['小明', 18, 95]
```

## 什么时候用字典 vs 列表?

- 数据有关联标签 -> 字典
- 数据只是顺序排列 -> 列表

## 常见错误

- 键不存在: `student["gender"]` 报 KeyError, 用 `.get()` 更安全

## 你的任务

创建学生字典, 用 [] 访问 name 和 age, 用 list(keys()) 输出所有键名。

预期输出:
```
小明
18
['name', 'age', 'score']
```
