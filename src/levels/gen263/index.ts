import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen263",
  title: "编写带类型标注的函数: iter_rows",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 formatting.py（pallets/click）中 \`iter_rows\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 iter_rows(rows: cabc.Iterable[tuple[str, str]], col_count: int) -> cabc.Iterator[tuple[str, ...]]，返回格式化字符串。

来源：pallets/click — src\\click\\formatting.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 iter_rows`,
  answer: "",
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
