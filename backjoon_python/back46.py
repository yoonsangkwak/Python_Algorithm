# 1157번

alphabet = input().upper()
alphabet_list = list(set(alphabet))
alphabet_count = list()

for i in alphabet_list:
    count = alphabet.count(i)
    alphabet_count.append(count)

if (alphabet_count.count(max(alphabet_count)) >= 2):
    print("?")
else:
    print(alphabet_list[(alphabet_count.index(max(alphabet_count)))])