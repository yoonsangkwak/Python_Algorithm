# 1541번
# https://yoonsang-it.tistory.com/

expression = input().split("-")

for i in range(len(expression)):
    expression[i] = expression[i].split("+")

total_sum = 0
for i in range(len(expression[0])):
    total_sum += int(expression[0][i])

for i in range(1, len(expression)):
    num_sum = 0
    for j in range(len(expression[i])):
        num_sum += int(expression[i][j])

    total_sum -= num_sum

print(total_sum)