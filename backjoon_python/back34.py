# 9506번

while True:
    n = int(input())
    if n == -1:
        break
    pocket = []
    i = 1
    while i < n:
        if n % i == 0:
            pocket.append(i)
        i += 1
    i = 0
    check = 0
    while i < len(pocket):
        check += pocket[i]
        i += 1
    answer = " + ".join(map(str, pocket))
    if n == check:
        print(f"{n} = {answer}")
    else:
        print(f"{n} is NOT perfect.")