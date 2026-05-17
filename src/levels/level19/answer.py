nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared = list(map(lambda x: x**2, nums))
even = list(filter(lambda x: x % 2 == 0, nums))
print(squared)
print(even)
