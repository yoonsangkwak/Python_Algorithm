"""
1. 트리 (Tree) 구조
- 트리 : Node와 Branch를 이용해서, 사이클을 이루지 않도록 구성한 데이터 구조
- 실제로 어디에 많이 사용되나?
    - 트리 중 이진 트리 (Binary Tree) 형태의 구조로, 탐색 (검색) 알고리즘 구현을 위해 많이 사용됨

2. 알아둘 용어
- Node : 트리에서 데이터를 저장하는 기본 요소 (데이터와 다른 연결된 노드에 대한 Branch 정보 포함)
- Root Node : 트리 맨 위에 있는 노드
- Level : 최상위 노드를 Level 0 으로 하였을 때, 하위 Branch로 연결된 노드의 길이를 나타냄
- Parent Node : 어떤 노드의 다음 레벨에 연결된 노드
- Child Node : 어떤 노드의 상위 레벨에 연결된 노드
- Leaf Node (Terminal Node) : Child Node가 하나도 없는 노드
- Sibling (Brother Node) : 동일한 Parent Node를 가진 노드
- Depth : 트리에서 Node가 가질 수 있는 최대 Level

3. 이진 트리 (Binary Tree) 와 이진 탐색 트리 (Binary Search Tree)
- 이진 트리 : 노드의 최대 Branch가 2인 트리
- 이진 탐색 트리 : 이진 트리에 다음과 같은 추가적인 조건이 있는 트리
    - 왼쪽 노드는 해당 노드보다 작은 갑스 오른쪽 노드는 해당 노드보다 큰 값을 가지고 있음

4. 자료 구조 이진 탐색 트리의 장점과 주요 용도
- 주요 용도 : 데이터 검색 (탐색)
- 장점 : 탐색 속도를 개선할 수 있음
"""

# 이진 탐색 트리
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class NodeMgmt:
    def __init__(self, head):
        self.head = head

    # 이진 탐색 트리 삽입
    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    # 이진 탐색 트리 탐색
    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False


head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)
BST.insert(8)
print(BST.search(8))
print(BST.search(-4))
