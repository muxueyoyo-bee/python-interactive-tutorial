# 第五十六关: 注意力机制 - AI的眼睛

注意力机制是 Transformer 的核心, 让模型在处理每个词时能"看到"整个序列.

## QKV 三剑客

- **Q (Query)**: "我在找什么?"
- **K (Key)**: "我这里有什么?"
- **V (Value)**: 实际的信息内容

## 注意力分数

scores = Q @ K^T / sqrt(d_k)

```python
import numpy as np
Q = np.random.randn(4, 3)  # 4个词, 每个3维
K = np.random.randn(4, 3)
d_k = 3
scores = Q @ K.T / np.sqrt(d_k)
print("分数矩阵形状:", scores.shape)
```

除以 sqrt(d_k) 是为了防止点积过大导致梯度消失.

## 你的任务

计算 Q@K^T/sqrt(d_k) 注意力分数矩阵, 打印形状和第一行分数.

预期输出: 分数矩阵形状和第一行的数值
