import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "credit-fraud",
  title: "信用卡欺诈检测",
  category: "实战",
  description: "处理极度不平衡的信用卡欺诈数据",
  content: md,
  defaultCode: 'import numpy as np\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.metrics import recall_score\n\nnp.random.seed(42)\nn = 500\nX = np.random.randn(n, 10)\ny = np.zeros(n, dtype=int)\nfraud_idx = np.random.choice(n, 5, replace=False)\ny[fraud_idx] = 1  # 仅1%是欺诈\n\nX_train, X_test, y_train, y_test = train_test_split(\n    X, y, test_size=0.3, random_state=42, stratify=y)\n\n# 用 RandomForestClassifier(class_weight="balanced") 处理不平衡数据\n# 训练后预测, 打印欺诈召回率 (recall_score)',
  answer,
  hint: "处理极度不平衡的信用卡欺诈数据",
  type: "custom",
  difficulty: 5,
  compareMode: "stdout",
  tags: ['异常检测', '分类', '不平衡'],
};

export default level;
