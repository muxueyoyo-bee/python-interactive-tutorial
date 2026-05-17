import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "customer-churn",
  title: "客户流失预测",
  category: "实战",
  description: "用机器学习预测哪些客户可能流失",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: "用机器学习预测哪些客户可能流失",
  type: "custom",
  difficulty: 4,
  compareMode: "stdout",
  tags: ['分类', 'sklearn', '业务'],
};

export default level;
