import os, json
BASE = r"C:\Users\15346\Desktop\python-mother\src\levels"

# Read content data from JSON
with open(r"C:\Users\15346\Desktop\python-mother\tutorial_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for key, content in data.items():
    path = os.path.join(BASE, key, "README.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Written {len(data)} tutorials")