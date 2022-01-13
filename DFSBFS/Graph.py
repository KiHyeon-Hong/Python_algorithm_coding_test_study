# 파이썬에서는 그래프를 기본 자료 구조로 제공하지 않는다.
from collections import deque

adj = [[0] * 13 for _ in range(13)]

adj[0][1] = adj[0][7] = adj[1][9] = adj[7][10] = 1

for row in adj:
  print(row)

def dfs(now):
  print(now)
  for nxt in range(13):
    if adj[now][nxt]:
      dfs(nxt)

dfs(0)

def bfs():
  dq = deque()
  dq.append(0)

  while dq:
    now = dq.popleft()
    print(now)
    for nxt in range(13):
      if adj[now][nxt]:
        dq.append(nxt)

bfs()