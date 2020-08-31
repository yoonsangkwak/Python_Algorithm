# 2941번

word = input()
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
count = 0

for i in range(len(croatia)):
    if croatia[i] in word:
        word_count = word.count(croatia[i])
        word = word.replace(croatia[i], " ")
        count += word_count

word = word.replace(" ", "")
count += len(word)
print(count)