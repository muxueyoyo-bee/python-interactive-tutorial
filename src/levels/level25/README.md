# 第二十五关: 模块与导入

Python 的强大来自于丰富的标准库和第三方模块. import 语句让你使用这些模块.

## 导入方式

```python
import math
print(round(math.pi, 2))  # 3.14

import random
random.seed(42)            # 固定随机种子
print(random.randint(1, 100))
```

## 常用标准库

| 模块 | 用途 |
|------|------|
| math | 数学函数和常量 |
| random | 随机数生成 |
| datetime | 日期时间处理 |
| json | JSON 数据处理 |
| re | 正则表达式 |

## 你的任务

导入 math 和 random. 设置随机种子为 42, 输出 pi 保留两位小数, 再输出一个 1-100 的随机整数.

预期输出:
```
3.14
82
```
