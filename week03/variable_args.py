a = [1, 2, 3]
b = (1, 2, 3)

def add(*numbers):
    total = 0
    for i in numbers:
        total = total + i
    print(type(numbers))
    return total

print(add(10, 20))
