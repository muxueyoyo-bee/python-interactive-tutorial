import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level12",
  title: "for 循环",
  category: "基础语法",
  description: "for循环和range()遍历序列",
  content: "",
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 2,
  compareMode: "stdout",
  tags: ['for', '循环'],
};

export default level;
