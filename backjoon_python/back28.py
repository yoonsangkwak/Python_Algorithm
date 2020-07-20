# 10886번

people = int(input())
pocket = []

for num in range(people):
    vote = input()
    pocket.append(vote)

cute = pocket.count('1')
not_cute = pocket.count('0')

if cute > not_cute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")