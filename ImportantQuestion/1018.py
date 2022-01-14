"""
N, M = map(int, input().split())

maps = [input() for _ in range(N)]

# 왼쪽 위 white
chk1 = [[0] * (M - 7) for _ in range(N)]

for i in range(N):
  for j in range(M - 7):
    for k in range(8):
      if (i % 2 == 0) and (j % 2 == 0) or (i % 2 == 1) and (j % 2 == 1):
        if maps[i][j + k] == 'W' and k % 2 == 1 or maps[i][j + k] == 'B' and k % 2 == 0:
          chk1[i][j] += 1
      else:
        if maps[i][j + k] == 'B' and k % 2 == 1 or maps[i][j + k] == 'W' and k % 2 == 0:
          chk1[i][j] += 1

chk2 = [[0] * (M - 7) for _ in range(N)]

for i in range(N):
  for j in range(M - 7):
    for k in range(8):
      if (i % 2 == 0) and (j % 2 == 0) or (i % 2 == 1) and (j % 2 == 1):
        if maps[i][j + k] == 'B' and k % 2 == 1 or maps[i][j + k] == 'W' and k % 2 == 0:
          chk2[i][j] += 1
      else:
        if maps[i][j + k] == 'W' and k % 2 == 1 or maps[i][j + k] == 'B' and k % 2 == 0:
          chk2[i][j] += 1

min = 64

for i in range(len(chk1) - 7):
  for j in range(len(chk1[0])):
    sum = 0
    for k in range(8):
      sum += chk1[i + k][j]
    
    if min > sum:
      min = sum

for i in range(len(chk2) - 7):
  for j in range(len(chk2[0])):
    sum = 0
    for k in range(8):
      sum += chk2[i + k][j]
    
    if min > sum:
      min = sum

print(min)
"""

N, M =  map(int, input().split())
board = [input() for _ in range(N)]

ans = 64

def fill(y, x, bw):
  global ans
  cnt = 0

  for i in range(8):
    for j in range(8):
      if(i + j) % 2:
        if board[y + i][x + j] == bw:
          cnt += 1
      else:
        if board[y + i][x + j] != bw:
          cnt += 1
  ans = min(ans, cnt)

for i in range(N - 7):
  for j in range(M - 7):
    fill(i, j, 'B')
    fill(i, j, 'W')

print(ans)