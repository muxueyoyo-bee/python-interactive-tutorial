from typing import List, Dict

def process(data: List[int]) -> Dict[str, int]:
    return {"sum": sum(data), "len": len(data), "max": max(data)}

result = process([1, 2, 3, 4, 5])
print(result)
