# 第六十关: 前馈网络与 LayerNorm

每个 Transformer 层包含两个子层: Self-Attention 和 FeedForward.

## FeedForward Network

FFN(x) = ReLU(xW1 + b1)W2 + b2

两层全连接, 中间用 ReLU 激活. 增强非线性表达能力.

## Layer Normalization

LayerNorm(x) = (x - mean) / sqrt(var + eps)

将每层输出的均值归0, 方差归1. 稳定训练, 加速收敛.

## 残差连接

x = LayerNorm(x + SubLayer(x))

让梯度直接流过, 解决深层网络的训练困难.

## 你的任务

实现 FeedForward 和 LayerNorm, 打印输出形状和 LayerNorm 后均值是否接近0.

预期输出: 形状信息 + 均值验证
