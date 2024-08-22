# stack
stack = []
stack.append(5)
stack.pop()

# queue
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
print(queue.popleft()) # 왼쪽 원소 pop
print(queue.pop()) # 오른쪽 원소 pop
print(queue)