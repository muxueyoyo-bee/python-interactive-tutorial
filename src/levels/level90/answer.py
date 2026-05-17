from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_absolute_error, r2_score
import numpy as np

data = fetch_california_housing()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = GradientBoostingRegressor(n_estimators=200, max_depth=4, learning_rate=0.1, random_state=42)
scores = cross_val_score(model, X_train, y_train, cv=5, scoring="r2")
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f"CV R2: {np.mean(scores):.3f} +/- {np.std(scores):.3f}")
print(f"Test MAE: {mean_absolute_error(y_test, y_pred):.3f}")
print(f"Test R2: {r2_score(y_test, y_pred):.3f}")
