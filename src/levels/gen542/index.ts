import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen542",
  title: "编写装饰器: app_errorhandler",
  category: "进阶",
  description: `装饰器是 Python 中用于包装函数、添加横切关注点的强大模式。

源文件 blueprints.py（pallets/flask）中 \`app_errorhandler\` 展示了装饰器模式。

请编写一个装饰器，在函数调用前后各打印一行信息。

编写装饰器 app_errorhandler，包装目标函数并在调用前后打印 'before call' 和 'after call'。

来源：pallets/flask — src\\flask\\sansio\\blueprints.py`,
  content: "",
  defaultCode: `# 编写装饰器 app_errorhandler`,
  answer,
  hint: `外层函数接受 func 参数，内层定义 wrapper(*args, **kwargs)，外层 return wrapper`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["decorator", "functional"],
};

export default level;
