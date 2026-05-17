import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level54",
  title: "决策树 — 可解释的AI",
  category: "AI基础",
  description: "计算信息增益，理解决策树的分裂原理",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 4,
  compareMode: "stdout",
  tags: ['决策树', '信息增益'],
};

export default level;
