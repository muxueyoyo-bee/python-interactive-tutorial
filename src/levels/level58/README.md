# 第五十八关: 多头注意力 Multi-Head

单头可能只关注一种模式. 多头注意力并行运行多个注意力"头".

## 为什么多头?

类似多个专家从不同角度分析同一问题:
- 头1可能关注语法关系
- 头2可能关注语义相似
- 头3可能关注位置关系

## 实现

```python
def multi_head_attention(Q, K, V, n_heads=2):
    d_model = Q.shape[1]
    d_k = d_model // n_heads
    outputs = []
    for h in range(n_heads):
        # 每个头用不同的投影
        q_h = Q[:, h*d_k:(h+1)*d_k]
        k_h = K[:, h*d_k:(h+1)*d_k]
        v_h = V[:, h*d_k:(h+1)*d_k]
        # ... self-attention ...
    return concat(outputs)
```

## 你的任务

实现2头注意力, 输入4维, 每个头处理2维, 打印最终输出形状.

预期输出:
```
多头注意力输出形状: (4, 4)
```
