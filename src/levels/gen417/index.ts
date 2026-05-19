import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen417",
  title: "编写带类型标注的函数: update_test_metadata_with_transitive_metadata",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 extract_metadata_from_bazel_xml.py（grpc/grpc）中 \`update_test_metadata_with_transitive_metadata\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 update_test_metadata_with_transitive_metadata(all_extra_metadata: BuildDict, bazel_rules: BuildDict) -> None，返回格式化字符串。

来源：grpc/grpc — tools\\buildgen\\extract_metadata_from_bazel_xml.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 update_test_metadata_with_transitive_metadata`,
  answer: "",
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
