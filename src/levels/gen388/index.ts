import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen388",
  title: "编写带类型标注的函数: include_file_in_rd_header",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 glsl_builders.py（godotengine/godot）中 \`include_file_in_rd_header\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 include_file_in_rd_header(filename: str, header_data: RDHeaderStruct, depth: int) -> RDHeaderStruct，返回格式化字符串。

来源：godotengine/godot — glsl_builders.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 include_file_in_rd_header`,
  answer,
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
