"""
빈번한 충돌을 개선하는 기법
- 해쉬 함수를 재정의 및 해쉬 테이블 저장공간을 확대

참고 : 해쉬 함수와 키 생성 함수
- 파이썬의 hash() 함수는 실행할 때 마다, 값이 달라질 수 있음
- 유명한 해쉬 함수들이 있음 : SHA (Secure Hash Algorithm, 안전한 해시 알고리즘)
    - 어떤 데이터도 유일한 고정된 크기의 고정값을 리턴해주므로, 해쉬 함수로 유용하게 활용 가능
"""

# SHA-1
import hashlib

data = 'test'.encode()
hash_object = hashlib.sha1()
hash_object.update(b'test')
hex_dig = hash_object.hexdigest()
print(hex_dig)

# SHA-256
data = 'test'.encode()
hash_object = hashlib.sha256()
hash_object.update(b'test')
hex_dig = hash_object.hexdigest()
print(hex_dig)