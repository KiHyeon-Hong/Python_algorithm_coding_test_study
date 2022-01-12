# Array

- Python에서는 리스트를 사용

```python
arr = [10, 11, 12, 13]
arr[2] = 20
```

# Vector (c++)

- C++에서 코딩테스트에 사용하는 자료형
- 2차원 배열에 자주 사용하는 자료형이다.

# 연결리스트 Linked list

- Python에서는 직접 구현에서 써야 함
- PS에서 별로 안쓰이지만, 다른 자료구조를 구현할 때 많이 사용함
- 삽입 삭제가 빠르고(1), 탐색이 느리다(n)

# Stack

- 삽입과 삭제 o(1)
- FILO
- Python에서는 그냥 리스트로 구현...

```python
s = []

s.append(123)
s.append(456)

while len(s) > 0:
  print(s.pop(-1))  # -1 생략해도 맨뒤에서 출력
```

# Queue

- 삽입과 삭제 o(1)
- LILO
- 리스트를 이용하려면 o(1)을 위해 포인터 변수가 맨뒤를 가리켜야 함

```python
from collections import deque

q = deque()
q.append(123)
q.append(456)
# q.appendleft(456)

print(len(q))

while len(q) > 0:
  # print(q.pop())
  print(q.popleft())

```

```python
from queue import queue
# thread-safe를 고려했기 때문에 속도가 느림
# 코테에서는 사용하지 않음

q = Queue()
q.put(123)
q.put(456)

while q:
  print(q.get())
```

# Priority Queue (Heap)

- 삽입 삭제에 o(logN)
- 최상단에 가장 큰 값이 존재 (max Heap)
- Python에서는 min Heap 제공
- from queue import PriorityQueue도 쓰레드 때문에 속도가 느려 사용하지 않음

```python
import heapq

pd = []

heapq.heappush(pd, 456)
heapq.heappush(pd, 123)
heapq.heappush(pd, 789)

while len(pd) > 0:
  print(heapq.heappop(pd))
```

# Map

- Key, value 쌍을 갖는다.
- Json
- o(1)
- key는 중복이 될 수 없음
- c++에서는 red-black tree로 map이 구현되어 있으며o(logN), python은 hash로 구현되어 있어 o(1)이다.

```python
m = {}
m['a'] = 10
m['b'] = 20

for k in m:
  print(k, m[k])
```

# Set

- 중복이 되지 않는다.
- 삽입과 삭제: o(1)
- c++에서는 o(logN), python에서는 o(1)

```python
s = set()
s.add(123)
s.add(123)
s.add(456)
s.add(789)

# s.remove(456)
# s.clear()

for i in s: # 3
  print(i)
```
