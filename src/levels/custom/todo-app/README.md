# 工具实战: 待办事项管理器

> 涉及主线知识: 第26关 类与对象, 第5关 列表, 第8关 字典

## 场景

写一个命令行版的Todo应用。这是每个程序员在学习新语言时常做的练手项目 -- 麻雀虽小, 涵盖了数据结构设计的核心思路。

## 数据设计

```python
tasks = [
    {"task": "学习Python", "done": False},
    {"task": "写项目", "done": True},
]
```

每个任务是一个字典, 有任务描述和完成状态。用列表存所有任务。

> 回顾第8关: 字典用有意义的键("task"/"done"), 比用列表["学习Python", False]更清晰。

## 类设计

```python
class TodoList:
    def add(self, task):    # 添加任务
    def done(self, idx):    # 标记完成
    def show(self):         # 打印清单
```

show()输出格式: `[v] 0. 学习Python` 或 `[ ] 1. 运动` -- v表示已完成。

## 你的任务

实现 TodoList 类, 添加3个任务, 完成第1个, 打印全部任务的状态。
