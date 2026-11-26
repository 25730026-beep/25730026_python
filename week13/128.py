number = input().strip().replace("-", "")
if len(number) != 13 or not number.isdecimal():
    print("13자리 숫자를 입력하세요.")
else:
    region_code = int(number[7:9])
    if 0 <= region_code <= 8:
        print("서울입니다.")
    else:
        print("서울이 아닙니다.")
