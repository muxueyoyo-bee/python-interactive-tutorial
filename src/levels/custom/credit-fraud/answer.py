import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
np.random.seed(42)

# 模拟: 500笔交易, 1%欺诈(严重不平衡!)
n = 500
X = np.random.randn(n, 10)
y = np.zeros(n, dtype=int)
fraud_idx = np.random.choice(n, 5, replace=False)  # 5笔欺诈
y[fraud_idx] = 1

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
model = RandomForestClassifier(n_estimators=200, class_weight="balanced", random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

from sklearn.metrics import recall_score
print(f"欺诈交易总数: {np.sum(y_test)}")
print(f"欺诈召回率(Recall): {recall_score(y_test, y_pred):.0%}")
