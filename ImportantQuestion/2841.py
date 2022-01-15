import sys
input = sys.stdin.readline

stk = [[0] for _ in range(6)]

N, P = map(int, input().split())

ans = 0

for _ in range(N):
  line, p = map(int, input().split())

  if stk[line - 1][-1] == p:
    continue
  elif stk[line - 1][-1] < p:
    stk[line - 1].append(p)
    ans += 1
  else:
    while stk[line - 1][-1] > p:
      stk[line - 1].pop()
      ans += 1
    
    if stk[line - 1][-1] == p:
      continue
    else:
      stk[line - 1].append(p)
      ans += 1
print(ans)
