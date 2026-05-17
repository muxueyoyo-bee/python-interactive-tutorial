import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "spam-detector",
  title: "垃圾邮件检测器",
  category: "实战",
  description: "用朴素贝叶斯识别垃圾邮件",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: "用朴素贝叶斯识别垃圾邮件",
  type: "custom",
  difficulty: 4,
  compareMode: "stdout",
  tags: ['NLP', '分类', '朴素贝叶斯'],
};

export default level;
