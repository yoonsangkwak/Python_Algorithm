# 3009번

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

x_list = sorted([x1, x2, x3])
y_list = sorted([y1, y2, y3])

if x_list[0] == x_list[1] < x_list[2]:
    x4 = x_list[2]
elif x_list[0] < x_list[1] == x_list[2]:
    x4 = x_list[0]


if y_list[0] == y_list[1] < y_list[2]:
    y4 = y_list[2]
elif y_list[0] < y_list[1] == y_list[2]:
    y4 = y_list[0]

print(f"{x4} {y4}")

# list.count() : 리스트안에 몇개들어있는지 셀수있음