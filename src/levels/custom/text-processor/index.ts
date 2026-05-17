import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "text-processor",
  title: "文本词频统计",
  category: "实战",
  description: "统计文章中出现最多的前3个词",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '一篇英文短文中, 统计每个单词的出现次数, 打印出前3个最常见的词。用 Counter 完成。...',
  type: "custom",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['Counter', '字符串', '统计'],
};

export default level;
