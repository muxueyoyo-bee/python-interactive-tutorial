import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen881",
  title: "编写装饰器: register_operation",
  category: "进阶",
  description: `装饰器是 Python 中用于包装函数、添加横切关注点的强大模式。

源文件 base.py（sqlalchemy/alembic）中 \`register_operation\` 展示了装饰器模式。

请编写一个装饰器，在函数调用前后各打印一行信息。

编写装饰器 register_operation，包装目标函数并在调用前后打印 'before call' 和 'after call'。

来源：sqlalchemy/alembic — alembic\\operations\\base.py`,
  content: "",
  defaultCode: `# 编写装饰器 register_operation`,
  answer,
  hint: `外层函数接受 func 参数，内层定义 wrapper(*args, **kwargs)，外层 return wrapper`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["decorator", "functional"],
};

export default level;
