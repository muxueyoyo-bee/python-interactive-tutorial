import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level65",
  title: "Transformer 家族 — BERT与GPT",
  category: "Transformer",
  description: "了解BERT、GPT、T5等变体的设计差异",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 2,
  compareMode: "stdout",
  tags: ['BERT', 'GPT', '家族'],
};

export default level;
