import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen376",
  title: "编写带类型标注的函数: create_model_field",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 utils.py（fastapi/fastapi）中 \`create_model_field\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 create_model_field(name: str, type_: Any, default: Any | None, field_info: FieldInfo | None, alias: str | None, mode: Literal['validation', 'serialization']) -> ModelField，返回格式化字符串。

来源：fastapi/fastapi — fastapi\\utils.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 create_model_field`,
  answer,
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
