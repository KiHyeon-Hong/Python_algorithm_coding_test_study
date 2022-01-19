"""
data = input().split(' ')
n, m = int(data[0]), int(data[1])
coin = [int(input()) for _ in range(n)]

cnt = 0
sum = 0
for i in range(n - 1, -1, -1):
  while(coin[i] <= m - sum):
    sum = sum + coin[i]
    cnt = cnt + 1

print(cnt)
"""

N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]
coins.reverse()

ans = 0
for coin in coins:
  ans += K // coin
  K %= coin

print(ans)