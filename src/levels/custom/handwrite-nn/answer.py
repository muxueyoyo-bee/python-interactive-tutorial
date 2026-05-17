import numpy as np
from sklearn.datasets import load_digits
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)
X_train = X_train / 16.0
X_test = X_test / 16.0

model = MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=500, random_state=42)
model.fit(X_train, y_train)
print(f"鎵嬪啓鏁板瓧璇嗗埆鍑嗙‘鐜? {model.score(X_test, y_test):.1%}")
print(f"闅愯棌灞傜粨鏋? {model.hidden_layer_sizes}")
