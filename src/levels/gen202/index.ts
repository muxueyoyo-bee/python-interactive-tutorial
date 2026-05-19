import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen202",
  title: "编写带类型标注的函数: validate_gif",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 validators.py（anthropics/skills）中 \`validate_gif\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 validate_gif(gif_path: str | Path, is_emoji: bool, verbose: bool) -> tuple[bool, dict]，返回格式化字符串。

来源：anthropics/skills — skills\\slack-gif-creator\\core\\validators.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 validate_gif`,
  answer: "",
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
