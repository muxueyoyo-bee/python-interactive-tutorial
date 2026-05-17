import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

texts = ["I love Python", "Python is great", "I hate bugs", "Debugging sucks", "ML is amazing", "Bad code", "Awesome AI", "Terrible error"]
labels = [1, 1, 0, 0, 1, 0, 1, 0]

X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.25, random_state=42)
vec = CountVectorizer()
X_train_vec = vec.fit_transform(X_train)
model = MultinomialNB()
model.fit(X_train_vec, y_train)
print(f"璁粌闆嗗噯纭巼: {model.score(X_train_vec, y_train):.0%}")
print(f"鐗瑰緛缁村害: {X_train_vec.shape[1]}")
