import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level7",
  title: "元组 — 不可变的序列",
  category: "基础语法",
  description: "元组的创建和特性——不可变序列",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 1,
  compareMode: "stdout",
  tags: ['元组', 'tuple'],
};

export default level;
