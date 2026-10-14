hour, minute = map(int, input().split())
period = "PM" if hour >= 12 else "AM"
if hour >= 13:
    hour -= 12
print(f"{hour:02d} : {minute:02d} {period}")
