import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level40",
  title: "pandas 读取CSV",
  category: "数据分析",
  description: "从CSV数据创建DataFrame",
  content: "",
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['pandas', 'csv'],
};

export default level;
