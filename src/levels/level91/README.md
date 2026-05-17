# 第九十一关: RAG -- 检索增强生成

> 前置回顾: 第56关 注意力机制, 第74关 文本分类(TF-IDF), 第65关 Transformer家族(GPT)

## RAG 是什么?

RAG = Retrieval Augmented Generation。大模型(LLM)的知识局限在训练数据中, RAG 通过**先检索再生成**的方式, 让模型能引用外部知识。

## 三步流程

```
1. 用户提问: "什么是AI?"
2. 检索: 从文档库中找相关文档 (TF-IDF/向量相似度)
3. 生成: 把检索到的文档+问题一起输入LLM, 生成答案
```

## 简易RAG模拟

本关实现最简版: 用 TF-IDF 做文档检索:

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 文档库
docs = ["Python是编程语言", "AI改变世界", ...]
query = "什么是AI"

# TF-IDF向量化
vec = TfidfVectorizer()
doc_vecs = vec.fit_transform(docs)
query_vec = vec.transform([query])

# 余弦相似度检索最相关文档
scores = cosine_similarity(query_vec, doc_vecs)[0]
```

> 实际RAG系统用的是 dense embedding(如 OpenAI text-embedding-3) 而不是 TF-IDF, 但原理相通。

## RAG vs 微调

| | RAG | 微调 |
|------|-----|------|
| 知识更新 | 换文档即可 | 需重新训练 |
| 幻觉控制 | 引用来源 | 无来源 |
| 成本 | 检索+推理 | 训练+推理 |
| 隐私 | 文档可本地 | 数据需上传 |

## 你的任务

对4个文档用TF-IDF检索与查询最相关的Top-2文档, 打印文档内容和相似度分数。

预期输出:
```
Query: 什么是AI
Top文档: ['AI改变世界', '机器学习需要数据']
相似度: [0.xxx 0.xxx]
```
