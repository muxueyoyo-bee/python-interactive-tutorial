import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "ai-text-gen",
  title: "迷你文本生成器",
  category: "实战",
  description: "基于词转移概率生成随机句子",
  content: md,
  defaultCode: 'import random\n\nrandom.seed(42)\n\ntransitions = {\n    "我": ["爱", "喜欢", "想"],\n    "爱": ["Python", "编程", "学习"],\n    "喜欢": ["写代码", "看书", "运动"],\n    "想": ["睡觉", "旅行", "吃火锅"],\n}\n\ndef generate(start="我", length=5):\n    """从start出发, 每次从transitions中随机选下一个词"""\n    current = start\n    result = [current]\n    # 用 for _ in range(length-1) 循环\n    # 如果 current 在 transitions 中, 随机选下一个\n    return "".join(result)\n\n# 生成并打印两句话',
  answer,
  hint: "用字典存储词语的转移关系，实现一个最简单的马尔可夫链文本生成器",
  type: "custom",
  difficulty: 5,
  compareMode: "stdout",
  tags: ['random', '字典', '马尔可夫'],
};

export default level;
