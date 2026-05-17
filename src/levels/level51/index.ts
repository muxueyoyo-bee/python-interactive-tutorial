import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level51",
  title: "过拟合与正则化",
  category: "AI基础",
  description: "实现L1/L2正则化项，理解模型复杂度惩罚",
  content: "",
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 4,
  compareMode: "stdout",
  tags: ['过拟合', '正则化', 'L1', 'L2'],
};

export default level;
