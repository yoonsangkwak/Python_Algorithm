a = input("")
num_a = int(a)

for num in range(num_a):
    test = input("").split(" ")
    S = test[1]
    R = int(len(S))
    P = []
    i = 0
    while i < R:
        P.append(S[i] * int(test[0]))
        i += 1
    string = "".join(P)
    print(string)