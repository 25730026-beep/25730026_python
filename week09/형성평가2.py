a, b = map(int, input().split())
total = 0
while a <= b:
    total += a
    a += 1
print(total)
