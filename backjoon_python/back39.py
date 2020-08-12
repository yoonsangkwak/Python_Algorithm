# 2309번

pocket = []

sum = 0
for i in range(0, 9):
    nanjang = int(input(""))
    pocket.append(nanjang)
    sum += pocket[i]

gap = sum - 100
j = 0
fake_nanjang = []

for a in range(len(pocket)):
    for b in range(len(pocket) - 1):
        if pocket[a] + pocket[b] == gap:
            fake_nanjang.append(pocket[a])
            fake_nanjang.append(pocket[b])

pocket.remove(fake_nanjang[-1])
pocket.remove(fake_nanjang[-2])

pocket.sort()

for x in range(len(pocket)):
    print(pocket[x])