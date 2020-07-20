# 7567번

plate = input("")

length = 10
i = 1
while i < len(plate):
    if plate[i - 1] == plate[i]:
        length += 5
    elif plate[i - 1] != plate[i]:
        length += 10
    i += 1

print(length)