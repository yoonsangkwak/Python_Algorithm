# 14720번

market = int(input())
market_list = list(map(int, input().split()))

count = 0
current_milk = -1

for i in range(len(market_list)):
    if market_list[i] == (current_milk + 1) % 3:
        count += 1
        current_milk += 1

print(count)