# 4153번

while True:
    triangle = list(map(int, input().split()))
    if triangle[0] == triangle[1] == triangle[2] == 0:
        break
    sorted_triangle = sorted(triangle)

    if (sorted_triangle[0]**2 + sorted_triangle[1]**2) == sorted_triangle[2]**2:
        print("right")
    else:
        print("wrong")
