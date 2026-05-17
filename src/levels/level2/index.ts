import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level2",
  title: "变量与赋值 — 给数据起个名字",
  category: "基础语法",
  description: "学习变量和赋值语句",
  content: md,
  defaultCode: '# 请在此处编写代码\nname = ""\nage = 0\nprint()',
  answer,
  hint: '使用 = 给变量赋值，print() 中可以用逗号连接多个输出项',
  type: "main",
  difficulty: 1,
  compareMode: "stdout",
  tags: ["变量", "赋值", "入门"],
};

export default level;
