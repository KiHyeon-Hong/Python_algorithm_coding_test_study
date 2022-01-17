from bisect import bisect_left, bisect_right

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
qry = list(map(int, input().split()))

ans = []
for q in qry:
  l = bisect_left(cards, q)
  r = bisect_right(cards, q)

  if r - l > 0:
    ans.append(1)
  else:
    ans.append(0)

print(*ans)



"""
import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

H.sort()

ans = []
for i in range(M):
  start = 0
  finish = N - 1
  mid = (start + finish) // 2
  
  chk = False
  while start <= finish:
    if H[mid] == C[i]:
      chk = True
      ans.append(1)
      break
    elif H[mid] < C[i]:
      start = mid + 1
      mid = (start + finish) // 2
    else:
      finish = mid - 1
      mid = (start + finish) // 2
    print(start, finish)

  if not chk:
    ans.append(0)

print(' '.join(map(str, ans)))
"""