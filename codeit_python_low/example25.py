import datetime

pi_day = datetime.datetime(2020, 3, 14)
print(pi_day)
print(type(pi_day))
print()
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(pi_day)
print(type(pi_day))
print()

today = datetime.datetime.now()
print(today)
print(type(today))
print()

print(today - pi_day)
print(type(today - pi_day))
print()

my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10, seconds=50)
print(today)
print(today + my_timedelta)
print()

print(today)
print(today.year)  # 연도
print(today.month)  # 월
print(today.day)  # 일
print(today.hour)  # 시
print(today.minute)  # 분
print(today.second)  # 초
print(today.microsecond)  # 마이크로초
print()

print(today.strftime("%A, %B %dth %Y"))