# 1744번
# https://yoonsang-it.tistory.com/

n = int(input())
negative = []
positive = []
num_sum = 0

for _ in range(n):
    num = int(input())
    if num <= 0:
        negative.append(num)
    elif num == 1:
        num_sum += 1
    elif num > 1:
        positive.append(num)

negative.sort()
positive.sort(reverse=True)

for i in range(0, len(negative), 2):
    if i+1 < len(negative):
        num_sum += negative[i] * negative[i+1]
    else:
        num_sum += negative[i]

for i in range(0, len(positive), 2):
    if i+1 < len(positive):
        num_sum += positive[i] * positive[i+1]
    else:
        num_sum += positive[i]

print(num_sum)