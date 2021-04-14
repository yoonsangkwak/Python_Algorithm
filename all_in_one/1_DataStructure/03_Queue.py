"""
# 큐 (Queue)
- 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조
    - 음식점에서 가장 먼저 줄을 선 사람이 가장 먼저 입장하는 것과 동일
    - FIFO(First in, First out) 방식으로 스택과 꺼내는 순서가 반대

- Enqueue : 큐에 데이터를 넣는 기능
- Dequeue : 큐에서 데이터를 꺼내는 기능

파이썬 Queue 라이브러리
- Queue(), LifoQueue(), PriorityQueue() 제공
- Queue() : 가장 일반적인 큐 자료 구조
- LifoQueue() : 나중에 입력된 데이터가 먼저 출력되는 구조 (스택 구조)
- PriorityQueue() : 데이터마다 우선순위를 넣어서, 우선순위가 높은 순으로 데이터 출력

어디에 큐가 많이 쓰일까?
- 멀티 태스킹을 위한 프로세스 스케쥴링 방식을 구현하기 위해 많이 사용됨
"""

# Queue()로 큐 만들기
import queue
data_queue = queue.Queue()
data_queue.put("abc")
data_queue.put(1)
print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())