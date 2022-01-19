# 카드2

"""
from collections import deque

q = deque()
for _ in range(int(input())):
  q.append(_ + 1)

while len(q) != 1:
  q.popleft()
  q.append(q.popleft())

print(q.popleft())
"""

"""
from collections import deque

dp = depue()
N = int(input())

for i in range(1, N + 1):
  dp.append(i)

while len(dp) > 1:
  dp.popleft()
  dp.append(dp.popleft())

print(dp.popleft())
"""

# 배열로 풀기 (시간이 매우 오래 걸림)

N = int(input())
arr = [*range(1, N + 1)]

while len(arr) > 1:
  arr.pop(0)
  arr.append(arr.pop(0))

print(arr[0])
