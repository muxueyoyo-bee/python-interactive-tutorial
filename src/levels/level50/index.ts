import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level50",
  title: "损失函数 — 衡量模型好坏",
  category: "AI基础",
  description: "计算MSE和MAE，理解不同的误差衡量方式",
  content: "",
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['损失函数', 'MSE', 'MAE'],
};

export default level;
