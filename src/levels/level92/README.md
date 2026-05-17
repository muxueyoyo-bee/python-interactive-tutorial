# 第九十二关: GraphRAG -- 知识图谱增强

> 前置回顾: 第91关 RAG, 第30关 itertools

## RAG的局限

传统RAG检索孤立的文档片段, 丢失了**实体之间的关系**。"Python"和"AI"之间的关系在普通RAG中只是一个相似度分数。

## GraphRAG 的优势

GraphRAG 把知识组织成**图结构**: 实体=节点, 关系=边。

```
Python -> 是 -> 编程语言
Python -> 用于 -> AI开发
AI -> 包含 -> 机器学习
机器学习 -> 包含 -> 深度学习
```

## BFS 图遍历

从起始实体出发, 逐层探索:

```python
def graph_search(kg, start, depth=2):
    """从start出发, BFS遍历depth层"""
    queue = [(start, 0)]
    while queue:
        node, d = queue.pop(0)
        if d >= depth: continue
        for child in kg[node]:
            queue.append((child, d+1))
```

## 知识图谱在RAG中的应用

1. 用户问"Python在AI中怎么用"
2. 传统RAG: 检索含"Python"和"AI"的文档
3. GraphRAG: 遍历Python->AI的子图, 理解两者关系路径, 生成更全面的答案

> Microsoft的GraphRAG论文(2024)证明: 图结构RAG在回答"总结这个数据集的主要主题"这类全局问题时明显优于传统RAG。

## 你的任务

实现BFS图遍历, 从"Python"出发遍历两层, 打印每层深度发现的实体。

预期输出:
```
Python知识图谱遍历:
  深度0: ['Python']
  深度1: ['编程语言', 'AI工具']
  深度2: ['机器学习', '深度学习', 'NLP']
```
