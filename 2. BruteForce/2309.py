"""
from itertools import combinations
import sys

v = []
for _ in range(9):
  v.append(int(sys.stdin.readline()))

for i in combinations(v, 7):
  sum = 0
  for j in i:
    sum = sum + j
  
  if sum == 100:
    print()
    for k in tuple(sorted(i)):
      print(k)
    break
"""

"""
from itertools import combinations

heights = [int(input()) for _ in range(9)]

for combi in combinations(heights, 7):
  if sum(combi) == 100:
    for height in sorted(combi):
      print(height)
    break
"""

# combination 없이 작성
"""
heights = [int(input()) for _ in range(9)]

for i in range(9):
  for j in range(i + 1, 9):
    ... # 7중 for문

for i in range(9):
  for j in range(i + 1, 9):
    # 안뽑힌 7개를 더하는 법도 있다
"""