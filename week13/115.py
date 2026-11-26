result = int(input()) - 20
if result < 0:
    result = 0
elif result > 255:
    result = 255
print("출력값:", result)
