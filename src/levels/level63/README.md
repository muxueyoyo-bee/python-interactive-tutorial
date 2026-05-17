# 第六十三关: 完整 Transformer - 组装

## 完整架构

```
输入 -> 位置编码 (+)
  Encoder(6层):
    Self-Attention -> Add&Norm ->
    FeedForward -> Add&Norm
  Decoder(6层):
    Masked Self-Attn -> Add&Norm ->
    Cross-Attention -> Add&Norm ->
    FeedForward -> Add&Norm
  Linear + Softmax -> 输出
```

## 核心创新

- **并行处理**: 不像RNN要逐词处理, Transformer一次性看整个序列
- **全局依赖**: 每个词都能直接关注到任何其他词
- **可扩展**: 堆叠更多层就能获得更强能力

## 你的任务

从架构层面理解完整 Transformer 的数据流, 打印架构概览.

预期输出: Transformer 架构ASCII总览
