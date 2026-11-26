exchange_rates = {"달러": 1167, "엔": 1.096, "유로": 1268, "위안": 171}
amount, currency = input().split()
won = float(amount) * exchange_rates[currency]
print(f"{won:.2f} 원")
