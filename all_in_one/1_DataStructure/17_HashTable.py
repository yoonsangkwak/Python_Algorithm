"""
4. 자료 구조 해쉬 테이블의 장단점과 주요 용도
- 장점
    - 데이터 저장 / 읽기 속도가 빠르다 (검색 속도가 빠르다)
    - 해쉬는 키에 대한 데이터가 있는지 확인이 쉬움 (중복 확인)
- 단점
    - 일반적으로 저장공간이 좀 더 많이 필요하다
    - 여러 키에 해당하는 주소가 동일할 경우 충돌을 해결하기 위한 별도 자료구조가 필요함
- 주요 용도
    - 검색이 많이 필요한 경우
    - 저장, 삭제, 읽기가 빈번한 경우
    - 캐쉬 구현시 (중복 확인이 쉽기 때문)
"""

# 리스트 변수를 활용해서 해쉬 테이블 구현하기
# 1. 해쉬 함수 : key % 8
# 2. 해쉬 키 생성 : hash(data)
hash_table = list([0 for i in range(8)])


def get_key(data):
    return hash(data)


def hash_function(key):
    return key % 8


def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value


def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]


save_data('Dave', '01012341234')
save_data('Andy', '01012345555')
print(read_data('Dave'))
print(hash_table)
