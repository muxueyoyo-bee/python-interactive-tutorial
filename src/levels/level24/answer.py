import re
text = "鑱旂郴閭: abc@example.com, 鐢佃瘽: 13800138000"
email = re.search(r"[\w.]+@[\w.]+", text)
phone = re.search(r"1\d{10}", text)
print(email.group() if email else "")
print(phone.group() if phone else "")
