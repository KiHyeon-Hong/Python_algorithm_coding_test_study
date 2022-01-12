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
"""