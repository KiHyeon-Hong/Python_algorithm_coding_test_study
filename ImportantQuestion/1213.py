c = dict()
s = input()

for ch in s:
  if ch in c:
    c[ch] += 1
  else:
    c[ch] = 1

if sum(i % 2 for i in c.values()) > 1:
  print("I'm Sorry Hansoo")
else:
  half = ''

  for k, v in sorted(c.items()):
    half += k * (v // 2)
  
  ans = half
  for k, v in c.items():
    if v % 2:
      ans += k
  
  ans += ''.join(reversed(half))
  print(ans)