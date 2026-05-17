import numpy as np
def gradient_descent(lr=0.1, epochs=10):
    x = 10.0
    history = []
    for _ in range(epochs):
        grad = 2 * x
        x -= lr * grad
        history.append(round(x, 2))
    return history

print(gradient_descent())
