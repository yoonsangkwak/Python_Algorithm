# 11021번

i = input("")
j = int(i)

pocket = []

for num in range(j):
    test = input("").split(" ")
    pocket.append(test[0])
    pocket.append(test[1])

k = 0
a = 1
while k + 1 <= 2 * j and a <= j:
    calc = int(pocket[k]) + int(pocket[k + 1])
    case = "Case #" + f"{a}" + ": "
    print(f"{case}{pocket[k]} + {pocket[k + 1]} = {calc}")
    a += 1
    k += 2
