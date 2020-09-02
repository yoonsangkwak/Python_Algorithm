# 1316번

n = int(input())
word_list = []
group_word = n
check = True
for i in range(n):
    word_list.append(input())

for i in range(len(word_list)):
    check = True
    for j in range(len(word_list[i])):
        for k in range(j+1, len(word_list[i])):
            if word_list[i][k] != word_list[i][j]:
                if word_list[i][j] in word_list[i][k+1:]:
                    group_word -= 1
                    check = False
                    break
        if check == False:
            break

print(group_word)