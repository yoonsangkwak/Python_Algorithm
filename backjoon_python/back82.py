# 1436번

n = int(input())

end_num = 666
idx = 0

while True:
    if "666" in str(end_num):
        idx += 1
    if idx == n:
        print(end_num)
        break
    end_num += 1