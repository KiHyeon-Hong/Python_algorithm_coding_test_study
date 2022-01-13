"""
N, T = map(int, input().split())
Temp = input().split()
G = [int(Temp[i]) for i in range(N)]
G.sort()

ans = 0
ck = -1
for i in range(N):
  if (ck <= G[i]):
    ans += 1
    ck = G[i] + T

print(ans)
"""

N, L = map(int, input().split())
coord = [False] * 1001

x = 0
ans = 0

for i in map(int, input().split()):
  coord[i] = True

while x < 1001:
  if coord[x]:
    ans += 1
    x += L
  else:
    x += 1

print(ans)