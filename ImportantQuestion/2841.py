import sys
input = sys.stdin.readline

N, P = map(int, input().split())

A = [list(input().split()) for _ in range(N)]

s = [[P+1] for _ in range(6)]

ans = 0

for i in range(N):
