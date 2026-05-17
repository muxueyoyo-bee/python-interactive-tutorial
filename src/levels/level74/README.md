# 第七十四关: 小型文本分类项目

用 CountVectorizer + 朴素贝叶斯完成文本情感分类.

## CountVectorizer

将文本转为词频向量: "I love Python" -> {love:1, python:1} 形式的向量.

## MultinomialNB (朴素贝叶斯)

基于贝叶斯定理, 假设特征之间条件独立. 文本分类的经典 baseline.

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

vec = CountVectorizer()
X = vec.fit_transform(texts)  # 文本 -> 词频矩阵
model = MultinomialNB()
model.fit(X, labels)
```

## 你的任务

用朴素贝叶斯训练一个简单的英文文本情感分类器.

预期输出: 训练集准确率 + 特征维度
