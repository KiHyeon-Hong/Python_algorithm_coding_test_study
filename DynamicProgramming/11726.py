"""
import sys
sys.setrecursionlimit(10 ** 7)

MOD = 10007

N = int(input())

cache = [0, 1, 2]

def fib(N):
  if N >= len(cache):
    cache.append((fib(N -1) + fib(N - 2)) % MOD)
  return cache[N]

print(fib(N))
"""

MOD = 10_007
dp = [0] * 1001
dp[1] = 1
dp[2] = 2

n = int(input())
for i in range(3, 1001):
  dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

print(dp[n])