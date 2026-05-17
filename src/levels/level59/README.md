# 第五十九关: 位置编码

Transformer 没有循环结构, 天生不知道词的顺序. 位置编码注入位置信息.

## 正弦位置编码

PE(pos, 2i) = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))

## 为什么用正弦/余弦?

- 值域稳定在 [-1, 1]
- 相对位置可通过线性变换表示
- 可外推到训练时没见过的序列长度

```python
def positional_encoding(seq_len, d_model):
    pe = np.zeros((seq_len, d_model))
    for pos in range(seq_len):
        for i in range(0, d_model, 2):
            pe[pos, i] = np.sin(pos / (10000 ** (i/d_model)))
            pe[pos, i+1] = np.cos(pos / (10000 ** (i/d_model)))
    return pe
```

## 你的任务

生成序列长度5, 维度8的位置编码, 打印形状和第一个位置的前4维.

预期输出: 形状和位置编码数值
