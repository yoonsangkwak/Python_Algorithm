# 10039번

i = 0
pocket = []


while i < 5:
    student = int(input(""))
    if student <= 40:
        student = 40
    pocket.append(student)
    i += 1

i = 0
score = 0
while i < 5:
    score = score + pocket[i]
    i += 1


print(int(score/5))


'''
s = 0
for i in range(5) :
	s += max(40, int(input()))
print(s/5)
'''