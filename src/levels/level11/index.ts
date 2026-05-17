import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level11",
  title: "if 条件判断",
  category: "基础语法",
  description: "if/elif/else 多分支判断",
  content: "",
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 2,
  compareMode: "stdout",
  tags: ['if', '条件'],
};

export default level;
