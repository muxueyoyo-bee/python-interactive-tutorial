# 第三十二关: json 数据处理

JSON 是最通用的数据交换格式. json 模块用于序列化和反序列化.

## Python -> JSON (序列化)

```python
import json
data = {"name": "小明", "age": 18, "skills": ["Python", "SQL"]}
json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(json_str)
```

## JSON -> Python (反序列化)

```python
parsed = json.loads(json_str)
print(parsed["skills"][0])   # Python
```

关键参数: ensure_ascii=False 保留中文, indent=2 缩进2格.

## 你的任务

将一个字典序列化为 JSON (保留中文, 缩进2格), 再反序列化回来, 访问 skills[0].

预期输出: 格式化的 JSON + Python
