# 第十八关: lambda 匿名函数

lambda 创建没有名字的函数, 适合简短的一次性操作.

## 基本语法

```python
lambda 参数: 表达式
```

## def vs lambda

```python
# def 写法
def add(a, b):
    return a + b

# lambda 写法 -- 一行搞定
add = lambda a, b: a + b

print(add(10, 20))   # 30
```

lambda 的精髓: 只能有一行表达式, 值自动返回, 不需要写 return. 常用于 map(), filter(), sorted() 等.

## 你的任务

用 lambda 创建两个匿名函数: 一个做加法, 一个做乘法. 用 10 和 20 调用, 打印结果.

预期输出:
```
30
200
```
