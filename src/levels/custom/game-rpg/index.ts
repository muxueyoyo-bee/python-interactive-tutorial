import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "game-rpg",
  title: "RPG 角色战力排行",
  category: "实战",
  description: "对角色列表按公式排序",
  content: md,
  defaultCode: 'heroes = [\n    {"name":"战士", "atk":180, "def":120, "hp":5000},\n    {"name":"法师", "atk":280, "def":50,  "hp":3000},\n    {"name":"射手", "atk":220, "def":80,  "hp":3500},\n    {"name":"坦克", "atk":80,  "def":250, "hp":8000},\n    {"name":"刺客", "atk":300, "def":40,  "hp":2500},\n]\n\n# 战力 = atk + def + hp//100\n# 按战力降序排序, 打印排行榜: "名次. 名称 (战力:xxx)"',
  answer,
  hint: '你正在设计 RPG 游戏。有5个英雄, 每个有攻击力/防御力/生命值。战力=攻击+防御+生命/100。按战力降序输出排行...',
  type: "custom",
  difficulty: 3,
  compareMode: "stdout",
  tags: ['排序', 'lambda', '列表'],
};

export default level;
