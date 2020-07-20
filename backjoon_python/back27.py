# 10102번

judge = int(input())
vote = input()
red = vote.count('A')
blue = vote.count('B')
if red > blue:
    print("A")
elif red < blue:
    print('B')
elif  red == blue:
    print("Tie")