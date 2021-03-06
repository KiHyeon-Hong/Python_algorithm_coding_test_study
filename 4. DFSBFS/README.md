# Graph

- VCS (Version control system)도 그래프의 한 사례이다.

- Vertex(node)
- edge
- V, E로 표현할 때가 많다

- 무방향 그래프, 방향 그래프
- 양방향 그래프는 무방향 그래프와 동일하다
- 순환 그래프(사이클이 존재한다), 비순환 그래프

- 방향성 비순환 그래프는 DAG(Directed Acyclic Graph)이 자주 사용된다

- 연결 요소: Connected Component
- 떨어진 3개가 하나의 그래프일 수도 있다. 연결요소가 3개이다.

# Tree

- 순환성이 없는 무방향 그래프 = 사이클이 없다.
- 특정하지 않는 한 어떤 노드든지 루트가 될 수 있다
- 가장 바깥쪽 노드는 leaf node
- node A에서 node B로 가는 경로는 반드시 존재하며, 유일하다
- 노드 개수 = 간선 개수 + 1

- 자료구조에서 트리는 부모 자식 관계가 있는 방향 그래프이다.
- 루트는 하나이다

# 인접행렬

- 행은 시작 인덱스, 열을 도착 인덱스를 의미한다
- 무방향 그래프는 대각선을 기준으로 대칭이 된다.

# 인접리스트

- 인접리스트에서는 간선이 있는 부분에서만 할당이 된다.
- C++에서는 벡터, 파이썬에서는 리스트를 이용한다.

# 인접행렬(시간 유리) VS 인접리스트(공간 유리)

- 인접행렬이 공간을 더욱 많이 차지한다.
- 인접행렬은 탐색 시간에 유리하다. 임의의 접근을 이용하여 바로 접근이 가능
- 인접리스트에서는 하나하나 찾아야된다

# DFS

- 스택과 재귀를 사용해서 구현한다

# BFS

- 큐를 사용해서 구현한다

# DFS & BFS

## 공통점

- 모든 경우의 수를 살펴본다, 완전탐색이다.
-

## 차이점

- 탐색 순서가 다르다
- 최단 거리 탐색은 BFS를 사용하는 것이 유리할 때가 많다

## Big_o

- 인접행렬: o(V^2) // 재귀함수로 for문 돌면서.... 하므로 V만큼 전부 돌기 때문에...
- 인접리스트: o(V + E) // 모든 정점을 돌아야 하지만, 모든 간선도 살펴본다

# 길찾기 문제

- 보통 상하좌우 4개의 방향이 많으며, 방향값을 미리 코드에 짜두고 for문으로 순회하는 기법을 반드시 익히자

```c++
// c++
const int dy[4] = {0, 1, 0, -1};  // 행렬이므로 보기 쉽게 y, x 순으로 했다
const int dx[4] = {1, 0, -1, 0};  // 상대 좌표 값을 저장해서 다음 좌표를 구하는 방법이다

int N;
bool chk[100][100];

bool isValidCoord(int y, int x) { // 범위 체크
  return 0 <= y && y < N && 0 <= x && x <= N;
}

void dfs(int y, int x) {
  chk[y][x] = true;

  for(int k = 0; k < 4; ++k) {
    int ny = y + dy[k];
    int nx = x + dx[k];

    if(isValidCoord(ny, nx) && !chk[ny][nx])  // 범위 안쪽 && 아직 탐색 안함
      dfs(by, nx);
  }
}
```

- 방문 체크 필요
- 각 칸이 노드
- 상하좌우 4방향으 간선

```python
# python
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
chk = [[False] * 100 for _ in range(100)]
N = int(input())

def is_valid_coord(y, x):
  return 0 <= y < N and 0 <= x <= N


def fs(start_y, start_x):
  q = deque()
  q.append((start_y, start_x))

  while len(q) > 0:
    y, x = q.popleft()
    chk[y][x] = True
    for k in range(4):
      ny = y + dy[k]
      nx = x + dx[k]

      if is_valid_coord(ny, nx) and not chk[ny][nx]:
        q.append((ny, nx))
```

- dy, dx 안쓰고도 구현은 가능하지만, 코드가 길어지며, 코딩 실수가 날 수 있다

# Backtracking

- 퇴각검색
- 기본적으로 모든 경우를 탐색하며, 방법은 DFS,BFS와 유사하다
- 백트래킹은 가지치기를 통해 탐색 경우의 수를 줄인다는 차이가 있다

  - 최악의 경우 모든 경우를 다 살펴보지만, 가능한 덜 보겠다는 전략이다
  - 가망성이 없으면 가지 않는다

# 정리

- 그래프는 node, edge로 이루어짐
- 방향성과 순환성이 각각 있거나 없거나
  - 둘 다 없으면 트리
- 구현방법

  - 인접행렬: edge가 많은 그래프일 때 사용, edge 탐색이 빠름
  - 인접리스트: edge가 적은 그래프일 때 사용, 메모리를 적게 사용

- DFS, BFS, 백트래킹은 전부 완전 탐색 알고리즘
  - 최악의 경우 모든 노드를 탐색하는 건 동일함
- 최단거리를 구할 때는 BFS를 사용
- DFS는 재귀와 스택, BFS는 큐로 구현
- 가지치기를 하면 백트래킹
