# 2920번

check_list = list(map(int, input().split()))
ascending = sorted(check_list)
descending = sorted(check_list, reverse=True)

if check_list == ascending:
    print("ascending")
elif check_list == descending:
    print("descending")
else:
    print("mixed")