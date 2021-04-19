class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        # head 삭제
        if self.head == None:
            print("해당 값을 가진 노드가 없습니다.")
            return

        # 중간 노드 삭제
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next

    def search_node(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next

# 테스트를 위해 노드 1개 생성
linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

# head가 살아있음을 확인
print(linkedlist1.head)
print()

# head를 지워봄
linkedlist1.delete(0)

# 다음 코드 실행시 아무것도 안나오면 linkedlist1.head가 정상적으로 삭제되었음을 의미
print(linkedlist1.head)

# 다시 하나의 노드를 만들어봄
linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

# 여러 노드를 추가
for data in range(1, 10):
    linkedlist1.add(data)
linkedlist1.desc()
print()

# 노드 중에 한개를 삭제
linkedlist1.delete(4)
linkedlist1.desc()
print()

linkedlist1.delete(9)
linkedlist1.desc()