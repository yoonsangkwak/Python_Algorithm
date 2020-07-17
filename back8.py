a = input("")
num_a = int(a)

pocket = []

i = 0
j = 1
while j <= num_a:
    mars = input("").split(" ")
    pocket.append(mars[i])
    i += 1
    j += 1
print(pocket)
