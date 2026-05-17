# 第二十六关: 面向对象: 类与对象

面向对象编程(OOP)用类(class)和对象(object)来组织代码. 类是蓝图, 对象是按蓝图创建的实例.

## 定义类

```python
class Dog:
    def __init__(self, name, age):   # 构造函数
        self.name = name
        self.age = age

    def bark(self):                   # 方法
        return f"{self.name} says Woof!"
```

## 创建和使用对象

```python
dog = Dog("小白", 3)
print(dog.name)             # 访问属性
print(dog.age)
print(dog.bark())           # 调用方法
```

> self 代表实例自身, 是类中每个方法的第一个参数.

## 你的任务

定义 Dog 类, 有 name/age 属性和 bark() 方法. 创建实例并打印属性和方法返回值.

预期输出:
```
小白
3
小白 says Woof!
```
