# 第四十三关: matplotlib 折线图

Matplotlib 是 Python 最基础的数据可视化库.

## 绘制折线图

```python
import matplotlib
matplotlib.use("Agg")    # 浏览器模式必须设置
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)     # 从0到10均匀取50个点
y = np.sin(x)

plt.plot(x, y, "b-", label="sin(x)")  # 蓝实线
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sine Wave")
plt.legend()
plt.show()
```

plt.plot 格式: "b-"中 b=blue, -=实线. 也可用 "r--"(红虚线), "g."(绿点).

## 你的任务

绘制 sin(x) 折线图, 加标题, 坐标轴标签和图例. plt.show() 时图表会自动捕获.

预期输出: 一张正弦波折线图
