import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
np.random.seed(42)

# 妯℃嫙: 500绗斾氦鏄? 1%娆鸿瘓(涓ラ噸涓嶅钩琛?)
n = 500
X = np.random.randn(n, 10)
y = np.zeros(n, dtype=int)
fraud_idx = np.random.choice(n, 5, replace=False)  # 5绗旀璇?
y[fraud_idx] = 1

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
model = RandomForestClassifier(n_estimators=200, class_weight="balanced", random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

from sklearn.metrics import recall_score
print(f"娆鸿瘓浜ゆ槗鎬绘暟: {np.sum(y_test)}")
print(f"娆鸿瘓鍙洖鐜?Recall): {recall_score(y_test, y_pred):.0%}")
