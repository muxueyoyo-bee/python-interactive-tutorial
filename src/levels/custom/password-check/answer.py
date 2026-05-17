import re

def check_password(pw):
    score = 0
    if len(pw) >= 8:
        score += 1
    if re.search(r"[a-z]", pw):
        score += 1
    if re.search(r"[A-Z]", pw):
        score += 1
    if re.search(r"\d", pw):
        score += 1
    if re.search(r"[!@#$%^&*]", pw):
        score += 1
    levels = ["弱", "一般", "中等", "强", "非常强"]
    return levels[min(score, 4)]

print(check_password("abc123"))
print(check_password("Python@2025"))
print(check_password("123456"))
