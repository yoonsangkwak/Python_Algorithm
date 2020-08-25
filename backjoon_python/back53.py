# 15904번

sentence = input()
check_list = ["U", "C", "P", "C"]
check = True

for i in range(len(check_list)):
    if check_list[i] in sentence:
        check = True
        idx = sentence.find(check_list[i])
        sentence = sentence[idx + 1:]
    else:
        check = False
        break

if check == True:
    print("I love UCPC")
else:
    print("I hate UCPC")
