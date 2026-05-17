## # 第八关: 字典 - 键值对
字典(dict)是 Python 的核心数据结构, 用键-值对(key-value)存储数据.

## 为什么用字典?

列表用数字索引访问, 字典用有意义的键访问:

```python
# 用列表 -- 不直观
student_list = ["小明", 18, 95]  # 哪个是名字? 哪个是年龄?

# 用字典 -- 一目了然
student = {"name": "小明", "age": 18, "score": 95}
```

## 基本操作

```python
student = {"name": "小明", "age": 18, "score": 95}

print(student["name"])      # 小明
print(student.get("age"))   # 18
print(list(student.keys())) # ['name', 'age', 'score']
```

## 你的任务

创建一个学生字典, 包含 name, age, score 三个键. 用 [] 访问 name 和 age, 用 list() 转换输出所有键名.

预期输出:
```
小明
18
['name', 'age', 'score']
```

