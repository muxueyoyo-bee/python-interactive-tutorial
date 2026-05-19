import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen125",
  title: "定义模块的公共 API",
  category: "进阶",
  description: `__all__ 是 Python 模块的公共接口声明，控制 \`from module import *\` 的行为。

源文件 __init__.py 暴露了 7 个公开符号。

请仿照此模式，为以下符号定义 __all__ 列表。

定义 __all__ 列表，包含以下 6 个公开符号: ASGITransport, AsyncBaseTransport, BaseTransport, AsyncHTTPTransport, HTTPTransport, MockTransport

来源：encode/httpx — httpx\\_transports\\__init__.py`,
  content: "",
  defaultCode: `# 定义 __all__ 暴露以下公共 API: ASGITransport, AsyncBaseTransport, BaseTransport ...`,
  answer: "",
  hint: `__all__ = ['Name1', 'Name2', ...] —— 字符串列表`,
  type: "main",
  difficulty: 1,
  compareMode: "return",
  tags: ["module", "api-design", "__all__"],
};

export default level;
