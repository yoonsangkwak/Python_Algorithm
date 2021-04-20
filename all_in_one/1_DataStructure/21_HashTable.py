"""
해쉬 알고리즘 시간 복잡도
- 일반적인 경우 (Collision이 없는 경우) O(1)
- 최악의 경우 (Collision이 모두 발생한 경우) O(n)
- 해쉬 테이블의 경우, 일반적인 경우를 기대하고 만들기 때문에 시간복잡도는 O(1)이라고 말할 수 있음

검색에서 해쉬 테이블의 사용 예
- 16개의 배열에 데이터를 저장하고, 검색할 때 : O(n)
- 16개의 데이터 저장공간을 가진 위의 해쉬 테이블에 데이터를 저장하고, 검색할 때 : O(1)
"""

# Chaining 기법을 적용한 해쉬 테이블 코드에 키 생성 함수를 sha256 해쉬 알고리즘으로 변경

import hashlib

hash_table = list([0 for i in range(8)])


def get_key(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16)


def hash_function(key):
    return key % 8


def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = [[index_key, value]]


def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None
    return hash_table[hash_address]


print(get_key('db') % 8)
print(get_key('da') % 8)
print(get_key('dh') % 8)

save_data('da', '01012341234')
save_data('dh', '01012345555')
print(read_data('da'))
print(read_data('dh'))