import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
categories = ["A", "B", "C", "D"]
values = [23, 45, 56, 78]
plt.bar(categories, values, color=["#306998", "#FFD43B", "#4B8BBE", "#FFE873"])
plt.xlabel("Category")
plt.ylabel("Value")
plt.title("Bar Chart")
plt.show()
