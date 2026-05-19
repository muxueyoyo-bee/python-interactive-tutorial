import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen798",
  title: "编写带类型标注的函数: infer_constraints_for_callable",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 constraints.py（python/mypy）中 \`infer_constraints_for_callable\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 infer_constraints_for_callable(callee: CallableType, arg_types: Sequence[Type | None], arg_kinds: list[ArgKind], arg_names: Sequence[str | None] | None, formal_to_actual: list[list[int]], context: ArgumentInferContext) -> list[Constraint]，返回格式化字符串。

来源：python/mypy — mypy\\constraints.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 infer_constraints_for_callable`,
  answer: "",
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
