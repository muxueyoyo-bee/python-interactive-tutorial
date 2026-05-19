import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen168",
  title: "编写带类型标注的函数: find_breaking_changes",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 detect-breaking-changes.py（anthropics/anthropic-sdk-python）中 \`find_breaking_changes\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 find_breaking_changes(new_obj: griffe.Object | griffe.Alias, old_obj: griffe.Object | griffe.Alias) -> Iterator[Text | str]，返回格式化字符串。

来源：anthropics/anthropic-sdk-python — scripts\\detect-breaking-changes.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 find_breaking_changes`,
  answer,
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
