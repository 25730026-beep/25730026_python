fruits = ["apple", "banana", "apple", "melon", "banana", "apple"]
count = {}
for fruit in fruits:
    count[fruit] = count.get(fruit, 0) + 1
for key, value in count.items():
    print(key, ":", value)
