import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "housing-predict",
  title: "房价预测挑战",
  category: "实战",
  description: "用梯度提升回归预测加州房价",
  content: md,
  defaultCode: 'from sklearn.datasets import fetch_california_housing\nfrom sklearn.ensemble import GradientBoostingRegressor\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.metrics import r2_score\n\ndata = fetch_california_housing()\nX_train, X_test, y_train, y_test = train_test_split(\n    data.data[:2000], data.target[:2000], test_size=0.2, random_state=42)\n\n# 创建 GradientBoostingRegressor(n_estimators=150, max_depth=4) 并训练\n# 预测并打印 R2 分数',
  answer,
  hint: "用梯度提升回归预测加州房价",
  type: "custom",
  difficulty: 4,
  compareMode: "stdout",
  tags: ['回归', 'GBRT', '预测'],
};

export default level;
