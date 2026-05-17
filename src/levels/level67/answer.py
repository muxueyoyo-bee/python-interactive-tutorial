import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

X = np.array([[25, 50000], [30, 80000], [22, 30000], [35, 120000], [28, 65000]])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("鍘熷鏁版嵁(鍓?琛?:")
print(X[:2])
print("\n鏍囧噯鍖栧悗(鍓?琛?:")
print(np.round(X_scaled[:2], 2))
