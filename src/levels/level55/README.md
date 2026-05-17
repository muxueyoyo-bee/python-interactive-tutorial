# 第五十五关: 模型评估指标

评估分类模型需要多个指标, 不能只看准确率.

## 混淆矩阵

| | 预测正 | 预测负 |
|------|------|------|
| 实际正 | TP | FN |
| 实际负 | FP | TN |

## 核心指标

- Accuracy = (TP+TN) / total: 预测正确的比例
- Precision = TP / (TP+FP): 预测为正的样本中实际为正的比例
- Recall = TP / (TP+FN): 实际为正的样本中被找出的比例
- F1 = 2 * P * R / (P + R): Precision和Recall的调和平均数

## 你的任务

给定真实标签和预测标签, 计算 Accuracy, Precision, Recall, F1.

预期输出:
```
Accuracy: 80.0%
Precision: 80.0%
Recall: 80.0%
F1: 80.0%
```
