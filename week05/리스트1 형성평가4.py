n = int(input())
lst = []

for i in range(n):
    value = int(input())
    lst.append(value)

print(int(sum(lst) / n))
