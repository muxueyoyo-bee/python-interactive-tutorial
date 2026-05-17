import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level26",
  title: "面向对象：类与对象",
  category: "进阶",
  description: "面向对象编程：定义类和创建对象",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['OOP', 'class'],
};

export default level;
