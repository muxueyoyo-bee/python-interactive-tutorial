import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "credit-fraud",
  title: "信用卡欺诈检测",
  category: "实战",
  description: "处理极度不平衡的信用卡欺诈数据",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: "处理极度不平衡的信用卡欺诈数据",
  type: "custom",
  difficulty: 5,
  compareMode: "stdout",
  tags: ['异常检测', '分类', '不平衡'],
};

export default level;
