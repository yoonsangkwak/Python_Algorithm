# 11399번

people = int(input())
output_list = list(map(int, input().split()))

answer = 0
temp = 0

for j in range(len(output_list)):
    temp += sorted(output_list)[j]
    answer += temp

print(answer)