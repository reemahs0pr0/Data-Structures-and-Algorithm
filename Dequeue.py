import collections

q = collections.deque([23, 45, 23, 12, 5, 76, 68, 3, 56])

q.append(99)
print(q)

q.appendleft(55)
print(q)

q.pop()
print(q)

q.popleft()
print(q)