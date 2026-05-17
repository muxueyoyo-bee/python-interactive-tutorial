import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level92",
  title: "GraphRAG: 知识图谱增强",
  category: "AI进阶",
  description: "掌握GraphRAG: 知识图谱增强的核心概念与实现",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 5,
  compareMode: "stdout",
  tags: ['GraphRAG', '知识图谱', '图'],
};

export default level;
