# Binary Search

- 탐색 전에 반드시 정렬이 되어 있어야 한다
- 살펴보는 범위를 절반 씩 줄여가면서 답을 찾는다
- 미리 정렬되어 들어오면 이진 탐색만 하면 되므로 o(logN)

- 탐색을 1번 할 때는 선형탐색이 나을수도 있지만, 탐색을 N번 해야 할 때는 오히러 정렬을 한 후 이진탐색이 빠를 수도 있다

```python
from bisect import bisect_left, bisect_right

v = (0,1,2,3,3,3,4,5,6,7,8,9)

three = bisect_right(v, 3) - bisect_left(v, 3)

print(three)  # 3개
```

# 파라메트릭 서치

- 최적화 문제를 결정 문제로 바꿔서 이진탐색으로 푸는 방법이다.

## 최적화문제(Optimization Problem)

- 문제 상황을 만족하는 변수의 최솟값, 최댓값을 구하는 문제

## 결정문제(Decision Problem)

- Yes or No Problem

## 파라메트릭 서치

- 매개변수가 주어지면 true, false가 결정되어야 함
- 가능한 해의 영역이 연속적
- 범위를 반씩 줄여가면서 가운데 값이 true인지 false인지 구한다
- 이진 탐색과 똑같은 원리이다

- 알고리즘 문제로 자주 나온다
- 이진 탐색보다는 파라메트릭 서치가 많이 나온다
- 다른 알고리즘과 결합해서 출제가 좋음
- true, false 구하는 함수 이용?
- true, fasle 핵심 부분 구성하는 방법이 알고리즘 문제이다? (시뮬레이션 etc...)
