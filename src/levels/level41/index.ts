import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level41",
  title: "pandas groupby 分组",
  category: "数据分析",
  description: "分组聚合操作",
  content: "",
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 4,
  compareMode: "stdout",
  tags: ['pandas', 'groupby'],
};

export default level;
