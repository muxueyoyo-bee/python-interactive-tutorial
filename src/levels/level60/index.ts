import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level60",
  title: "前馈网络与 LayerNorm",
  category: "Transformer",
  description: "实现FeedForward和Layer Normalization",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 4,
  compareMode: "stdout",
  tags: ['FeedForward', 'LayerNorm'],
};

export default level;
