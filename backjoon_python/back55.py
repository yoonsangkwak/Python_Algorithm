# 10448번

case = int(input())
gauss_list = []

for _ in range(case):
    gauss = int(input())
    gauss_list.append(gauss)

triangle = []
check_list = []
for n in range(1, 46):
    tri_num = n * (n+1) // 2
    triangle.append(tri_num)

for a in range(len(triangle)):
    for b in range(len(triangle)):
        for c in range(len(triangle)):
            num = triangle[a] + triangle[b] + triangle[c]
            check_list.append(num)

for x in range(len(gauss_list)):
    if gauss_list[x] in check_list:
        print(1)
    else:
        print(0)
