import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import classification_report

data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
scores = cross_val_score(model, X_train, y_train, cv=5)
model.fit(X_train, y_train)
print(f"浜ゅ弶楠岃瘉: {np.mean(scores):.2%} 卤 {np.std(scores):.2%}")
print(f"娴嬭瘯闆嗗噯纭巼: {model.score(X_test, y_test):.2%}")
print(f"鐗瑰緛閲嶈鎬?Top-3: {np.argsort(model.feature_importances_)[-3:][::-1]}")
