# 11047번

coin, value = map(int, input().split())
price = []
for i in range(coin):
    price.append(int(input()))

sorted_price = sorted(price, reverse=True)
count = 0
for j in range(len(sorted_price)):
    count += (value // sorted_price[j])
    value %= sorted_price[j]

print(count)