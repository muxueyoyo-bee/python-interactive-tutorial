import random
random.seed(42)

transitions = {
    "鎴?: ["鐖?, "鍠滄", "鎯?],
    "鐖?: ["Python", "缂栫▼", "瀛︿範"],
    "鍠滄": ["鍐欎唬鐮?, "鐪嬩功", "杩愬姩"],
    "鎯?: ["鐫¤", "鏃呰", "鍚冪伀閿?],
}

def generate(start="鎴?, length=5):
    current = start
    result = [current]
    for _ in range(length - 1):
        if current in transitions:
            current = random.choice(transitions[current])
        else:
            current = random.choice(list(transitions.keys()))
        result.append(current)
    return "".join(result)

print(generate("鎴?, 5))
print(generate("鎴?, 5))
