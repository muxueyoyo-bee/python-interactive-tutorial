# 第二十七关: 类的继承

继承让你在现有类的基础上创建新类, 复用代码.

## 基本语法

```python
class Animal:                   # 父类
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."

class Cat(Animal):              # 子类
    def speak(self):            # 重写父类方法
        return f"{self.name} says Meow!"
```

## 关键概念

- 继承: class Cat(Animal) 表示 Cat 继承 Animal
- 重写: 子类定义和父类同名的方法, 覆盖父类行为

## 你的任务

创建 Animal 父类和 Cat 子类, Cat 重写 speak(). 创建 Cat("小花") 并调用 speak().

预期输出:
```
小花 says Meow!
```
