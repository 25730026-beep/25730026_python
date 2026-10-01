a = input()
print(a)
print(type(a))

a = int(input())
print(a)
print(type(a))

a = float(input())
print(a)
print(type(a))

a, b = input().split()
print(a, b)
print(type(a), type(b))

a, b = input().split(" ")
print(a, b)

a, b = map(int, input().split())
print(a, b)
print(type(a), type(b))

a, b = map(float, input().split())
print(a, b)
print(type(a), type(b))
