# 2292번

n = int(input())

line = 1
next_num = 1

if n == 1:
    print(1)
else:
    while True:
        if n <= next_num:
            print(line)
            break
        
        next_num += (6 * line)
        line += 1 