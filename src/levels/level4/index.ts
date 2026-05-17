import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level4",
  title: "字符串操作",
  category: "基础语法",
  description: "字符串的基本方法：upper()、lower()、len()",
  content: "",
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 1,
  compareMode: "stdout",
  tags: ['字符串', '方法'],
};

export default level;
