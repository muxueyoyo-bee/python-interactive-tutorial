# 第三十四关: typing 类型注解

类型注解(Type Hints)标注函数参数和返回值的类型, 提高代码可读性.

## 基本语法

```python
from typing import List, Dict

def process(data: List[int]) -> Dict[str, int]:
    return {"sum": sum(data), "len": len(data), "max": max(data)}
```

## 常用类型

| 注解 | 含义 |
|------|------|
| int, float, str, bool | 基本类型 |
| List[int] | 整数列表 |
| Dict[str, int] | 字符串->整数字典 |

> 类型注解不影响运行, 但让 IDE 提供更好的提示.

## 你的任务

定义带类型注解的函数 process(data: List[int]) -> Dict[str, int], 返回 sum/len/max.

预期输出:
```
{'sum': 15, 'len': 5, 'max': 5}
```
