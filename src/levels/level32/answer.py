import json
data = {"name": "小明", "age": 18, "skills": ["Python", "SQL"]}
json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(json_str)
parsed = json.loads(json_str)
print(parsed["skills"][0])
