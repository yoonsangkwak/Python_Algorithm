# 11720번

n = int(input())
num = input()
answer = 0

for i in range(len(num)):
    answer += int(num[i])

print(answer)