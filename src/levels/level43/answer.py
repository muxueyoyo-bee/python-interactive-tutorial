import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42)
x = np.linspace(0, 10, 50)
y = np.sin(x)
plt.plot(x, y, "b-", label="sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sine Wave")
plt.legend()
plt.show()
