# 10156번

price, snack, money = map(int, input().split())
if price * snack >= money:
    mom = price * snack - money
elif price * snack < money:
    mom = 0
print(mom)