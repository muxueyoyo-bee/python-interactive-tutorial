import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen516",
  title: "编写带类型标注的函数: get_buffer",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 _winconsole.py（pallets/click）中 \`get_buffer\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 get_buffer(obj: Buffer, writable: bool) -> Array[c_char]，返回格式化字符串。

来源：pallets/click — src\\click\\_winconsole.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 get_buffer`,
  answer: "",
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
