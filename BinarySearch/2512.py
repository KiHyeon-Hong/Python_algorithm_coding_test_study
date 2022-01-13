import sys
input = sys.stdin.readline

N = int(input())
req = list(map(int, input().split()))
M = int(input())

lo = 0
hi = max(req)
mid = (lo + hi) // 2

ans = 0

def is_possible(mid):
  return sum(min(r, mid) for r in req) <= M

while lo <= hi:
  if is_possible(mid):
    lo = mid + 1
    ans = mid
  else:
    hi = mid - 1

  mid = (lo + hi) // 2

print(ans)