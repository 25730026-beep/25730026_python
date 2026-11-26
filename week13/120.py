fruits_by_season = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
fruit = input()
if fruit in fruits_by_season.values():
    print("정답입니다.")
else:
    print("오답입니다.")
