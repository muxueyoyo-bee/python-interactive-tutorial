import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen577",
  title: "编写带类型标注的函数: is_internal_attribute",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 sandbox.py（pallets/jinja）中 \`is_internal_attribute\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 is_internal_attribute(obj: t.Any, attr: str) -> bool，返回格式化字符串。

来源：pallets/jinja — src\\jinja2\\sandbox.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 is_internal_attribute`,
  answer,
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
