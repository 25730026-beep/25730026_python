def get_area(radius):
area = 3.14 * radius**2
return area

result = get_area(3)
print("반지름이 3인 원의 면적=", result)


a = [1,2,3]
b = (1,2,3)

def add(*numbers):
sum = 0
for i in numbers:
print(type(numbers))

print(add(10, 20))
