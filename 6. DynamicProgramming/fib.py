"""
N = int(input())

def fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  return fib(n - 1) + fib(n - 2)

print(fib(N))
"""
"""
N = int(input())

arr = [0, 1]

def fib(n):
  for i in range(2, N + 1):
    arr.append(arr[i - 1] + arr[i - 2])
  return arr[-1]

print(fib(N))
"""

N = int(input())

cache = [-1] * 91
cache[0] = 0
cache[1] = 1

def f(n):
  if cache[n] == -1:
    cache[n] = f(n - 1) + f(n - 2)
  return cache[n]

print(f(N))