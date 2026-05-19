import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen208",
  title: "编写带类型标注的函数: improve_description",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 improve_description.py（anthropics/skills）中 \`improve_description\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 improve_description(skill_name: str, skill_content: str, current_description: str, eval_results: dict, history: list[dict], model: str, test_results: dict | None, log_dir: Path | None, iteration: int | None) -> str，返回格式化字符串。

来源：anthropics/skills — skills\\skill-creator\\scripts\\improve_description.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 improve_description`,
  answer: "",
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
