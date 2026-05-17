import numpy as np

def relu(x): return np.maximum(0, x)
def sigmoid(x): return 1/(1+np.exp(-x))
def tanh(x): return np.tanh(x)
def leaky_relu(x, a=0.01): return np.where(x>0, x, a*x)

x = np.array([-2, -1, 0, 1, 2])
print("ReLU:     ", relu(x))
print("Sigmoid:  ", sigmoid(x).round(3))
print("Tanh:     ", tanh(x).round(3))
print("LeakyReLU:", leaky_relu(x))
