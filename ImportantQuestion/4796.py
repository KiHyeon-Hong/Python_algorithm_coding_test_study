import sys
input = sys.stdin.readline

ans = []

while True:
  L, P, V = map(int, input().split())

  if L == 0 and P == 0 and V == 0:
    break
  
  camp = (V // P) * L
  camp += min(L, V % P)

  ans.append(camp)

for i in range(len(ans)):
  print(f'Case {i + 1}: {ans[i]}')