import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen404",
  title: "编写带类型标注的函数: serialize",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 proto_text.py（google/protobuf）中 \`serialize\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 serialize(message: Message, as_utf8: bool, as_one_line: bool, use_short_repeated_primitives: bool, pointy_brackets: bool, use_index_order: bool, use_field_number: bool, descriptor_pool: Optional[DescriptorPool], indent: int, message_formatter: Optional[_MsgFormatter], print_unknown_fields: bool, force_colon: bool) -> str，返回格式化字符串。

来源：google/protobuf — python\\google\\protobuf\\proto_text.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 serialize`,
  answer,
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
