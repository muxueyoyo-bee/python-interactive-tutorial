# 第五十四关: 决策树 - 可解释的AI

决策树用树状结构做决策, 每次分裂追求最大信息增益.

## 熵 (Entropy)

衡量不确定性: H = -sum(p * log2(p))

## 信息增益

IG = H(parent) - weighted_average(H(children))

```python
import numpy as np
def entropy(labels):
    _, counts = np.unique(labels, return_counts=True)
    probs = counts / len(labels)
    return -np.sum(probs * np.log2(probs))
```

## 你的任务

计算给定标签的熵, 以及一次分裂后的信息增益.

预期输出:
```
初始熵: 1.000
信息增益: 1.000
```
