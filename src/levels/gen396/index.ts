import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen396",
  title: "编写带类型标注的函数: execute",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 session.py（tiangolo/sqlmodel）中 \`execute\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 execute(self, statement: _Executable, params: _CoreAnyExecuteParams | None) -> Result[Any]，返回格式化字符串。

来源：tiangolo/sqlmodel — sqlmodel\\orm\\session.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 execute`,
  answer: "",
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
