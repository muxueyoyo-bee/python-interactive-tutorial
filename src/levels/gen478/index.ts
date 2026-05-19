import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen478",
  title: "编写带类型标注的函数: run_pyright_with_coverage",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 pyright_completeness.py（numpy/numpy）中 \`run_pyright_with_coverage\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 run_pyright_with_coverage(pyright_args: list[str], exclude_like: Sequence[str]) -> int，返回格式化字符串。

来源：numpy/numpy — tools\\pyright_completeness.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 run_pyright_with_coverage`,
  answer: "",
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
