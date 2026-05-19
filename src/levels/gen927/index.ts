import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen927",
  title: "编写带类型标注的函数: before_execute",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 events.py（sqlalchemy/sqlalchemy）中 \`before_execute\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 before_execute(self, conn: Connection, clauseelement: Executable, multiparams: _CoreMultiExecuteParams, params: _CoreSingleExecuteParams, execution_options: _ExecuteOptions) -> Optional[Tuple[Executable, _CoreMultiExecuteParams, _CoreSingleExecuteParams]]，返回格式化字符串。

来源：sqlalchemy/sqlalchemy — lib\\sqlalchemy\\engine\\events.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 before_execute`,
  answer,
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
