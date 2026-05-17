## # 第十五关: 函数的参数与返回值
return 语句让函数输出计算结果, 参数让函数接收输入数据.

## return 返回值

```python
def add(a, b):
    return a + b        # 把计算结果返回给调用者

result = add(3, 5)      # result 的值为 8
```

return 有两个作用:
1. 向调用者返回一个值
2. 终止函数执行(return 后面的代码不会运行)

## 多参数函数

```python
def multiply(a, b):
    return a * b

print(multiply(3, 5))    # 15
```

## 你的任务

定义两个函数: add(a, b) 返回两数之和, multiply(a, b) 返回两数之积. 分别用 3 和 5 调用并打印.

预期输出:
```
8
15
```

