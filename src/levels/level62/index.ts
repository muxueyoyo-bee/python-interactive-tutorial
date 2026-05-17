import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level62",
  title: "Transformer Decoder 层",
  category: "Transformer",
  description: "实现Cross-Attention，理解Decoder如何关注Encoder",
  content: "",
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 5,
  compareMode: "stdout",
  tags: ['Decoder', 'Cross-Attention'],
};

export default level;
