# 1987번

n = int(input())
num_list = list(map(int, input().split()))
count = 0

for i in range(len(num_list)):
    check = True
    if num_list[i] == 1:
        check = False
        
    for j in range(2, num_list[i]):
        if num_list[i] % j == 0:
            check = False
            break
    if check == True:
        count += 1

print(count)