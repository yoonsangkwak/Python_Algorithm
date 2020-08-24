# 2798번

n, m = map(int, input().split())

card_list = list(map(int, input().split()))
card_sum = 0

for i in range(0, len(card_list)-2):
    for j in range(i+1, len(card_list)-1):
        for k in range(j+1, len(card_list)):
            if card_list[i] + card_list[j] + card_list[k] > m:
                continue
            else:
                card_sum = max(card_sum, card_list[i] + card_list[j] + card_list[k])

print(card_sum)