# 第六十二关: Transformer Decoder 层

Decoder 比 Encoder 多一层 Cross-Attention.

## Decoder 结构

x -> Masked Self-Attention -> Add & Norm -> Cross-Attention -> Add & Norm -> FFN -> Add & Norm

## Cross-Attention

Decoder的Q去查询Encoder输出的K和V.

```python
def cross_attention(Q_dec, K_enc, V_enc, d_k):
    scores = Q_dec @ K_enc.T / np.sqrt(d_k)
    return softmax(scores) @ V_enc
```

## Masked Self-Attention

生成时只能看到当前位置和之前的位置, 不能偷看未来.

## 你的任务

实现 Cross-Attention, Decoder(3个词)查询 Encoder输出(5个词).

预期输出:
```
Cross-Attention 输出形状: (3, 4)
Decoder 关注 Encoder 的输出
```
