"""
import sys
sys.setrecursionlimit(10 ** 7)

MOD = 10007

N, K = map(int, input().split())

cache = [[0] * 1001 for _ in range(1001)]

def bino(n, k):
  if cache[n][k]:
    return cache[n][k]

  if k == 0 or k == n:
    cache[n][k] = 1
  else:
    cache[n][k] = (bino(n - 1, k - 1) + bino(n - 1, k)) % MOD
  return cache[n][k]


print(bino(N, K))
"""

MOD = 10007

N, K = map(int, input().split())
cache = [[0] * 1001 for _ in range(1001)]

for n in range(N + 1):
  for k in range(n + 1):
    if k == 0 or k == n:
      cache[n][k] = 1
    else:
      cache[n][k] = (cache[n - 1][k - 1] + cache[n - 1][k]) % MOD

print(cache[N][K])