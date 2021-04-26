"""
- 회문(Palindrome)은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 의미함
- 회문을 판별할 수 있는 함수를 리스트 슬라이싱을 활용해서 만드세요
"""
def palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False

print(palindrome("Dave"))
print(palindrome("Asdsa"))
print(palindrome("AbcbA"))