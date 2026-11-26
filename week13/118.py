warning_stocks = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
stock = input()
if stock in warning_stocks:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")
