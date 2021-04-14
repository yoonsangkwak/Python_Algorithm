import queue

data_queue = queue.PriorityQueue()
# 우선순위가 숫자상으로 낮으면 Head, 높으면 Tail

data_queue.put((10, "Korea"))
data_queue.put((5, 1))
data_queue.put((15, "ho"))
print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())