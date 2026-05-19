# 第268关: 编写 Click CLI 命令: run_command

> 真实案例：pallets/flask 的 `src\flask\cli.py` 中使用了这个模式。

## 概念介绍

Click 是 Python 生态中最流行的 CLI 框架之一。

源文件 cli.py 使用 @click.command() 定义 CLI 入口。

请仿照此模式编写一个简单的 Click 命令。

## 代码示例

```python
import click

@click.command()
click.option('--host', '-h', default='127.0.0.1', help='The interface to bind to.')
click.option('--port', '-p', default=5000, help='The port to bind to.')
def run_command():
    click.echo('Hello, World!')
```

## 关键点

用 @click.command() 装饰函数，用 click.echo() 输出

## 常见陷阱

- `if __name__ == '__main__':` 保证脚本既能导入又能直接运行
- Click 的 `@click.option('--name')` 自动生成 `--help` 文档
- argparse 的 `add_argument` 支持 `type=int` 自动类型转换

## 你的任务

编写一个 Click 命令 run_command，用 click.echo() 输出 'Hello, World!'。

预期行为：参考上方代码示例的输出。
