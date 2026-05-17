from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle, io, base64

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X_train, y_train)

buf = io.BytesIO()
pickle.dump(model, buf)
buf.seek(0)
loaded = pickle.load(buf)
print(f"原始模型准确率: {model.score(X_test, y_test):.2%}")
print(f"持久化后加载准确率: {loaded.score(X_test, y_test):.2%}")
print(f"序列化大小: {len(buf.getvalue()) // 1024} KB")
