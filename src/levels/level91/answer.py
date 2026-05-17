import numpy as np

# 简易RAG模拟: 文档检索 + 生成
# 向量检索部分
np.random.seed(42)
docs = ["Python是编程语言", "AI改变世界", "机器学习需要数据", "深度学习是ML子集"]
query = "什么是AI"

# 简单TF-IDF相似度
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vec = TfidfVectorizer()
doc_vecs = vec.fit_transform(docs)
query_vec = vec.transform([query])
scores = cosine_similarity(query_vec, doc_vecs)[0]
top_idx = np.argsort(scores)[-2:][::-1]
print(f"Query: {query}")
print(f"Top文档: {[docs[i] for i in top_idx]}")
print(f"相似度: {scores[top_idx].round(3)}")
