# 📚 Day 18 파이썬 심화 — 이진탐색 + DFS / BFS

---

## 1️⃣ 이진탐색 (Binary Search)

### 핵심 개념

```
정렬된 데이터에서 절반씩 줄여가며 탐색
시간복잡도: O(log n)

핵심 조건 — 규칙성(단조성) 이 있어야 사용 가능
"mid 를 기준으로 한쪽을 확실히 제거할 수 있는가?"

오름차순 정렬  → 기본 케이스
내림차순 정렬  → 조건만 반대로
정렬 없어도    → 단조성 있으면 가능 (제곱근, 파라메트릭 서치 등)
```

### 기본 구현

```python
def binary_search(nums: list, target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid          # 찾으면 인덱스 반환
        elif nums[mid] < target:
            left = mid + 1      # 오른쪽 탐색
        else:
            right = mid - 1     # 왼쪽 탐색

    return -1   # 없으면 -1 반환
```

### bisect 모듈

```python
import bisect

nums = [1, 3, 5, 7, 9]

bisect.bisect_left(nums, 5)    # 2 ← 5의 왼쪽 위치
bisect.bisect_right(nums, 5)   # 3 ← 5의 오른쪽 위치

# 개수 구하기
bisect.bisect_right(nums, target) - bisect.bisect_left(nums, target)

# 존재 확인
def contains(nums, target):
    i = bisect.bisect_left(nums, target)
    return i < len(nums) and nums[i] == target
    # i < len(nums) 먼저 확인 → IndexError 방지 (단락 평가)
```

### 가장 가까운 값

```python
def closest_value(nums, target):
    i = bisect.bisect_left(nums, target)

    if i == 0: return nums[0]       # 왼쪽 없음
    if i == len(nums): return nums[-1]  # 오른쪽 없음

    left_val  = nums[i - 1]
    right_val = nums[i]

    if abs(target - left_val) <= abs(target - right_val):
        return left_val
    return right_val
```

### 파라메트릭 서치

```python
# 합이 target 이상이 되는 최소 원소 개수
def min_count(nums, target):
    nums.sort(reverse=True)      # 큰 수부터 정렬
    left, right = 1, len(nums)   # 인덱스 아닌 개수 기준
    result = len(nums)

    while left <= right:
        mid = (left + right) // 2
        total = sum(nums[:mid])

        if total >= target:
            result = mid
            right = mid - 1     # 더 적은 개수로 가능한지
        else:
            left = mid + 1      # 개수 부족 → 늘리기

    return result

# left, right = 인덱스가 아니라 "개수" 기준
# 이진탐색은 인덱스뿐만 아니라 탐색 범위가 되는 어떤 값이든 가능
```

---

## 2️⃣ DFS (깊이 우선 탐색)

### 핵심 개념

```
한 방향으로 끝까지 파고들다가 막히면 돌아오는 방식
스택 / 재귀 로 구현
활용 — 경로 탐색, 연결된 영역 크기, 사이클 감지
```

### 그래프 표현

```python
# 인접 리스트 — 가장 많이 씀
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}
```

### 재귀 구현

```python
def dfs(graph, node, visited):
    visited.add(node)             # 방문 처리
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:   # 방문 안 한 이웃만
            dfs(graph, neighbor, visited)

dfs(graph, 1, set())   # 1 2 4 5 3
```

### 실행 흐름

```
dfs(1) → visited={1}, 출력: 1
  dfs(2) → visited={1,2}, 출력: 2
    dfs(4) → visited={1,2,4}, 출력: 4
      이웃 [2] → 이미 방문 → 종료
    dfs(5) → visited={1,2,4,5}, 출력: 5
      이웃 [2] → 이미 방문 → 종료
  dfs(3) → visited={1,2,4,5,3}, 출력: 3
    이웃 [1] → 이미 방문 → 종료
결과: 1 2 4 5 3
```

### visited 가 필요한 이유

```python
# visited 없으면
dfs(1) → dfs(2) → dfs(1) → dfs(2) → ...   # 무한루프 ❌

# visited 있으면
dfs(1) → dfs(2) → dfs(1) 시도 → 이미 방문 → 스킵 ✅
```

---

## 3️⃣ BFS (너비 우선 탐색)

### 핵심 개념

```
가까운 노드부터 차례대로 탐색
큐 로 구현
활용 — 최단 거리, 레벨 탐색
```

### 구현

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)        # 큐에 넣을 때 방문 처리 (중복 방지)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)     # 큐에 넣기 전에 방문 처리
                queue.append(neighbor)

bfs(graph, 1)   # 1 2 3 4 5
```

### 실행 흐름

```
초기: queue=[1], visited={1}

1번째: node=1, 출력: 1
  이웃 [2,3] → queue=[2,3], visited={1,2,3}

2번째: node=2, 출력: 2
  이웃 [1,4,5] → 1 스킵 → queue=[3,4,5]

3번째: node=3, 출력: 3
  이웃 [1] → 스킵

4번째: node=4, 출력: 4
5번째: node=5, 출력: 5

결과: 1 2 3 4 5
```

### BFS 최단 거리

```python
def bfs_shortest(graph, start, end):
    visited = {start: 0}    # dict — 방문 여부 + 거리 동시 저장
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node == end:
            return visited[end]

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited[neighbor] = visited[node] + 1   # 거리 + 1
                queue.append(neighbor)

    return -1

# visited 를 set 대신 dict 쓰는 이유
# set  → 방문 여부만 저장
# dict → 방문 여부 + 거리 동시 저장
```

---

## 4️⃣ 2차원 배열 DFS

### 핵심 개념

```
영역 = 상하좌우로 연결된 1들의 덩어리
     = 0으로 분리된 1의 집합
     = 한 번의 DFS로 전부 방문할 수 있는 1들

대각선은 연결 안 됨 — 상하좌우만 연결
```

### 상하좌우 이동

```python
dx = [-1, 1, 0, 0]   # 상, 하, 좌, 우
dy = [0, 0, -1, 1]

# i=0 → (-1, 0) 위
# i=1 → (1, 0)  아래
# i=2 → (0, -1) 왼쪽
# i=3 → (0, 1)  오른쪽
```

### 연결된 영역 크기 구하기

```python
def dfs_2d(graph, x, y, visited):
    if x < 0 or x >= len(graph): return 0     # 경계 체크
    if y < 0 or y >= len(graph[0]): return 0  # 경계 체크
    if visited[x][y] or graph[x][y] == 0: return 0  # 방문 or 벽

    visited[x][y] = True
    count = 1              # 현재 칸

    for i in range(4):
        count += dfs_2d(graph, x + dx[i], y + dy[i], visited)

    return count

# return 0 → 그 방향만 종료, 나머지 방향은 계속 탐색
# 4방향이 각각 독립적으로 호출되고 count 에 합산
```

### 영역 개수 구하기

```python
def count_areas(graph):
    rows, cols = len(graph), len(graph[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0

    for x in range(rows):
        for y in range(cols):
            if graph[x][y] == 1 and not visited[x][y]:
                dfs_2d(graph, x, y, visited)   # 연결된 1 전부 방문
                count += 1                     # 새 영역 발견!

    return count
```

---

## 5️⃣ DFS vs BFS 한눈에 비교

```
DFS                         BFS
재귀 / 스택 사용             큐 사용
깊이 우선                    너비 우선
멀리 있는 것 먼저            가까운 것 먼저
경로 탐색, 영역 크기          최단 거리, 레벨 탐색
1 2 4 5 3                   1 2 3 4 5
```

---

## ✅ 오늘 주의사항

```python
# 1. visited 필수 — 없으면 무한루프
visited = set()         # 1차원 그래프
visited = [[False]...]  # 2차원 배열

# 2. BFS — 큐에 넣을 때 visited 처리
visited.add(neighbor)   # ✅ 넣기 전에
queue.append(neighbor)
# 꺼낼 때 처리하면 같은 노드 중복 입장 가능 ❌

# 3. bisect — IndexError 방지
return i < len(nums) and nums[i] == target
# i < len(nums) 먼저 → 단락 평가로 nums[i] 접근 방지

# 4. 파라메트릭 서치 — left, right 는 개수 기준
left, right = 1, len(nums)   # 인덱스 아님!

# 5. 2차원 배열 DFS
# return 0 → 그 방향만 종료 (전체 종료 아님)
# 4방향 각각 독립 호출 → count 에 합산
```
