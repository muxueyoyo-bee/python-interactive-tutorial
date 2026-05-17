import random
random.seed(42)

transitions = {
    "我": ["爱", "喜欢", "想"],
    "爱": ["Python", "编程", "学习"],
    "喜欢": ["写代码", "看书", "运动"],
    "想": ["睡觉", "旅行", "吃火锅"],
}

def generate(start="我", length=5):
    current = start
    result = [current]
    for _ in range(length - 1):
        if current in transitions:
            current = random.choice(transitions[current])
        else:
            current = random.choice(list(transitions.keys()))
        result.append(current)
    return "".join(result)

print(generate("我", 5))
print(generate("我", 5))
