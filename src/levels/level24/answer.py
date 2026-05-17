import re
text = "联系邮箱: abc@example.com, 电话: 13800138000"
email = re.search(r"[\w.]+@[\w.]+", text)
phone = re.search(r"1\d{10}", text)
print(email.group() if email else "")
print(phone.group() if phone else "")
