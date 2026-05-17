# 第五十七关: Self-Attention 的数学

Self-Attention: 输入序列中的每个位置都和其他所有位置计算注意力.

## 完整公式

Attention(Q,K,V) = softmax(QK^T / sqrt(d_k)) @ V

```python
import numpy as np
def softmax(x):
    e = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return e / np.sum(e, axis=-1, keepdims=True)

scores = Q @ K.T / np.sqrt(d_k)
attn = softmax(scores)       # 注意力权重
output = attn @ V             # 加权求和
```

## 为什么 softmax?

- 把分数转为概率分布(每行和为1)
- 放大差异: 重要的更大, 不重要的更小

## 你的任务

实现完整的 Self-Attention 计算, 验证注意力权重每行和为1.

预期输出:
```
注意力权重和为 1: True
输出形状: (4, 3)
```
