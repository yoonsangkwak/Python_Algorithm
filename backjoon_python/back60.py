# 1085번

x, y, m, h = map(int, input().split())

up = h - y
down = y
right = m - x
left = x

print(min(up, down, right, left))