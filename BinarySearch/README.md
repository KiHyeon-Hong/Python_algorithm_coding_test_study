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
