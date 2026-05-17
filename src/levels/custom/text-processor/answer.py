from collections import Counter
import re

text = "Python is great. Python is fun. I love Python programming."
words = re.findall(r"\w+", text.lower())
count = Counter(words)
print(count.most_common(3))
