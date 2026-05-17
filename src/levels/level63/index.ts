import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level63",
  title: "完整 Transformer — 组装",
  category: "Transformer",
  description: "从架构层面理解完整Transformer的数据流",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 5,
  compareMode: "stdout",
  tags: ['完整模型', '组装'],
};

export default level;
