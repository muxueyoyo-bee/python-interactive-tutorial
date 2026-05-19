# Python-Mother Level Generator

从开源项目源码中自动提取编程教学模式，生成 Python-Mother 关卡。

## 快速开始

```bash
# 扫描源码仓库，生成关卡
python generate.py --repo-dir <path-to-repos> --output-dir <path-to-output> --start-id 109

# 限制仓库数量试跑
python generate.py --repo-dir <path-to-repos> --output-dir ./levels --start-id 109 --limit-repos 3
```

## 支持的关卡类型

| 提取器 | 触发文件 | 教学模式 |
|--------|---------|---------|
| `extract_exception_hierarchy` | exceptions.py, errors.py | 自定义异常类层级 |
| `extract_test_fixtures` | conftest.py | pytest fixture |
| `extract_cli_patterns` | cli.py, __main__.py | Click/argparse 命令行 |
| `extract_api_exports` | __init__.py | `__all__` 公共 API |
| `extract_decorator_patterns` | 任意 .py | 装饰器模式 |
| `extract_context_manager` | 任意 .py | 上下文管理器 |
| `extract_error_handling` | 任意 .py | try/except 错误处理 |
| `extract_type_annotation` | 任意 .py | 类型标注 |

## 输出格式

每个关卡生成一个目录，包含：
- `index.ts` — 关卡元数据（标题、分类、提示、答案引用）
- `answer.py` — 参考解答
- `README.md` — 教学内容（概念介绍、关键点、常见陷阱、任务要求）

## 去重策略

- 基于 `(title, expected_code)` 的 MD5 hash 全局去重
- 私有命名（`_` 前缀）自动跳过
- 测试文件、migrations、site-packages 自动跳过

## 配置

编辑 `generate.py` 顶部的参数：
- `GENERAL_EXTRACTORS` — 通用提取器列表
- `EXTRACTORS` — 命名文件提取器
- `TAG_CATEGORY` — 标签到分类的映射
