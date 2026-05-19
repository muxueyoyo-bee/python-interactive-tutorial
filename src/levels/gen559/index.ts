import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen559",
  title: "编写带类型标注的函数: extract_from_ast",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 ext.py（pallets/jinja）中 \`extract_from_ast\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 extract_from_ast(ast: nodes.Template, gettext_functions: t.Sequence[str], babel_style: bool) -> t.Iterator[tuple[int, str, str | None | tuple[str | None, ...]]]，返回格式化字符串。

来源：pallets/jinja — src\\jinja2\\ext.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 extract_from_ast`,
  answer,
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
