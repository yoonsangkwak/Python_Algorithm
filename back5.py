# 2525번

before = input("").split(" ")
oven = input("")

hour = int(before[0])
minute = int(before[1])
cook = int(oven)
minute = minute + cook
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
time = f"{hour} "+f"{remain_minute}"
print(time)