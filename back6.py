before = input("").split(" ")
oven = input("")

hour = int(before[0])
minute = int(before[1])
second = int(before[2])
cook = int(oven)
second = second + cook
if second >= 60:
    over_second = second // 60
    remain_second = second % 60
    minute = minute + over_second
    if minute >= 60:
        over_minute = minute // 60
        remain_minute = minute % 60
        hour += over_minute
        if hour >= 24:
            hour = hour % 24
        else:
            hour = hour
    else:
        remain_minute = minute
        if hour >= 24:
            hour = hour % 24
        else:
            hour = hour
else:
    remain_second = second % 60
    remain_minute = minute
time = f"{hour} "+f"{remain_minute} "+f"{remain_second}"
print(time)