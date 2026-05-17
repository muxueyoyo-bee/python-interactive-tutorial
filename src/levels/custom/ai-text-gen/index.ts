import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "ai-text-gen",
  title: "迷你文本生成器",
  category: "实战",
  description: "基于词转移概率生成随机句子",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: "用字典存储词语的转移关系，实现一个最简单的马尔可夫链文本生成器",
  type: "custom",
  difficulty: 5,
  compareMode: "stdout",
  tags: ['random', '字典', '马尔可夫'],
};

export default level;
