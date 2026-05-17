# 第三关：数据类型

Python 中不同的数据有不同的**类型**。让我们来认识四种最基础的类型。

## 四种基本数据类型

| 类型 | 关键字 | 示例 | 说明 |
|------|--------|------|------|
| 整数 | `int` | `42` | 没有小数点的数字 |
| 浮点数 | `float` | `3.14` | 带小数点的数字 |
| 字符串 | `str` | `"Python"` | 文本，用引号包裹 |
| 布尔值 | `bool` | `True` / `False` | 只有两个值 |

## type() 函数

使用 `type()` 函数可以查看任何变量或值的类型：

```python
print(type(42))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type("hello"))  # <class 'str'>
print(type(True))     # <class 'bool'>
```

## 🎯 你的任务

有四行代码已经帮你写好了变量定义。请使用 `print(type(变量名))` 分别输出四个变量的类型。

期望输出（顺序必须一致）：
```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```
