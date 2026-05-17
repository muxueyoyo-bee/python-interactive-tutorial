import numpy as np
def perceptron(x, w, b):
    return 1 if np.dot(w, x) + b > 0 else 0

# AND逻辑门
w = np.array([1, 1])
b = -1.5
print(perceptron([0,0], w, b))  # 0
print(perceptron([0,1], w, b))  # 0
print(perceptron([1,0], w, b))  # 0
print(perceptron([1,1], w, b))  # 1
