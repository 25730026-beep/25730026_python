score = int(input())
if score < 0 or score > 100:
    print("0~100 사이의 점수를 입력하세요.")
else:
    if score > 80:
        grade = "A"
    elif score > 60:
        grade = "B"
    elif score > 40:
        grade = "C"
    elif score > 20:
        grade = "D"
    else:
        grade = "E"
    print("grade is", grade)
