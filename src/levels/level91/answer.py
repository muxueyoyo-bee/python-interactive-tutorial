import numpy as np

# 绠€鏄揜AG妯℃嫙: 鏂囨。妫€绱?+ 鐢熸垚
# 鍚戦噺妫€绱㈤儴鍒?
np.random.seed(42)
docs = ["Python鏄紪绋嬭瑷€", "AI鏀瑰彉涓栫晫", "鏈哄櫒瀛︿範闇€瑕佹暟鎹?, "娣卞害瀛︿範鏄疢L瀛愰泦"]
query = "浠€涔堟槸AI"

# 绠€鍗昑F-IDF鐩镐技搴?
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vec = TfidfVectorizer()
doc_vecs = vec.fit_transform(docs)
query_vec = vec.transform([query])
scores = cosine_similarity(query_vec, doc_vecs)[0]
top_idx = np.argsort(scores)[-2:][::-1]
print(f"Query: {query}")
print(f"Top鏂囨。: {[docs[i] for i in top_idx]}")
print(f"鐩镐技搴? {scores[top_idx].round(3)}")
