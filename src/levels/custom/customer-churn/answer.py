import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
np.random.seed(42)
n = 200
X = np.random.randn(n, 5)  # 5个特征: 使用频率/消费金额/投诉次数/会员月数/最近登录
X[:, 2] = np.abs(X[:, 2]) * 3  # 投诉次数偏态
y = (X[:, 0]*2 + X[:, 1]*1.5 - X[:, 2]*3 + X[:, 3]*0.5 + np.random.randn(n)*2 > 0).astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X_train, y_train)
print(f"客户流失预测准确率: {model.score(X_test, y_test):.1%}")
print(f"Top-2特征重要性: {np.argsort(model.feature_importances_)[-2:][::-1]}")
