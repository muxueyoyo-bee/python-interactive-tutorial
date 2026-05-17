import numpy as np

# 简易知识图谱: 实体+关系
# 用字典模拟图结构
kg = {
    "Python": ["编程语言", "AI工具"],
    "AI": ["机器学习", "深度学习", "NLP"],
    "机器学习": ["监督学习", "无监督学习"],
    "深度学习": ["Transformer", "CNN", "RNN"],
}

def graph_search(kg, start, depth=2):
    """BFS图遍历"""
    visited = set()
    queue = [(start, 0)]
    result = {0: [start]}
    while queue:
        node, d = queue.pop(0)
        if d >= depth:
            continue
        for child in kg.get(node, []):
            if child not in visited:
                visited.add(child)
                queue.append((child, d+1))
                result.setdefault(d+1, []).append(child)
    return result

print("Python知识图谱遍历:")
for depth, nodes in graph_search(kg, "Python", 2).items():
    print(f"  深度{depth}: {nodes}")
