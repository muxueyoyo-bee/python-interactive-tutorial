import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level59",
  title: "位置编码 Positional Encoding",
  category: "Transformer",
  description: "实现正弦位置编码，理解Transformer如何处理顺序",
  content: "",
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['位置编码', 'Positional'],
};

export default level;
