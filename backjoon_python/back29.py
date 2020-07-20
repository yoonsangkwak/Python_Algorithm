# 10988번

palindrome = input("")
check = palindrome[::-1]
if palindrome == check:
    print("1")
else:
    print("0")