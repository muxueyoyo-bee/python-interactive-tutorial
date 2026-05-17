from datetime import datetime, timedelta
now = datetime(2025, 1, 1)
future = now + timedelta(days=30)
print(now.strftime("%Y-%m-%d"))
print(future.strftime("%Y-%m-%d"))
