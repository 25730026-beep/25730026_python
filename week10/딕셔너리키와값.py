fruits = ["apple", "banana", "apple", "melon", "banana", "apple"]
count = {}
for fruit in fruits:
    count[fruit] = count.get(fruit, 0) + 1
print(count.keys())
print(*count.keys())
print(count.values())
print(*count.values())
