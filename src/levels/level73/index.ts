import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level73",
  title: "模型持久化 — 保存与加载",
  category: "搭建模型",
  description: "用pickle保存和加载训练好的模型",
  content: "",
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['持久化', 'pickle', 'joblib'],
};

export default level;
