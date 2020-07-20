# 11557번

T = int(input())

for i in range(T):
    case = int(input())
    pocket = ""
    normal = 0
    for j in range(case):
        test = input().split()
        univ = test[0]
        alchol = int(test[1])
        if alchol > normal:
            pocket = univ
            normal = alchol
    print(pocket)

'''
T = int(input())
for i in range(T):

    n=int(input())
    univ=[]
    bottle=[]

    for i in range(n):
        A, B = input().split()
        univ.append(A)
        bottle.append(int(B))
        
    print(univ[bottle.index(max(bottle))])
  '''