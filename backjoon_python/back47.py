# 5585번

money = int(input())
change = 1000 - money
coin_list = [500, 100, 50, 10, 5, 1]
count = 0

for coin in coin_list:
    count += (change // coin)
    change %= coin

print(count)