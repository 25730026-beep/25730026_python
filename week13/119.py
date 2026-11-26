fruits_by_season = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
season = input()
if season in fruits_by_season.keys():
    print("정답입니다.")
else:
    print("오답입니다.")
