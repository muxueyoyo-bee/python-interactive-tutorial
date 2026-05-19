import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen584",
  title: "定义模块的公共 API",
  category: "进阶",
  description: `__all__ 是 Python 模块的公共接口声明，控制 \`from module import *\` 的行为。

源文件 __init__.py 暴露了 21 个公开符号。

请仿照此模式，为以下符号定义 __all__ 列表。

定义 __all__ 列表，包含以下 6 个公开符号: CHAINED_WARNING_DISABLED, HAS_PYARROW, IS64, ISMUSL, PY312, PY314

来源：pandas-dev/pandas — pandas\\compat\\__init__.py`,
  content: "",
  defaultCode: `# 定义 __all__ 暴露以下公共 API: CHAINED_WARNING_DISABLED, HAS_PYARROW, IS64 ...`,
  answer: "",
  hint: `__all__ = ['Name1', 'Name2', ...] —— 字符串列表`,
  type: "main",
  difficulty: 1,
  compareMode: "return",
  tags: ["module", "api-design", "__all__"],
};

export default level;
