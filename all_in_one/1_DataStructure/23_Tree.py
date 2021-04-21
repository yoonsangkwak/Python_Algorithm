"""
5.4 이진 탐색 트리 삭제
- 매우 복잡함. 경우를 나누어서 이해하는 것이 좋음

- Leaf Node 삭제
    - Leaf Node : Child Node가 없는 Node
    - 삭제할 Node의 Parent Node가 삭제할 Node를 가리키지 않도록 한다.

- Child Node가 하나인 Node 삭제
    - 삭제할 Node의 Parent Node가 삭제할 Node의 Child Node를 가리키도록 한다.

- Child Node가 두 개인 Node 삭제
    1) 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 삭제할 Node의 Parent Node가 가리키도록 한다.
    2) 삭제할 Node의 왼쪽 자식 중, 가장 큰 값을 삭제할 Node의 Parent Node가 가리키도록 한다.

    1) 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 삭제할 Node의 Parent Node가 가리키게 할 경우
    - 삭제할 Node의 오른쪽 자식 선택
    - 오른쪽 자식의 가장 왼쪽에 있는 Node를 선택
    - 해당 Node를 삭제할 Node의 Parent Node의 왼쪽 Branch가 가리키게 함
    - 해당 Node의 왼쪽 Branch가 삭제할 Node의 왼쪽 Child Node를 가리키게 함
    - 해당 Node의 오른쪽 Branch가 삭제할 Node의 오른쪽 Child Node를 가리키게 함
    - 만약 해당 Node가 오른쪽 Child Node를 가지고 있었을 경우에는,
        해당 Node의 본래 Parent Node의 왼쪽 Branch가 해당 오른쪽 Child Node를 가리키게 함

5.5 이진 탐색 트리 삭제 코드 구현과 분석
1) 삭제할 Node 탐색
- 삭제할 Node가 없는 경우도 처리해야 함
    - 이를 위해 삭제할 Node가 없는 경우는 False를 리턴하고, 함수를 종료 시킴
"""

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

    def delete(self, value):
        searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        if searched == False:
            return False

        # 이후부터 Case들을 분리해서, 코드 작성
        # Case 1 : 삭제할 Node가 Leaf Node인 경우
        # self.current_node가 삭제할 Node, self.parent는 삭제할 Node의 Parent Node
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node

        # Case 2 : 삭제할 Node가 Child Node를 한 개 가지고 있을 경우
        # 왼쪽에만 Node가 있는 경우
        if self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
        # 오른쪽에만 Node가 있는 경우
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        # Case 3-1 : 삭제할 Node가 Child Node를 두 개 가지고 있을 경우
        if self.current_node.left != None and self.current_node.right != None:
            # 3-1-1) 삭제할 Node가 Parent Node 왼쪽에 있을 때
            if value < self.parent.value:
                self.change_node = self.current_node.right
                self.change_node.parent = self.current_node
                while self.change_node.left != None:
                    self.change_node.parent = self.change_node
                    self.change_node = self.change_node.left
                self.change_node.parent.left = None
                if self.change_node.right != None:
                    self.change_node.parent.left = self.change_node.right
                else:
                    self.change_node.parent.left = None
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left

        # Case 3-2 : 삭제할 Node가 Child Node를 두 개 가지고 있을 경우
            # 3-2-1) 삭제할 Node가 Parent Node 오른쪽에 있을 때
            else:
                self.change_node = self.current_node.right
                self.change_node.parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node.parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node.parent.left = self.change_node.right
                else:
                    self.change_node.parent.left = self.change_node.right
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right
        return True