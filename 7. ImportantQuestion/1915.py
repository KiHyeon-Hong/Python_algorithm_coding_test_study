# DP(i, j): i, j칸을 우하단으로 하는 정사각형 최대 크기
# 점화식은 DP(i, j) = DP(i-1, j), DP(i, j-1), DP(i-1, j-1)의 최솟값 + 1이며, DP(i, j) = 1 일때

n, m = map(int, input().split())
arr = [input() for _ in range(n)]
dp = [[0] * m for _ in range(n)]

for i in range(n):
  if arr[0][i] == '1':
    dp[0][i] = 1
  if arr[i][0] == '1':
    dp[i][0] = 1

for i in range(n):
  for j in range(m):
    if arr[i][j] == '1':
      dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

ans = 0
for i in range(n):
  for j in range(m):
    ans = max(ans, dp[i][j])

print(ans ** 2)
