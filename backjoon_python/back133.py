# 5597번
# https://yoonsang-it.tistory.com/

attendance = []

for i in range(28):
    attendance.append(int(input()))

attendance_list = sorted(attendance)

answer_list = [i for i in range(1, 31)]

for i in answer_list:
    if i not in attendance_list:
        print(i)