from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split
import numpy as np

data = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, random_state=42)

rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# 鍐呯疆鐗瑰緛閲嶈鎬?
print("鍐呯疆閲嶈鎬op-3:", np.argsort(rf.feature_importances_)[-3:][::-1])

# Permutation閲嶈鎬?
perm = permutation_importance(rf, X_test, y_test, n_repeats=5, random_state=42)
print("Permutation閲嶈鎬op-3:", np.argsort(perm.importances_mean)[-3:][::-1])
