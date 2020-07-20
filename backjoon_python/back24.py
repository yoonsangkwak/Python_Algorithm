# 2884번


'''
late = input("").split(" ")
alarm = 45

hour = int(late[0])
minute = int(late[1])

minute = minute - alarm
if minute < 0:
    under_minute = minute
    remain_minute = 60 + minute
    hour -= 1
    if hour >= 24:
        hour = hour % 24
    elif hour < 0:
        hour = 24 + hour
    else:
        hour = hour
else:
    remain_minute = minute
    if hour >= 24:
        hour = hour % 24
    elif hour < 0:
        hour = 24 + hour
    else:
        hour = hour
time = f"{hour} "+f"{remain_minute}"
print(time)
'''

late = input()
alarm = late.split(' ')
hour = int(alarm[0])
min = int(alarm[1])

min = min - 45
if min < 0:
    min = 60 + min
    hour = hour - 1
if hour < 0:
    hour = 24 + hour

print(f"{hour} {min}")