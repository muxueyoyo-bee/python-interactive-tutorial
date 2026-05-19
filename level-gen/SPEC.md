# Python-Mother 关卡自动生成器 Spec

## 目标

从高 star 开源仓库源码中自动提取 Python 教学模式，生成 python-mother 教学关卡。

## 输入

源码仓库目录，包含各开源项目的完整源码。建议使用 Python 项目为主的仓库集合。

## 输出

每个关卡一个 JSON 文件，格式如下：

```json
{
  "id": 109,
  "title": "自定义异常层次结构",
  "difficulty": "intermediate",
  "tags": ["exception", "error-handling", "class"],
  "source_repo": "psf/requests",
  "source_file": "src/requests/exceptions.py",
  "description": "Requests 库定义了一个完整的异常层次结构。请模仿这个模式...",
  "hint": "从基类 Exception 继承，然后逐层派生具体异常。",
  "task": "定义一个名为 AppError 的基类异常，以及两个子类：ConfigError 和 NetworkError。",
  "expected_stdout": null,
  "expected_return": null,
  "expected_code": "class AppError(Exception):...",
  "template": "class AppError(Exception):\n    pass\n\n# TODO: 定义 ConfigError 和 NetworkError",
  "judge_mode": "return",
  "judge_options": {
    "normalizePunctuation": true,
    "trimWhitespace": true,
    "ignoreTrailingNewline": true
  }
}
```

## 关卡难度分级

| 级别 | 定位 | 模式来源 |
|------|------|---------|
| basic (101-200) | 语法/数据类型 | 从简单代码片段提取 |
| intermediate (201-400) | 设计模式/工程实践 | 从 __init__.py、exceptions.py 提取 |
| advanced (401-600) | 架构/并发/性能 | 从 cli.py、converter.py、__main__.py 提取 |

编号从 109 开始（原有 108 关）。

## 模式提取策略

对每个仓库，按优先级扫描以下文件：

1. `exceptions.py` / `errors.py` → 异常层次结构关卡
2. `conftest.py` → 测试 fixture 关卡
3. `cli.py` / `__main__.py` → CLI 参数解析关卡
4. `__init__.py`（>10行的） → 公共 API 导出关卡
5. `.github/workflows/ci.yml` → CI/CD 阅读关卡

提取逻辑：
- 用 Python AST 解析 .py 文件
- 识别类继承树 → 生成"继承层次结构"关卡
- 识别函数签名（含类型标注）→ 生成"写带类型标注的函数"关卡
- 识别 with/as/contextmanager → 生成"上下文管理器"关卡
- 识别 try/except/finally → 生成"异常处理"关卡
- 识别 @decorator → 生成"装饰器"关卡

## 判定规则（重要！）

全部使用宽松判定：

```python
judge_options = {
    "normalizePunctuation": True,   # 中文标点 → 英文标点
    "trimWhitespace": True,         # 忽略首尾空白
    "ignoreTrailingNewline": True,  # 忽略尾部换行
    "numericTolerance": 0.001,      # 数值容差（如涉及）
    "ignoreCase": False,            # 区分大小写
}
```

宁可多判对，不要冤杀。正则匹配优先于精确匹配。

## 每个仓库的关卡配额

- 小型仓库（<100 源文件）：2-3 关
- 中型仓库（100-500 源文件）：5-8 关
- 大型仓库（>500 源文件）：10-15 关

目标总量：300-500 关

## 仓库优先级（先做这些）

Python 仓库优先：

1. psf/requests — 异常处理、会话管理
2. pallets/click — CLI 装饰器、参数类型
3. fastapi/fastapi — 类型标注、依赖注入
4. pallets/flask — 路由、蓝图
5. pydantic/pydantic — 数据验证模型
6. pytest-dev/pytest — fixture、参数化
7. python-poetry/poetry — 包管理、配置
8. pallets/jinja — 模板引擎
9. celery/celery — 任务队列
10. scikit-learn/scikit-learn — pipeline、estimator

## 生成脚本入口

```bash
python generate.py --repo-dir <path_to_repos> --output-dir <path_to_levels> --start-id 109
```

Reasonix 需要实现 `generate.py`，其余现成。
