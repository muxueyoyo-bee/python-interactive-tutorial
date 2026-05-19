import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen359",
  title: "编写带类型标注的函数: signal_handler",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 basereload.py（encode/uvicorn）中 \`signal_handler\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 signal_handler(self, sig: int, frame: FrameType | None) -> None，返回格式化字符串。

来源：encode/uvicorn — uvicorn\\supervisors\\basereload.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 signal_handler`,
  answer,
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
