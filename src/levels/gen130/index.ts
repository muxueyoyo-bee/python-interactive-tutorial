import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen130",
  title: "编写带类型标注的函数: feed_data",
  category: "中级",
  description: `类型标注使代码更可读、IDE 能提供更好的自动补全。

源文件 http_parser.py（aio-libs/aiohttp）中 \`feed_data\` 展示了完整的参数和返回值类型标注。

请仿照此模式编写一个带类型标注的函数。

编写函数 feed_data(self, data: bytes, SEP: _SEP, EMPTY: bytes, CONTENT_LENGTH: istr, METH_CONNECT: str, SEC_WEBSOCKET_KEY1: istr) -> tuple[list[tuple[_MsgT, StreamReader]], bool, bytes]，返回格式化字符串。

来源：aio-libs/aiohttp — aiohttp\\http_parser.py`,
  content: "",
  defaultCode: `# 编写带类型标注的函数 feed_data`,
  answer,
  hint: `def 函数名(参数: 类型, ...) -> 返回类型: —— 参数和返回值都标注类型`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["type-hints", "annotations"],
};

export default level;
