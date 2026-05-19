# Python-Mother — 闯关式 Python 自学网站

基于 Vue 3 + Pyodide 的闯关式 Python 自学网站，966 关循序渐进，浏览器内直接运行 Python。

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
| 扩展关卡 | gen109–982 | AST 自动生成：异常处理、装饰器、类型标注、CLI、上下文管理器等 |

## 关卡生成器

从开源项目源码中自动提取 8 种编程教学模式：

```bash
python level-gen/generate.py --repo-dir <源码仓库目录> --start-id 109
```

详情见 `level-gen/README.md`。

## 技术栈

- **前端**: Vue 3 + TypeScript + Ant Design Vue + Pinia
- **Python 运行时**: Pyodide (WebAssembly, 浏览器端执行)
- **编辑器**: Monaco Editor
- **关卡生成**: Python AST 解析 + MD5 hash 去重
- **构建**: Vite
