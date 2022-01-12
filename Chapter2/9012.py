# 올바른 괄호쌍 문제는 전형적인 Stack을 이용하는 문제이다.

for _ in range(int(input())):
  stk = []
  isVPS = True

  for ch in input():
    if ch == '(':
      stk.append(ch)
    else:
      if len(stk) == 0:
        isVPS = False
        break
      stk.pop()
  
  if len(stk) > 0:
    isVPS = False
  
  print('YES' if isVPS else 'NO')