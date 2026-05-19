import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen911",
  title: "编写带类型标注的函数: instance",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 exc.py（sqlalchemy/sqlalchemy）中 \`instance\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 instance(cls, statement: Optional[str], params: Optional[_AnyExecuteParams], orig: Exception, dbapi_base_err: Type[Exception], hide_parameters: bool, connection_invalidated: bool, dialect: Optional[Dialect], ismulti: Optional[bool]) -> StatementError，返回格式化字符串。

来源：sqlalchemy/sqlalchemy — lib\\sqlalchemy\\exc.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 instance`,
  answer: "",
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
