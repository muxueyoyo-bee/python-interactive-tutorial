import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level69",
  title: "回归模型实战",
  category: "搭建模型",
  description: "对比线性回归和Ridge回归的R²分数",
  content: "",
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['回归', '预测'],
};

export default level;
