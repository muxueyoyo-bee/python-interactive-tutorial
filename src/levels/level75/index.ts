import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "level75",
  title: "综合AI实战 — 端到端项目",
  category: "搭建模型",
  description: "端到端乳腺癌分类项目：预处理→模型→评估",
  content: "",
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '仔细阅读题目要求，按照期望输出格式编写代码',
  type: "main",
  difficulty: 5,
  compareMode: "stdout",
  tags: ['综合', '项目', '端到端'],
};

export default level;
