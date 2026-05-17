import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
np.random.seed(42)
n = 200
X = np.random.randn(n, 5)  # 5涓壒寰? 浣跨敤棰戠巼/娑堣垂閲戦/鎶曡瘔娆℃暟/浼氬憳鏈堟暟/鏈€杩戠櫥褰?
X[:, 2] = np.abs(X[:, 2]) * 3  # 鎶曡瘔娆℃暟鍋忔€?
y = (X[:, 0]*2 + X[:, 1]*1.5 - X[:, 2]*3 + X[:, 3]*0.5 + np.random.randn(n)*2 > 0).astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X_train, y_train)
print(f"瀹㈡埛娴佸け棰勬祴鍑嗙‘鐜? {model.score(X_test, y_test):.1%}")
print(f"Top-2鐗瑰緛閲嶈鎬? {np.argsort(model.feature_importances_)[-2:][::-1]}")
