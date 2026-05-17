import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "housing-predict",
  title: "房价预测挑战",
  category: "实战",
  description: "用梯度提升回归预测加州房价",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: "用梯度提升回归预测加州房价",
  type: "custom",
  difficulty: 4,
  compareMode: "stdout",
  tags: ['回归', 'GBRT', '预测'],
};

export default level;
