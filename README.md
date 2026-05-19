# Python 基础交互教程

> 学 SQL 的时候发现 SQLBolt、SQLZoo 这种交互式前端学习网站特别好用，不用装环境不用配终端，打开浏览器就能写代码。但找了很久，Python 生态里竟然没有一个同等体验的东西。既然如此，依葫芦画瓢，自己做一个。

基于 Vue 3 + Pyodide，966 关循序渐进，浏览器内直接运行 Python 代码。内置关卡参考了 GitHub 上高 star 项目的最佳实践路径，同时把 AI / 机器学习的基础知识也整合进来，一条线从 Hello World 学到 Transformer。

## 快速启动

```bash
npm install
npx vite --host
# 打开 http://localhost:5173
```

## 项目结构

```
├── src/
│   ├── levels/          # 关卡 (92 内置 + 874 自动生成)
│   │   ├── level1/      # index.ts + answer.py + README.md
│   │   ├── gen109/      # 自动生成关卡 (gen109–gen982)
│   │   └── level.d.ts   # 关卡类型定义
│   ├── components/      # Vue 组件 (编辑器、判题面板、题目展示)
│   ├── engine/          # Python 执行引擎 (Pyodide Web Worker)
│   ├── judge/           # 判题引擎 (stdout/return/both/plot)
│   ├── pages/           # 页面
│   └── core/            # 全局状态 (Pinia)
├── level-gen/           # 关卡自动生成器
│   ├── generate.py      # AST 模式提取 → TS 关卡输出
│   └── SPEC.md          # 生成器设计规格
└── package.json
```

## 关卡体系

| 阶段 | 范围 | 内容 |
|------|------|------|
| 基础语法 | 1–15 | Hello World → 函数参数 |
| 中级 | 16–25 | 列表推导式 → 模块与导入 |
| 进阶 | 26–35 | OOP → 单元测试 |
| 数据分析 | 36–45 | numpy → pandas → matplotlib |
| AI 基础 | 46–55 | 线性回归 → 模型评估 |
| Transformer | 56–65 | Self-Attention → BERT/GPT |
| 搭建模型 | 66–75 | scikit-learn → 综合项目 |
| AI 进阶 | 76–92 | 高级专题 |
| 扩展关卡 | gen109–982 | 自动生成关卡，涵盖异常处理、装饰器、类型标注、CLI、上下文管理器等 |

## 关卡生成器

扩展关卡由 Python AST 解析器从 74 个开源项目的源码中自动提取，通过 MD5 hash 全局去重，生成带教学内容的完整关卡。

```bash
python level-gen/generate.py --repo-dir <源码仓库目录> --start-id 109
```

提取的 8 种教学模式：自定义异常层级、pytest fixture、Click/argparse CLI、`__all__` 公共 API、装饰器、上下文管理器、try/except 错误处理、类型标注。

## 参考项目

### Python 生态（主要来源）

| 项目 | 说明 |
|------|------|
| [pallets/flask](https://github.com/pallets/flask) | Web 微框架 |
| [pallets/jinja](https://github.com/pallets/jinja) | 模板引擎 |
| [pallets/click](https://github.com/pallets/click) | CLI 框架 |
| [django/django](https://github.com/django/django) | Web 全栈框架 |
| [fastapi/fastapi](https://github.com/fastapi/fastapi) | 现代 Web API 框架 |
| [encode/httpx](https://github.com/encode/httpx) | HTTP 客户端 |
| [encode/starlette](https://github.com/encode/starlette) | 轻量 ASGI 框架 |
| [encode/uvicorn](https://github.com/encode/uvicorn) | ASGI 服务器 |
| [encode/databases](https://github.com/encode/databases) | 异步数据库客户端 |
| [tiangolo/sqlmodel](https://github.com/tiangolo/sqlmodel) | ORM |
| [tiangolo/typer](https://github.com/tiangolo/typer) | CLI 框架 |
| [psf/requests](https://github.com/psf/requests) | HTTP 库 |
| [aio-libs/aiohttp](https://github.com/aio-libs/aiohttp) | 异步 HTTP |
| [pydantic/pydantic](https://github.com/pydantic/pydantic) | 数据校验 |
| [sqlalchemy/sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | ORM |
| [sqlalchemy/alembic](https://github.com/sqlalchemy/alembic) | 数据库迁移 |
| [celery/celery](https://github.com/celery/celery) | 任务队列 |
| [python-poetry/poetry](https://github.com/python-poetry/poetry) | 包管理器 |
| [pypa/pip](https://github.com/pypa/pip) | 包管理器 |
| [astral-sh/ruff](https://github.com/astral-sh/ruff) | Linter |
| [python/mypy](https://github.com/python/mypy) | 静态类型检查 |
| [pytest-dev/pytest](https://github.com/pytest-dev/pytest) | 测试框架 |
| [sphinx-doc/sphinx](https://github.com/sphinx-doc/sphinx) | 文档生成 |
| [redis/redis](https://github.com/redis/redis) | 键值数据库 |
| [anthropics/anthropic-sdk-python](https://github.com/anthropics/anthropic-sdk-python) | AI SDK |
| [anthropics/skills](https://github.com/anthropics/skills) | AI 技能系统 |
| [anthropics/courses](https://github.com/anthropics/courses) | AI 教程 |

### 科学计算 & AI

| 项目 | 说明 |
|------|------|
| [numpy/numpy](https://github.com/numpy/numpy) | 数值计算 |
| [pandas-dev/pandas](https://github.com/pandas-dev/pandas) | 数据分析 |
| [matplotlib/matplotlib](https://github.com/matplotlib/matplotlib) | 可视化 |
| [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn) | 机器学习 |
| [google/protobuf](https://github.com/google/protobuf) | 序列化协议 |
| [grpc/grpc](https://github.com/grpc/grpc) | RPC 框架 |

### 跨语言参考

C / C++ / Rust / TypeScript / Lua 等多个语言的高 star 项目也纳入扫描，作为工程实践的横向参考：

[git/git](https://github.com/git/git)、[FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg)、[curl/curl](https://github.com/curl/curl)、[openssl/openssl](https://github.com/openssl/openssl)、[nginx/nginx](https://github.com/nginx/nginx)、[tmux/tmux](https://github.com/tmux/tmux)、[vim/vim](https://github.com/vim/vim)、[redis/redis](https://github.com/redis/redis)、[sqlite/sqlite](https://github.com/sqlite/sqlite)、[libuv/libuv](https://github.com/libuv/libuv)、[libevent/libevent](https://github.com/libevent/libevent)、[libgit2/libgit2](https://github.com/libgit2/libgit2)、[nlohmann/json](https://github.com/nlohmann/json)、[google/googletest](https://github.com/google/googletest)、[google/leveldb](https://github.com/google/leveldb)、[catchorg/Catch2](https://github.com/catchorg/Catch2)、[abseil/abseil-cpp](https://github.com/abseil/abseil-cpp)、[godotengine/godot](https://github.com/godotengine/godot)、[obsproject/obs-studio](https://github.com/obsproject/obs-studio)、[opencv/opencv](https://github.com/opencv/opencv)、[dolphin-emu/dolphin](https://github.com/dolphin-emu/dolphin)、[audacity/audacity](https://github.com/audacity/audacity)、[mpv-player/mpv](https://github.com/mpv-player/mpv)、[alacritty/alacritty](https://github.com/alacritty/alacritty)、[official-stockfish/Stockfish](https://github.com/official-stockfish/Stockfish)、[keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc)、[OpenRCT2/OpenRCT2](https://github.com/OpenRCT2/OpenRCT2)、[ocornut/imgui](https://github.com/ocornut/imgui)、[BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)、[tokio-rs/tokio](https://github.com/tokio-rs/tokio)、[denoland/deno](https://github.com/denoland/deno)、[vuejs/core](https://github.com/vuejs/core)、[microsoft/TypeScript](https://github.com/microsoft/TypeScript)、[swc-project/swc](https://github.com/swc-project/swc)、[slidevjs/slidev](https://github.com/slidevjs/slidev)、[TanStack/query](https://github.com/TanStack/query)、[tauri-apps/tauri](https://github.com/tauri-apps/tauri)、[lua/lua](https://github.com/lua/lua)、[yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp)、[meilisearch/meilisearch](https://github.com/meilisearch/meilisearch)、[LING71671/Open-ClaudeCode](https://github.com/LING71671/Open-ClaudeCode)

## 技术栈

- **前端**: Vue 3 + TypeScript + Ant Design Vue + Pinia
- **Python 运行时**: Pyodide (WebAssembly, 浏览器端执行)
- **编辑器**: Monaco Editor
- **关卡生成**: Python AST 解析 + MD5 hash 去重
- **构建**: Vite
