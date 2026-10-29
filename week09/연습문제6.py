largest = 0
while True:
    n = int(input())
    if n == 0:
        break
    if n > largest:
        largest = n
print(largest)
