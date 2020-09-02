# 5622번

alphabet = input()
dialog = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
Total_time = 0

for i in range(len(alphabet)):
    time = 2
    for j in range(len(dialog)):
        if alphabet[i] in dialog[j]:
            time += (j + 1)
            Total_time += time

print(Total_time)