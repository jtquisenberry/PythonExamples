from collections import deque

d = deque()
d.append(1)
d.append(2)
d.append(3)
d.pop()
print(list(d))

d.extend([4,5,6])
print(list(d))

d.appendleft(7)
print(list(d))


# print(list(d))
d.extendleft([8,9,10])
print(list(d))

d.extendleft(deque([11,12,13]))
print(list(d))

d.popleft()
print(list(d))


