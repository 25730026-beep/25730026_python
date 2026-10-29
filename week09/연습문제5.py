n = int(input())
i = 1
result = 1
while True:
    result *= i
    if result >= n:
        break
    i += 1
print(i)
