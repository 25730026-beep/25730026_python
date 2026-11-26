carriers = {"011": "SKT", "016": "KT", "019": "LGU"}
phone_number = input()
carrier = carriers.get(phone_number[:3], "알수없음")
print(f"당신은 {carrier} 사용자입니다.")
