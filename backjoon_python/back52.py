# 2217번

case = int(input())
rope = []
for i in range(case):
    rope.append(int(input()))

sorted_list = sorted(rope, reverse=True)
max_list = []

for j in range(len(sorted_list)):
    max_list.append(sorted_list[j] * (j+1))

print(max(max_list))