"""
# 힙 (Heap)
- 힙 : 데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리 (Complete Binary Tree)
    - 완전 이진 트리 : 노드를 삽입할 때 최하단 왼쪽 노드부터 차례대로 삽입하는 트리

- 힙을 사용하는 이유
    - 배열에 데이터를 넣고, 최대값과 최소값을 찾으려면 O(n)이 걸림
    - 이에 반해, 힙에 데이터를 넣고, 최대값과 최소값을 찾으면, O(logn)이 걸림
    - 우선순위 큐와 같이 최대값 또는 최소값을 빠르게 찾아야 하는 자료구조 및 알고리즘 구현에 사용됨

2. 힙 (Heap) 구조
- 힙은 최대값을 구하기 위한 구조(최대 힙)와, 최소값을 구하기 위한 구조(최소 힙)로 분류할 수 있음
- 힙은 다음과 같이 두 가지 조건을 가지고 있는 자료구조
    1) 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 같다. (최대 힙의 경우)
        - 최소 힙의 경우는 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 작음
    2) 완전 이진 트리 형태를 가짐

- 힙과 이진 탐색 트리의 공통점과 차이점
    - 공통점 : 힙과 이진 탐색 트리는 모두 이진 트리임
    - 차이점:
        - 힙은 각 노드의 값이 자식 노드보다 크거나 같음 (Max Heap의 경우)
        - 이진 탐색 트리는 왼쪽 자식 노드의 값이 가장 작고, 그 다음 부모 노드,
            그 다음 오른쪽 자식 노드 값이 가장 큼
        - 힙은 이진 탐색 트리의 조건인 자식 노드에서 작은 값은 왼쪽, 큰 값은 오른쪽이라는 조건은 없음
            - 힙의 왼쪽 및 오른쪽 자식 노드의 값은 오른쪽이 클 수도 있고, 왼쪽이 클 수도 있음
        - 이진 탐색트리는 탐색을 위한 구조, 힙은 최대/최소값 검색을 위한 구조 중 하나로 이해하면 됨

3. 힙 (Heap) 동작
- 힙에 데이터 삽입하기 - 기본 동작
    - 힙은 완전 이진 트리이므로, 삽입할 노드는 기본적으로 왼쪽 최하단부 노드부터 채워지는 형태로 삽입
- 힙에 데이터 삽입하기 - 삽입할 데이터가 힙의 데이터보다 클 경우 (Max Heap의 예)
    - 먼저 삽입된 데이터는 완전 이진 트리 구조에 맞추어, 최하단부 왼쪽 노드부터 채워짐
    - 채워진 노드 위치에서, 부모 노드보다 값이 클 경우, 부모 노드와 위치를 바꿔주는 작업을 반복함 (swap)
- 힙의 데이터 삭제하기 (Max Heap의 예)
    - 보통 삭제는 최상단 노드 (root 노드)를 삭제하는 것이 일반적임
        - 힙의 용도는 최대값 또는 최소값을 root 노드에 놓아서, 바로 꺼내 쓸 수 있도록 하는 것임
    - 상단의 데이터 삭제시, 가장 최하단부 왼쪽에 위치한 노드
        (일반적으로 가장 마지막에 추가한 노드)를 root 노드로 이동
    - root 노드의 값이 child node보다 작을 경우, root 노드의 child node 중
        가장 큰 값을 노드와 root 노드 위치를 바꿔주는 작업을 반복함 (swap)

4. 힙 구현
- 힙과 배열
    - 일반적으로 힙 구현시 배열 자료구조를 활용함
    - 배열은 인덱스가 0번부터 시작하지만, 힙 구현의 편의를 위해,
        root 노드 인덱스 번호를 1로 지정하면, 구현이 좀 더 수월함
        - 부모 노드 인덱스 번호 = 자식 노드 인덱스 번호 // 2
        - 왼쪽 자식 노드 인덱스 번호 = 부모 노드 인덱스 번호 * 2
        - 오른쪽 자식 노드 인덱스 번호 = 부모 노드 인덱스 번호 * 2 + 1
"""


class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self, inserted_idx):
        # root 노드일 경우
        if inserted_idx <= 1:
            return False

        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self, data):
        # root 노드가 없을 경우
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)

        inserted_idx = len(self.heap_array) - 1

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[
                inserted_idx]
            inserted_idx = parent_idx

        return True


heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)
