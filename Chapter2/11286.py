# 힙에서 정렬을 위해 정렬 비교를 삽입
# 10만번 입력에 오래 걸림

import heapq as hq
import sys

# input = sys.stdin.readline
# input()

pd = []
for _ in range(int(input())):
  x = int(sys.stdin.readline())
  if x:
    hq.heappush(pd, (abs(x), x)) # 앞 정렬 후 같으면, 뒤 비교
  else:
    # print(hq.heappop(pd) if pd else 0)
    if pd:
      print('>', hq.heappop(pd)[1])
    else:
      print('>', 0)

