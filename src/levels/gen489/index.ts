import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "gen489",
  title: "编写 Click CLI 命令: cli",
  category: "中级",
  description: `Click 是 Python 生态中最流行的 CLI 框架之一。

源文件 cli.py 使用 @click.command() 定义 CLI 入口。

请仿照此模式编写一个简单的 Click 命令。

编写一个 Click 命令 cli，用 click.echo() 输出 'Hello, World!'。

来源：pallets/click — examples\\complex\\complex\\cli.py`,
  content: "",
  defaultCode: `import click

# 编写 cli 命令`,
  answer,
  hint: `用 @click.command() 装饰函数，用 click.echo() 输出`,
  type: "main",
  difficulty: 3,
  compareMode: "return",
  tags: ["cli", "click"],
};

export default level;
