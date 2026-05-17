import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

print("sigmoid(0) =", round(sigmoid(0), 3))
print("sigmoid(2) =", round(sigmoid(2), 3))
print("sigmoid(-2) =", round(sigmoid(-2), 3))
