import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "game-rpg",
  title: "RPG 角色战力排行",
  category: "实战",
  description: "对角色列表按公式排序",
  content: md,
  defaultCode: '# 请在此处编写代码\n',
  answer,
  hint: '你正在设计 RPG 游戏。有5个英雄, 每个有攻击力/防御力/生命值。战力=攻击+防御+生命/100。按战力降序输出排行...',
  type: "custom",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['排序', 'lambda', '列表'],
};

export default level;
