# 1546번

case = int(input())
score = list(map(int, input().split()))

good = max(score)
new_score = 0
for i in range(len(score)):
    new_score += score[i] / good * 100

print(new_score / case) 