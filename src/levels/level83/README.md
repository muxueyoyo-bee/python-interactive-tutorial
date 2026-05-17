# 第八十三关: 集成学习 -- Bagging与Boosting

> 前置回顾: 第54关 决策树, 第68关 分类模型对比

## 三个臭皮匠, 顶个诸葛亮

集成学习(Ensemble)组合多个弱模型, 形成一个强模型。两种主流策略:

## Bagging (Bootstrap Aggregating)

并行训练多个模型, 每个用不同的数据子集, 最后投票/平均:

```python
RandomForestClassifier(n_estimators=100)  # 100棵树投票
```

特点: 降低方差, 防止过拟合。每棵树独立训练, 可以并行。

## Boosting

串行训练, 每个新模型专注于前一个模型犯的错:

```python
GradientBoostingClassifier(n_estimators=100)  # 100轮迭代改进
```

特点: 降低偏差, 逐步提升。不能并行, 但通常比Bagging更准。

## Bagging vs Boosting

| | Bagging | Boosting |
|------|---------|----------|
| 训练方式 | 并行 | 串行 |
| 降低 | 方差 | 偏差 |
| 代表 | 随机森林 | XGBoost, LightGBM |
| 速度 | 快(可并行) | 慢 |
| 过拟合风险 | 低 | 需小心调参 |

> XGBoost 是 Kaggle 竞赛之王, 大多数表格数据比赛的冠军方案都用了它。

## 你的任务

对分类数据, 对比随机森林(Bagging)和梯度提升(Boosting)的5折交叉验证准确率。

预期输出:
```
RandomForest: xx% +/- xx%
GradientBoost: xx% +/- xx%
```
