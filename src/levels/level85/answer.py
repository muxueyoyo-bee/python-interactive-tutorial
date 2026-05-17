from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

pipe = Pipeline([("scaler", StandardScaler()), ("svm", SVC())])
pipe.fit(X_train, y_train)
print(f"Pipeline测试准确率: {pipe.score(X_test, y_test):.2%}")
print(f"Pipeline步骤: {[s[0] for s in pipe.steps]}")
