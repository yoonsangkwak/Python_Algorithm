# 2455번

train = 0
people = []

for _ in range(4):
    people.append(train)

    bye, hi = map(int, input().split())

    train -= bye
    train += hi

print(max(people))