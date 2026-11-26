prefix = input()[:3]
if prefix in ("010", "011", "012"):
    print("강북구")
elif prefix in ("013", "014", "015"):
    print("도봉구")
elif prefix in ("016", "017", "018", "019"):
    print("노원구")
else:
    print("해당 구를 판별할 수 없습니다.")
