import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level58",
  title: "多头注意力 Multi-Head",
  category: "Transformer",
  description: "实现Multi-Head Attention，理解多头分工",
  content: "",
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 4,
  compareMode: "stdout",
  tags: ['多头注意力', 'Multi-Head'],
};

export default level;
