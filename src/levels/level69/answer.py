from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import cross_val_score
import numpy as np

X, y = make_regression(n_samples=200, n_features=5, noise=10, random_state=42)
lr = LinearRegression()
ridge = Ridge(alpha=1.0)

for name, m in [("Linear", lr), ("Ridge", ridge)]:
    scores = cross_val_score(m, X, y, cv=5, scoring="r2")
    print(f"{name} R2: {np.mean(scores):.3f}")
