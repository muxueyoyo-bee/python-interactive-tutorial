# 第六十五关: Transformer 家族

## BERT (Bidirectional Encoder)

- 只看 Encoder, 双向注意力
- 预训练任务: 掩码语言模型(MLM)
- 适合: 文本分类, NER, 问答

## GPT (Generative Pre-trained)

- 只看 Decoder, 单向(因果)注意力
- 预训练任务: 下一个词预测
- 适合: 文本生成, 对话

## 其他变体

| 模型 | 架构 | 特点 |
|------|------|------|
| T5 | Encoder-Decoder | 全部任务统一为text-to-text |
| ViT | Encoder only | Transformer用于图像 |
| Whisper | Encoder-Decoder | 语音识别 |

## 你的任务

打印 BERT, GPT, T5, ViT, Whisper 的核心区别.

预期输出: Transformer 家族各成员的描述
