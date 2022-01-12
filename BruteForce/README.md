# 완전탐색

- 장점: 반드시 답을 찾을 수 있다, 답이 없다면 답이 존재하지 않는다는 의미
- 단점: 오래 걸린다

- trade-off 관계
  - 컴퓨팅 자원과 시간

## BruteForce

- 무차별 대입
- 가장 확실한 방법이라 의외로 많이 사용됨
  - 4색정리 증명에도 사용됨
- 암호학 수학 등 학계에서도, PS에서도 널리 사용되는 알고리즘

## Permutation

- 모든 경우의 수를 순서대로 살펴볼 때 용이하다
- 삼성에서 next_permutation 활용하면 쉽게 풀리는 문제들이 많이 나왔다

```python
from itertools import permutations

v = [0,1,2,3]

for i in permutations(v, 4):
  print(i)
```

```bash
0 1 2 3
0 1 3 2
...
3 2 0 1
3 2 1 0
```

## Combination

- 파이썬은 comination까지 기본으로 제공

```python
from itertools import combinations

v = [0,1,2,3]

for i in combinations(v, 2):
  print(i)
```

```bash
0 1
0 2
0 3
1 2
1 3
2 3
```
