a = input("")
num_a = int(a)

for num in range(num_a):
    mars = input("").split(" ")
    answer = float(mars[0])
    i = 1
    while i < len(mars):
        if mars[i] == '@':
            answer = answer * 3
        elif mars[i] == '%':
            answer = answer + 5
        elif mars[i] == '#':
            answer = answer - 7
        i += 1
    print(f"{answer:.2f}")
