# 第四关: 字符串操作

> 前置回顾: 第1关 print(), 第2关 变量赋值

## 什么是字符串?

字符串(str)是一切文本的基础。你之前写的 `"Hello, World!"` 就是一个字符串。Python 中所有用引号包裹的内容都是字符串:

```python
"Hello"        # 双引号
'World'        # 单引号(效果相同)
"123"          # 注意: 这是字符串 "123", 不是数字 123
```

## 字符串方法一览

| 方法 | 作用 | 示例 | 结果 |
|------|------|------|------|
| `upper()` | 全转大写 | `"hello".upper()` | `"HELLO"` |
| `lower()` | 全转小写 | `"HELLO".lower()` | `"hello"` |
| `len(s)` | 获取长度 | `len("Python")` | `6` |
| `strip()` | 去两端空格 | `" hi ".strip()` | `"hi"` |
| `replace(a,b)` | 替换子串 | `"abc".replace("a","x")` | `"xbc"` |
| `split()` | 按分隔符切割 | `"a,b,c".split(",")` | `["a","b","c"]` |
| `join()` | 用分隔符拼接 | `"-".join(["a","b"])` | `"a-b"` |

## 字符串不可变

```python
s = "hello"
s.upper()       # 返回 "HELLO", 但...
print(s)        # 仍然是 "hello"! 原字符串没有变

# 如果要保留结果, 必须重新赋值:
s = s.upper()   # 现在 s 才变成了 "HELLO"
```

> 回顾: 这和变量的赋值逻辑一样 -- 第2关学过 `=` 是把右边的值赋给左边。

## 常见错误

- 忘了重新赋值: 写了 `s.upper()` 但没写 `s = s.upper()`
- len 不是方法: 正确是 `len(s)`, 不是 `s.len()`

## 你的任务

创建 `s = "Python"`, 分别调用 upper(), lower() 和 len(), 打印结果。

预期输出:
```
PYTHON
python
6
```
