# 第二十三关: datetime 日期时间

datetime 模块用于处理日期和时间.

## 创建日期时间

```python
from datetime import datetime

now = datetime(2025, 1, 1)
print(now)  # 2025-01-01 00:00:00
```

## 时间加减

```python
from datetime import datetime, timedelta

now = datetime(2025, 1, 1)
future = now + timedelta(days=30)  # 30天后
```

## 格式化输出

```python
print(now.strftime("%Y-%m-%d"))  # 2025-01-01
```

常用格式化码: %Y年 %m月 %d日 %H时 %M分 %S秒

## 你的任务

创建日期 2025年1月1日, 计算 30 天后的日期, 分别按 %Y-%m-%d 格式打印.

预期输出:
```
2025-01-01
2025-01-31
```
