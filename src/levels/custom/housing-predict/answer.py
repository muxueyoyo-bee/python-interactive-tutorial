from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

data = fetch_california_housing()
X_train, X_test, y_train, y_test = train_test_split(data.data[:2000], data.target[:2000], test_size=0.2, random_state=42)

model = GradientBoostingRegressor(n_estimators=150, max_depth=4, learning_rate=0.1, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(f"鎴夸环棰勬祴 R2: {r2_score(y_test, y_pred):.3f}")
print(f"鐗瑰緛閲嶈鎬op-3: {data.feature_names[model.feature_importances_.argsort()[-3:][::-1]].tolist()}")
