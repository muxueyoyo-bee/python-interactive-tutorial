import numpy as np
np.random.seed(42)
temps = np.random.randint(15, 38, 30)
print(f"最高温: {np.max(temps)} C")
print(f"最低温: {np.min(temps)} C")
print(f"平均温: {np.mean(temps):.1f} C")
print(f"温差: {np.max(temps) - np.min(temps)} C")
