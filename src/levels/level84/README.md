# 第八十四关: 混淆矩阵与ROC曲线

> 前置回顾: 第55关 模型评估(Accuracy/Precision/Recall/F1), 第48关 逻辑回归

## 准确率够用吗?

99%准确率的模型可能毫无用处: 如果正样本只有1%, 模型全部预测为负就能拿99%准确率 -- 但它没找出任何一个正样本。

## 混淆矩阵

```
              预测为正  预测为负
实际为正        TP        FN
实际为负        FP        TN
```

从混淆矩阵可以算出所有指标:

- Accuracy = (TP+TN)/Total
- Precision = TP/(TP+FP)
- Recall = TP/(TP+FN)
- F1 = 2*P*R/(P+R)

> 回顾第55关: 这些指标的定义和计算公式。

## ROC 曲线与 AUC

ROC曲线画的是: 不同阈值下, TPR(Recall) vs FPR 的关系。

- AUC = Area Under Curve: ROC曲线下的面积
- AUC=1.0: 完美分类器
- AUC=0.5: 随机猜测
- AUC<0.5: 比随机还差(反向预测)

AUC 的好处: 不依赖具体阈值, 评估模型整体的排序能力。

## 你的任务

训练逻辑回归, 打印混淆矩阵和AUC分数。

预期输出:
```
混淆矩阵:
[[xx xx]
 [xx xx]]

AUC: 0.xxx
```
