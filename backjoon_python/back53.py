# 15904번

sentence = input()
check = ["U", "C", "P", "C"]
foo = True

for i in range(len(check)):
    if check[i] in sentence:
        foo = True
        idx = sentence.find(check[i])
        sentence = sentence[idx:]
    else:
        foo = False
        break

if foo == True:
    print("I love UCPC")
else:
    print("I hate UCPC")