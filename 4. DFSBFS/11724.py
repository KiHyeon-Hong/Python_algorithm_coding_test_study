"""
from collections import deque
import sys

input = sys.stdin.readline

def bfs(n, v):
  dq = deque()
  dq.append(n)

  while dq:
    now = dq.popleft()
    chk[now] = True

    for nxt in range(v):
      if adj[now][nxt] == 1 and not chk[nxt]:
        dq.append(nxt)

V, E = map(int, input().split())
adj = [[0] * V for _ in range(V)]

for _ in range(E):
  A, B = map(int, input().split())
  adj[A - 1][B - 1] = 1
  adj[B - 1][A - 1] = 1

chk = [False for _ in range(V)]

ans = 0
for i in range(V):
  if(chk[i]):
    continue
  
  ans += 1
  bfs(i, V)

print(ans)
"""

"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[0] * N for _ in range(N)]

for _ in range(M):
  a, b = map(lambda x: x - 1, map(int, input().split()))
  adj[a][b] = adj[b][a] = 1

chk = [False] * N
ans = 0

def dfs(now):
  for nxt in range(N):
    if adj[now][nxt] and not chk[nxt]:
      chk[nxt] = True
      dfs(nxt)

for i in range(N):
  if not chk[i]:
    ans += 1
    chk[i] = True
    dfs(i)

print(ans)
"""