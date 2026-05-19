import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen212",
  title: "编写带类型标注的函数: split_eval_set",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 run_loop.py（anthropics/skills）中 \`split_eval_set\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 split_eval_set(eval_set: list[dict], holdout: float, seed: int) -> tuple[list[dict], list[dict]]，返回格式化字符串。

来源：anthropics/skills — skills\\skill-creator\\scripts\\run_loop.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 split_eval_set`,
  answer,
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
