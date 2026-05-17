# 第九十关: 端到端ML项目 -- 房价预测

> 前置回顾: 第75关 综合AI实战, 第85关 Pipeline, 第83关 集成学习

## 完整ML项目流程

1. **加载数据**: fetch_california_housing (加州房价)
2. **划分**: train_test_split
3. **预处理**: StandardScaler
4. **交叉验证**: 评估模型稳定性
5. **训练**: GradientBoostingRegressor
6. **评估**: MAE + R2

## 回归 vs 分类评估

- 分类用: Accuracy, Precision, Recall, F1, AUC
- 回归用: MAE(平均绝对误差), MSE, R2(决定系数)

```python
from sklearn.metrics import mean_absolute_error, r2_score

# MAE: 平均差多少元
print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f}")

# R2: 模型解释了%的方差, 越接近1越好
print(f"R2: {r2_score(y_test, y_pred):.3f}")
```

## 你的任务

完成加州房价预测全流程: CV评估 -> 训练 -> 测试MAE和R2。

预期输出:
```
CV R2: 0.xxx +/- 0.xxx
Test MAE: 0.xxx
Test R2: 0.xxx
```
