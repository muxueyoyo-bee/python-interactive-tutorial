# 第六十四关: 注意力可视化

将注意力权重矩阵画成热力图: 深色格子表示两个词之间有强关联.

```python
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

words = ["我", "爱", "Python", "编程"]
attn = np.random.rand(4, 4)
attn = attn / attn.sum(axis=1, keepdims=True)

plt.imshow(attn, cmap="Blues")
plt.xticks(range(4), words)
plt.yticks(range(4), words)
plt.title("Self-Attention 权重可视化")
plt.colorbar()
plt.show()
```

## 如何解读热力图?

- 第 i 行: 第 i 个词关注其他词的分布
- 对角线深: 词关注自己
- 非对角线深: 词之间有强关联

## 你的任务

生成一个4词句子的注意力权重矩阵并可视化.

预期输出: 一张注意力热力图
