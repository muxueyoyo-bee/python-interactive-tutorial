import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen403",
  title: "编写带类型标注的函数: serialize",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 proto_json.py（google/protobuf）中 \`serialize\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 serialize(message: Message, always_print_fields_with_no_presence: bool, preserving_proto_field_name: bool, use_integers_for_enums: bool, descriptor_pool: Optional[DescriptorPool]) -> dict，返回格式化字符串。

来源：google/protobuf — python\\google\\protobuf\\proto_json.py`,
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
