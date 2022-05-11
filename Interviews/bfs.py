from collections import deque

d = deque()

d.append(1)
d.append(2)
d.append(3)

print(d)

d.popleft()
d.pop()

print(d)
print(list(d))