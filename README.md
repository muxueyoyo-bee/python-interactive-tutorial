# Python之母 - 闯关式 Python 自学网站

纯前端实现的闯关式 Python 自学网站，从零基础到 AI 建模，75 关循序渐进。

## 技术栈

- **框架**: Vue 3 + TypeScript + Vite
- **UI**: ant-design-vue 4
- **编辑器**: Monaco Editor（VS Code 同款）
- **Python 执行**: Pyodide（WebAssembly，浏览器内运行 CPython）
- **数据科学**: numpy / pandas / matplotlib / scikit-learn
- **Markdown 渲染**: bytemd

## 快速启动

```bash
# 1. 安装依赖
npm install

# 2. 启动开发服务器
npm run dev

# 3. 打开浏览器访问
# http://localhost:5173
```

构建生产版本：

```bash
npm run build
npm run preview
```

## 关卡体系

| 阶段 | 关卡 | 内容 |
|---|---|---|
| 📖 基础语法 | 1-15 | Hello World → 函数参数与返回值 |
| ⚡ 中级 | 16-25 | 列表推导式 → 模块与导入 |
| 🔥 进阶 | 26-35 | OOP → 单元测试 |
| 📊 数据分析 | 36-45 | numpy → pandas → matplotlib |
| 🧠 AI基础 | 46-55 | 线性回归 → 模型评估指标 |
| 🔬 Transformer | 56-65 | Self-Attention → BERT/GPT |
| 🏗️ 搭建模型 | 66-75 | scikit-learn 全流程 → 综合项目 |

## 使用方式

1. 左侧阅读教程
2. 右侧 Monaco 编辑器中编写 Python 代码
3. 点击「运行」或按 `Ctrl+Enter` 执行
4. 首次运行会下载 Pyodide 引擎（约 15MB，需等待 30-60 秒），之后浏览器缓存就快了
5. 输出与预期一致即可进入下一关

## 注意事项

- 首次点击「运行」需要下载 Python 运行时（~15MB），请耐心等待
- 不要写死循环，浏览器标签页会卡住（刷新页面即可恢复）
- 仅在浏览器本地运行，不需要后端服务
