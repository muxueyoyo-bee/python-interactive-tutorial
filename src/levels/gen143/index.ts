import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen143",
  title: "定义模块的公共 API",
  category: "进阶",
  description: `__all__ 是 Python 模块的公共接口声明，控制 \`from module import *\` 的行为。

源文件 __init__.py 暴露了 25 个公开符号。

请仿照此模式，为以下符号定义 __all__ 列表。

定义 __all__ 列表，包含以下 6 个公开符号: ConnectionError, ConnectTimeout, HTTPError, JSONDecodeError, PreparedRequest, ReadTimeout

来源：psf/requests — src\\requests\\__init__.py`,
  content: "",
  defaultCode: `# 定义 __all__ 暴露以下公共 API: ConnectionError, ConnectTimeout, HTTPError ...`,
  answer: "",
  hint: `__all__ = ['Name1', 'Name2', ...] —— 字符串列表`,
  type: "main",
  difficulty: 1,
  compareMode: "return",
  tags: ["module", "api-design", "__all__"],
};

export default level;
