# 1292번
# https://yoonsang-it.tistory.com/

a, b = map(int, input().split())

number_list = [0]
ans = 0

i = 1
while len(number_list) < b + 1:
    for x in range(i):
        number_list.append(i)
    i += 1

for i in range(a, b+1):
    ans += number_list[i]

print(ans)