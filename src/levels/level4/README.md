## # 第四关: 字符串操作
字符串(str)是 Python 最常用的数据类型之一, 用于表示文本.

## 字符串方法

Python 为字符串提供了丰富的内置方法:

| 方法 | 作用 | 示例 |
|------|------|------|
| `upper()` | 转为全大写 | `"hello".upper()` -> `"HELLO"` |
| `lower()` | 转为全小写 | `"HELLO".lower()` -> `"hello"` |
| `len()` | 获取长度 | `len("Python")` -> `6` |
| `strip()` | 去除两端空格 | `" hi ".strip()` -> `"hi"` |
| `replace()` | 替换子串 | `"abc".replace("a","x")` -> `"xbc"` |

## 示例

```python
s = "Python"
print(s.upper())   # PYTHON
print(s.lower())   # python
print(len(s))      # 6
```

> 注意: 字符串方法不会修改原字符串(字符串是不可变的), 而是返回一个新字符串.

## 你的任务

创建字符串变量 `s = "Python"`, 分别调用 upper(), lower() 和 len() 方法, 打印结果.

预期输出:
```
PYTHON
python
6
```

