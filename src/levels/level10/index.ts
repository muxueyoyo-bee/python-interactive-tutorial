import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level10",
  title: "集合 — 不重复的元素",
  category: "基础语法",
  description: "集合的创建和交并差运算",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 2,
  compareMode: "stdout",
  tags: ['集合', 'set'],
};

export default level;
