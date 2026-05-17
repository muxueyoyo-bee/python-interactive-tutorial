# 第七十一关: 模型调参 - GridSearchCV

超参数在训练前设定(不同于模型学习的参数). GridSearchCV 自动搜索最佳组合.

## 原理

穷举搜索所有参数组合, 交叉验证评估每种组合, 找出最优配置.

```python
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

param_grid = {"C": [0.1, 1, 10], "kernel": ["linear", "rbf"]}
gs = GridSearchCV(SVC(), param_grid, cv=3)
gs.fit(X_train, y_train)
print(f"最佳参数: {gs.best_params_}")
print(f"最佳分数: {gs.best_score_:.2%}")
```

## 你的任务

用 GridSearchCV 搜索 SVM 的最佳 C 和 kernel.

预期输出: 最佳参数和最佳分数
