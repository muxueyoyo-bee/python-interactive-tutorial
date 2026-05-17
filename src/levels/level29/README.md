# 第二十九关: 生成器

生成器(Generator)用 yield 关键字逐个产出值, 而非一次性生成全部 -- 节省内存.

## yield vs return

```python
# 普通函数: 一次性返回整个列表
def squares_list(n):
    return [x**2 for x in range(n)]

# 生成器: 逐个产出
def squares_gen(n):
    for i in range(n):
        yield i**2
```

## 斐波那契

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(10)))  # [0,1,1,2,3,5,8,13,21,34]
```

## 你的任务

用生成器实现斐波那契数列的前 10 个数, 转为列表打印.

预期输出:
```
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```
