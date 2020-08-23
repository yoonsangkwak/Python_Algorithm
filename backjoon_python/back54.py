# 14916번

change = int(input())
count = 0

while change > 0:
    if change % 5 != 0:
        change -= 2
        if change < 0:
            count = -1
            break
        count += 1
    
    elif change % 5 == 0:
        count += 1
        change -= 5
    
    elif change % 5 != 0 and change % 2 != 0:
        count = -1

print(count)


'''
change = int(input())
count = 0
while True:
    if change % 5 == 0:
        count += change // 5
        break
    change -= 2
    count += 1
    if change < 0:
        count = -1
        break
print(count)
'''