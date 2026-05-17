import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "customer-churn",
  title: "客户流失预测",
  category: "实战",
  description: "用机器学习预测哪些客户可能流失",
  content: md,
  defaultCode: 'import numpy as np\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.model_selection import train_test_split\n\nnp.random.seed(42)\nn = 200\nX = np.random.randn(n, 5)\nX[:, 2] = np.abs(X[:, 2]) * 3\ny = (X[:, 0]*2 + X[:, 1]*1.5 - X[:, 2]*3 + X[:, 3]*0.5 + np.random.randn(n)*2 > 0).astype(int)\n\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)\n\n# TODO: 创建并训练随机森林模型\n# model = RandomForestClassifier(...)\n# model.fit(...)\n\n# TODO: 评估并打印准确率\n# print(f"准确率: {model.score(X_test, y_test):.1%}")\n',
  answer,
  hint: "用机器学习预测哪些客户可能流失",
  type: "custom",
  difficulty: 4,
  compareMode: "stdout",
  tags: ['分类', 'sklearn', '业务'],
};

export default level;
