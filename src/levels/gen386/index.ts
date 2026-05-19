import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen386",
  title: "编写带类型标注的函数: format_file",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 format_docs_code.py（sqlalchemy/sqlalchemy）中 \`format_file\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 format_file(file: Path, exit_on_error: bool, check: bool) -> tuple[bool, int]，返回格式化字符串。

来源：sqlalchemy/sqlalchemy — tools\\format_docs_code.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 format_file`,
  answer: "",
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
