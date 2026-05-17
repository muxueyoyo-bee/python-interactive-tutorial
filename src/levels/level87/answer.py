import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

X = np.array([[25, 50000], [30, 80000], [22, 30000], [45, 200000], [28, 65000]])

for name, scaler in [("Standard", StandardScaler()), ("MinMax", MinMaxScaler()), ("Robust", RobustScaler())]:
    X_t = scaler.fit_transform(X)
    print(f"{name}: mean={X_t.mean(axis=0).round(2)}, std={X_t.std(axis=0).round(2)}")
