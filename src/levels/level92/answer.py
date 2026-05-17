import numpy as np

# 绠€鏄撶煡璇嗗浘璋? 瀹炰綋+鍏崇郴
# 鐢ㄥ瓧鍏告ā鎷熷浘缁撴瀯
kg = {
    "Python": ["缂栫▼璇█", "AI宸ュ叿"],
    "AI": ["鏈哄櫒瀛︿範", "娣卞害瀛︿範", "NLP"],
    "鏈哄櫒瀛︿範": ["鐩戠潱瀛︿範", "鏃犵洃鐫ｅ涔?],
    "娣卞害瀛︿範": ["Transformer", "CNN", "RNN"],
}

def graph_search(kg, start, depth=2):
    """BFS鍥鹃亶鍘?""
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

print("Python鐭ヨ瘑鍥捐氨閬嶅巻:")
for depth, nodes in graph_search(kg, "Python", 2).items():
    print(f"  娣卞害{depth}: {nodes}")
