from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, train_test_split

digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data[:500], digits.target[:500], test_size=0.3, random_state=42)
param_grid = {"C": [0.1, 1, 10], "kernel": ["linear", "rbf"]}
gs = GridSearchCV(SVC(), param_grid, cv=3, scoring="accuracy")
gs.fit(X_train, y_train)
print(f"鏈€浣冲弬鏁? {gs.best_params_}")
print(f"鏈€浣冲垎鏁? {gs.best_score_:.2%}")
