# 10103번

Round = int(input())
chang = 100
sang = 100

for num in range(Round):
    dice1, dice2 = map(int, input().split())
    if dice1 > dice2:
        sang -= dice1
    elif dice1 < dice2:
        chang -= dice2

print(chang)
print(sang)