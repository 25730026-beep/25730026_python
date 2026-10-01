def varfunc(*args):
    print(args)

varfunc(10)
varfunc(10, 20, 30)


def add(*numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total

print(add(10, 20))
print(add(10, 20, 30))
