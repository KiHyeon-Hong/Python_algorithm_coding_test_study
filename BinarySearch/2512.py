import sys
input = sys.stdin.readline

N = int(input())
C = []

for i in map(int, input().split()):
  C.append(i)
M = int(input())

left = 1
right = max(C)
mid = int(left + right)

