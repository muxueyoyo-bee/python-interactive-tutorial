# 第四十四关: matplotlib 柱状图

柱状图用于比较不同类别的数值.

## 绘制柱状图

```python
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

categories = ["A", "B", "C", "D"]
values = [23, 45, 56, 78]
colors = ["#306998", "#FFD43B", "#4B8BBE", "#FFE873"]

plt.bar(categories, values, color=colors)
plt.xlabel("Category")
plt.ylabel("Value")
plt.title("Bar Chart")
plt.show()
```

## 你的任务

绘制四个类别的柱状图, 每根柱子用不同颜色, 加标题和坐标轴标签.

预期输出: 一张四柱彩色柱状图
