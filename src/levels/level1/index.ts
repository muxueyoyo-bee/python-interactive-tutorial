import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level1",
  title: "Hello World — 你好，世界",
  category: "基础语法",
  description: "学习 print() 函数，输出你的第一行 Python 代码",
  content: "",
  defaultCode: '# 请在此处编写代码\nprint("")',
  answer,
  hint: '使用 print() 函数输出文本，例如 print("Hello, World!")',
  type: "main",
  difficulty: 1,
  compareMode: "stdout",
  tags: ["print", "入门"],
};

export default level;
