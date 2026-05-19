import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen965",
  title: "编写带类型标注的函数: generate_table_lines",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 update_requirements.py（yt-dlp/yt-dlp）中 \`generate_table_lines\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 generate_table_lines(table_name: str, table: dict[str, str | bool | int | float | list[str | dict[str, str]]]) -> collections.abc.Iterator[str]，返回格式化字符串。

来源：yt-dlp/yt-dlp — devscripts\\update_requirements.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 generate_table_lines`,
  answer,
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
