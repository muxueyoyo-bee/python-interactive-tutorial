# 第六十一关: Transformer Encoder 层

完整的 Encoder 层组装.

## 结构

x -> Self-Attention -> Add & LayerNorm -> FeedForward -> Add & LayerNorm

```python
def encoder_layer(x):
    # 1. Self-Attention + Residual + LayerNorm
    attn_out = self_attention(x, x, x)
    x = layer_norm(x + attn_out)
    # 2. FeedForward + Residual + LayerNorm
    ff_out = feed_forward(x)
    x = layer_norm(x + ff_out)
    return x
```

## 为什么残差连接?

没有残差: 深层网络梯度消失, 无法训练
有残差: 梯度可以直接流过, 堆叠任意层数

## 你的任务

组装并运行一个完整的 Encoder 层.

预期输出:
```
Encoder 输出形状: (3, 4)
```
