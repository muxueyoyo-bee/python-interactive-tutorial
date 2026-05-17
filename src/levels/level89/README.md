# 第八十九关: 特征重要性分析

> 前置回顾: 第72关 特征工程(SelectKBest), 第83关 集成学习(随机森林)

## 哪些特征最重要?

特征重要性告诉你模型"依赖"哪些特征做决策。两种主流方法:

## 1. 内置特征重要性 (随机森林)

随机森林训练时自动计算每个特征对减少不纯度的贡献:

```python
rf.feature_importances_  # 每个特征的重要性分数, 和为1
```

## 2. Permutation 重要性 (模型无关)

打乱某个特征的值, 看模型性能下降多少:

```python
from sklearn.inspection import permutation_importance

# 打乱特征i -> 准确率下降越多 -> 特征越重要
perm = permutation_importance(model, X_test, y_test)
```

## 内置 vs Permutation

| | 内置 | Permutation |
|------|------|------------|
| 速度 | 快(免费) | 慢(需多次推理) |
| 适用 | 仅树模型 | 任何模型 |
| 偏差 | 偏向高基数特征 | 较客观 |

## 你的任务

用糖尿病数据训练随机森林, 分别用内置和Permutation方法找出Top-3重要特征。

预期输出:
```
内置重要性Top-3: [x x x]
Permutation重要性Top-3: [x x x]
```
