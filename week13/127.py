number = input().strip().replace("-", "")
if len(number) != 13 or not number.isdecimal():
    print("13자리 숫자를 입력하세요.")
elif number[6] in ("1", "3"):
    print("남자")
elif number[6] in ("2", "4"):
    print("여자")
else:
    print("문제에서 정의한 성별 코드가 아닙니다.")
