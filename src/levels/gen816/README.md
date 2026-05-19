# 第816关: 定义模块的公共 API

> 真实案例：scikit-learn/scikit-learn 的 `sklearn\callback\__init__.py` 中使用了这个模式。

## 概念介绍

__all__ 是 Python 模块的公共接口声明，控制 `from module import *` 的行为。

源文件 __init__.py 暴露了 8 个公开符号。

请仿照此模式，为以下符号定义 __all__ 列表。

## 关键点

__all__ = ['Name1', 'Name2', ...] —— 字符串列表

## 你的任务

定义 __all__ 列表，包含以下 6 个公开符号: AutoPropagatedCallback, CallbackContext, CallbackSupportMixin, FitCallback, ProgressBar, ScoringMonitor

请按照上方任务描述编写代码。
