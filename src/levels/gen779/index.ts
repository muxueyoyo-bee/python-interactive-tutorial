import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen779",
  title: "编写带类型标注的函数: map_actuals_to_formals",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 argmap.py（python/mypy）中 \`map_actuals_to_formals\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 map_actuals_to_formals(actual_kinds: list[nodes.ArgKind], actual_names: Sequence[str | None] | None, formal_kinds: list[nodes.ArgKind], formal_names: Sequence[str | None], actual_arg_type: Callable[[int], Type]) -> list[list[int]]，返回格式化字符串。

来源：python/mypy — mypy\\argmap.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 map_actuals_to_formals`,
  answer: "",
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
