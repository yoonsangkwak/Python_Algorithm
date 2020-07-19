# 11653번

number = int(input(""))

i = 2
j = 0
factoriztion = []

while i <= number:
    if number % i == 0:
        number = number // i
        factoriztion.append(i)
    else:
        i += 1

for num in range(len(factoriztion)):
    print(factoriztion[j])
    j += 1