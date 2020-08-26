# 1110번

num = input()
if len(num) < 2:
    num = "0" + num
original = num
count = 0
    
while True:
    new_num = str(int(num[0]) + int(num[1]))
    if len(new_num) < 2:
        new_num = "0" + new_num
    
    num = num[1] + new_num[1]

    count += 1
    if num == original:
        break

print(count)