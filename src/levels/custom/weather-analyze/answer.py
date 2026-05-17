import numpy as np
np.random.seed(42)
temps = np.random.randint(15, 38, 30)
print(f"鏈€楂樻俯: {np.max(temps)} C")
print(f"鏈€浣庢俯: {np.min(temps)} C")
print(f"骞冲潎娓? {np.mean(temps):.1f} C")
print(f"娓╁樊: {np.max(temps) - np.min(temps)} C")
