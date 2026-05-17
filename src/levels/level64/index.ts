import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level64",
  title: "注意力可视化",
  category: "Transformer",
  description: "用matplotlib可视化Self-Attention的权重矩阵",
  content: "",
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 4,
  compareMode: "plot",
  tags: ['可视化', '注意力权重'],
};

export default level;
