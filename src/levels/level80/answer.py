import numpy as np
np.random.seed(42)

# 妯℃嫙: 鐪熷疄鍑芥暟 y=2x+1, 鍔犲櫔澹?
X = np.linspace(0, 5, 20)
y_true = 2*X + 1 + np.random.randn(20)*0.5

# 妯″瀷1: 甯告暟(楂樺亸宸?  model2: 杩囨嫙鍚?楂樻柟宸?  model3: 鍒氬ソ
m1 = np.full_like(X, np.mean(y_true))
m2 = np.polyval(np.polyfit(X, y_true, 10), X)  # 10娆″椤瑰紡
m3 = np.polyval(np.polyfit(X, y_true, 1), X)   # 1娆?绾挎€?

print("楂樺亸宸?娆犳嫙鍚?璇樊:", round(np.mean((y_true-m1)**2), 3))
print("楂樻柟宸?杩囨嫙鍚?璇樊:", round(np.mean((y_true-m2)**2), 3))
print("鎭板ソ鎷熷悎璇樊:     ", round(np.mean((y_true-m3)**2), 3))
