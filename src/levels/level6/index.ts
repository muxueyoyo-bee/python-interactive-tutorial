import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level6",
  title: "列表的增删改查",
  category: "基础语法",
  description: "列表的增删改查：append()、insert()、remove()",
  content: "",
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 2,
  compareMode: "stdout",
  tags: ['列表', '方法'],
};

export default level;
