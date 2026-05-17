# NLP实战: 文本词频统计

> 涉及主线知识: 第33关 collections.Counter, 第24关 正则, 第4关 字符串

## 场景

你是一家媒体公司的数据分析师。需要从英文文章中提取最常见的词, 了解文章主题。词频统计是NLP最基础的操作。

## Counter: 一行统计

```python
from collections import Counter
words = ["a", "b", "c", "a", "b", "a"]
Counter(words)                    # Counter({'a':3, 'b':2, 'c':1})
Counter(words).most_common(2)     # [('a',3), ('b',2)]
```

> 回顾第33关: Counter 自动统计每个元素出现次数, most_common(n) 直接取Top-n。

## 文本预处理

```python
import re
text = "Python is great. Python is fun."
words = re.findall(r'\w+', text.lower())  # ['python','is','great','python','is','fun']
```

- text.lower(): 转小写, 避免"Python"和"python"被当成两个词
- re.findall(r'\w+', text): 提取所有"单词"(字母数字序列), 去掉标点

## 你的任务

对英文短文提取所有单词, 用 Counter 统计并打印出现最多的前3个词。
