from collections import Counter
words = ["a", "b", "c", "a", "b", "a"]
count = Counter(words)
print(count.most_common(2))
