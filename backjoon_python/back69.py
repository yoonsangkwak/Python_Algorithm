# 2750번

n = int(input())
num_list = []
for i in range(n):
    num = int(input())
    num_list.append(num)

sorted_list = sorted(num_list)

for j in range(len(sorted_list)):
    print(sorted_list[j])