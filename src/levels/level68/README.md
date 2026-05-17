# 第六十八关: 分类模型实战 - 多种算法对比

不同算法各有千秋. 用交叉验证对比性能.

## 交叉验证

将数据分成 K 折, 每次用 K-1 折训练, 1折验证, 取平均.

```python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5)
print(f"{np.mean(scores):.2%} +/- {np.std(scores):.2%}")
```

## 三种分类器

- LogisticRegression: 简单, 可解释
- DecisionTree: 直观, 易过拟合
- RandomForest: 集成, 准确率高

## 你的任务

对比三种分类器的5折交叉验证准确率.

预期输出: 三种模型的准确率对比
