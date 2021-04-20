"""
Linear Probing 기법
- 폐쇄 해싱 또는 Closed Hashing 기법 중 하나 : 해쉬 테이블 저장공간 안에서 충돌 문제를 해결하는 기법
- 충돌이 일어나면 , 해당 Hash address의 다음 address부터 맨 처음 나오는 빈 공간에 저장하는 기법
    - 저장공간 활용도를 높이기 위한 기법
"""

# 해쉬 테이블 코드에 Linear Probing 기법으로 충돌해결 코드 추가해보기
hash_table = list([0 for i in range(8)])


def get_key(data):
    return hash(data)


def hash_function(key):
    return key % 8


def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value
                return
    else:
        hash_table[hash_address] = [index_key, value]


def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None


save_data('Dd', '01012341234')
save_data('Dg', '01012345555')
save_data('any', '01012346666')
print(read_data('Dd'))
print(hash_table)
