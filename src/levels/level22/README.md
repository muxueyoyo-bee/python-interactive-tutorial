# 第二十二关: 异常处理

程序运行时遇到的错误叫异常(Exception). try/except 让你优雅地处理错误.

## 基本语法

```python
try:
    result = 10 / 0          # 可能出错的代码
except ZeroDivisionError:
    print("不能除以零!")      # 出错时的处理
finally:
    print("程序结束")         # 无论是否出错都会执行
```

## 常见异常类型

| 异常 | 触发条件 |
|------|---------|
| ZeroDivisionError | 除以零 |
| TypeError | 类型不匹配 |
| ValueError | 值不正确 |
| FileNotFoundError | 文件不存在 |
| KeyError | 字典键不存在 |

## 你的任务

在 try 块中尝试 10 / 0, 捕获 ZeroDivisionError 输出提示, finally 块打印"程序结束".

预期输出:
```
不能除以零!
程序结束
```
