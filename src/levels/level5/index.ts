import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level5",
  title: "列表 — 有序的集合",
  category: "基础语法",
  description: "列表的创建、索引访问和基本操作",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 1,
  compareMode: "stdout",
  tags: ['列表', 'list'],
};

export default level;
