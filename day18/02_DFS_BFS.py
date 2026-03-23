# DFS / BFS
# 1. 그래프란?
# 그래프 = 노드(Node) + 간선(Edge)
#     1
#    / \
#   2   3
#  / \
# 4   5

# 노드: 1, 2, 3, 4, 5
# 간선: 1-2, 1-3, 2-4, 2-5

# 코드로 표현
# 인접 리스트 — 가장 많이 씀
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

# 2. DFS - 깊이 우선 탐색
# => 한 방향으로 끝까지 파고들다가 막히면 돌아오는 방식
#     1
#    / \
#   2   3
#  / \
# 4   5

# DFS 순서: 1 → 2 → 4 → 5 → 3

# 스택 / 재귀 구현
# 재귀 방식
def dfs(graph, node, visited):
    visited.add(node)        # 1. 현재 노드 방문 처리
    print(node, end=" ")     # 2. 현재 노드 출력

    for neighbor in graph[node]:       # 3. 현재 노드의 이웃 순회
        if neighbor not in visited:    # 4. 아직 방문 안 한 이웃만
            dfs(graph, neighbor, visited)  # 5. 재귀 호출

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

dfs(graph, 1, set())   # 1 2 4 5 3

# DFS 실행 흐름 손으로 추적

# dfs(1) 호출
#   visited = {1}, 출력: 1
#   이웃: [2, 3]

#   → 2 방문 안 함 → dfs(2) 호출
#       visited = {1, 2}, 출력: 2
#       이웃: [1, 4, 5]

#       → 1 이미 방문 → 스킵
#       → 4 방문 안 함 → dfs(4) 호출
#           visited = {1, 2, 4}, 출력: 4
#           이웃: [2]
#           → 2 이미 방문 → 스킵
#           → 더 이상 갈 곳 없음 → 돌아감

#       → 5 방문 안 함 → dfs(5) 호출
#           visited = {1, 2, 4, 5}, 출력: 5
#           이웃: [2]
#           → 2 이미 방문 → 스킵
#           → 더 이상 갈 곳 없음 → 돌아감

#   → 3 방문 안 함 → dfs(3) 호출
#       visited = {1, 2, 4, 5, 3}, 출력: 3
#       이웃: [1]
#       → 1 이미 방문 → 스킵
#       → 더 이상 갈 곳 없음 → 돌아감

# 최종 출력: 1 2 4 5 3

# visited 없으면?
# dfs(1) → dfs(2) → dfs(1) → dfs(2) → dfs(1) ...
# 무한 루프! ❌

# visited 있으면?
# dfs(1) → dfs(2) → dfs(1) 시도 → 이미 방문 → 스킵 ✅


# 스택 방식
def dfs_stack(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

dfs_stack(graph, 1)   # 1 3 2 5 4


# 3. BFS - 너비 우선 탐색
# => 가까운 노드부터 차례대로 탐색하는 방식
#     1
#    / \
#   2   3
#  / \
# 4   5

# BFS 순서: 1 → 2 → 3 → 4 → 5

# 큐 구현
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])    # 1. 시작 노드를 큐에 넣기
    visited.add(start)        # 2. 시작 노드 방문 처리

    while queue:              # 3. 큐가 빌 때까지
        node = queue.popleft()        # 4. 큐 앞에서 꺼내기
        print(node, end=" ")          # 5. 출력

        for neighbor in graph[node]:          # 6. 이웃 순회
            if neighbor not in visited:       # 7. 방문 안 한 이웃만
                visited.add(neighbor)         # 8. 방문 처리
                queue.append(neighbor)        # 9. 큐 뒤에 추가

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

bfs(graph, 1)   # 1 2 3 4 5

# BFS 실행 흐름 손으로 추적

# 초기 상태
# queue = [1], visited = {1}

# --- 1번째 반복 ---
# node = 1 (popleft)
# 출력: 1
# 이웃: [2, 3]
#   → 2 방문 안 함 → visited = {1, 2}, queue = [2]
#   → 3 방문 안 함 → visited = {1, 2, 3}, queue = [2, 3]

# --- 2번째 반복 ---
# node = 2 (popleft)
# 출력: 2
# 이웃: [1, 4, 5]
#   → 1 이미 방문 → 스킵
#   → 4 방문 안 함 → visited = {1,2,3,4}, queue = [3, 4]
#   → 5 방문 안 함 → visited = {1,2,3,4,5}, queue = [3, 4, 5]

# --- 3번째 반복 ---
# node = 3 (popleft)
# 출력: 3
# 이웃: [1]
#   → 1 이미 방문 → 스킵

# --- 4번째 반복 ---
# node = 4 (popleft)
# 출력: 4
# 이웃: [2] → 이미 방문 → 스킵

# --- 5번째 반복 ---
# node = 5 (popleft)
# 출력: 5
# 이웃: [2] → 이미 방문 → 스킵

# 최종 출력: 1 2 3 4 5

# DFS VS BFS
# DFS — 스택 / 재귀   깊이 우선   경로 탐색, 사이클 감지
# BFS — 큐            너비 우선   최단 거리, 레벨 탐색


# 4. 2차원 배열 탐색
# 1차원 그래프 DFS
# 이웃 = graph[node] 리스트

# 2차원 배열 DFS
# 이웃 = 상하좌우 4방향
dx = [-1, 1, 0, 0]   # 상, 하, 좌, 우 (x 변화량)
dy = [0, 0, -1, 1]   # 상, 하, 좌, 우 (y 변화량)

graph = [
    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 1]
]

# DFS — 연결된 영역 크기 구하기
def dfs_2d(graph, x, y, visited):

    # 경계 체크 — 배열 밖으로 나가면 0 반환
    if x < 0 or x >= len(graph): return 0
    if y < 0 or y >= len(graph[0]): return 0

    # 이미 방문했거나 0이면 (벽이면) 0 반환
    if visited[x][y] or graph[x][y] == 0: return 0

    visited[x][y] = True   # 방문 처리
    count = 1              # 현재 칸 카운트

    # 상하좌우 4방향 탐색
    for i in range(4):
        count += dfs_2d(graph, x + dx[i], y + dy[i], visited)

    return count

rows, cols = len(graph), len(graph[0])
visited = [[False] * cols for _ in range(rows)]
print(dfs_2d(graph, 0, 0, visited))   # 4


# 실행 흐름 손으로 추적
# graph = [
#     [1, 1, 0, 0],   # x=0
#     [1, 1, 0, 1],   # x=1
#     [0, 0, 1, 1],   # x=2
#     [0, 0, 1, 1]    # x=3
# ]
# y = 0  1  2  3

# dfs_2d(0, 0) 호출
#   경계 체크 통과
#   graph[0][0] = 1, 방문 안 함 → 진행
#   visited[0][0] = True, count = 1

#   상 (x=-1, y=0) → x < 0 → return 0
#   하 (x=1,  y=0) → graph[1][0] = 1
#       visited[1][0] = True, count = 1
#       상 (x=0, y=0) → 이미 방문 → return 0
#       하 (x=2, y=0) → graph[2][0] = 0 → return 0
#       좌 (x=1, y=-1) → y < 0 → return 0
#       우 (x=1, y=1) → graph[1][1] = 1
#           visited[1][1] = True, count = 1
#           상 (x=0, y=1) → graph[0][1] = 1
#               visited[0][1] = True, count = 1
#               상 (x=-1, y=1) → x < 0 → return 0
#               하 (x=1,  y=1) → 이미 방문 → return 0
#               좌 (x=0,  y=0) → 이미 방문 → return 0
#               우 (x=0,  y=2) → graph[0][2] = 0 → return 0
#               return 1
#           하 (x=2, y=1) → graph[2][1] = 0 → return 0
#           좌 (x=1, y=0) → 이미 방문 → return 0
#           우 (x=1, y=2) → graph[1][2] = 0 → return 0
#           return 1 + 1 = 2
#       return 1 + 2 = 3
#   좌 (x=0, y=-1) → y < 0 → return 0
#   우 (x=0, y=1) → 이미 방문 → return 0
#   return 1 + 3 = 4 ✅

# visited 2차원 배열 만드는 법
rows, cols = len(graph), len(graph[0])
visited = [[False] * cols for _ in range(rows)]

# 결과
# [[False, False, False, False],
#  [False, False, False, False],
#  [False, False, False, False],
#  [False, False, False, False]]

# visited[x][y] = True 로 방문 처리


# 5. BFS 최단 거리
from collections import deque

def bfs_shortest(graph, start, end):

    # visited 를 딕셔너리로 — 노드: 거리
    # 방문 여부 + 거리를 동시에 저장
    visited = {start: 0}   # 시작 노드 거리 = 0
    queue = deque([start])

    while queue:
        node = queue.popleft()

        # 목적지 도달하면 거리 반환
        if node == end:
            return visited[end]

        for neighbor in graph[node]:
            if neighbor not in visited:
                # 이웃 거리 = 현재 거리 + 1
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)

    return -1   # 경로 없음

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

print(bfs_shortest(graph, 1, 5))   # 2

# 실행 흐름 손으로 추적

# graph = {1:[2,3], 2:[1,4,5], 3:[1], 4:[2], 5:[2]}
# start=1, end=5

# 초기: visited={1:0}, queue=[1]

# --- 1번째 ---
# node = 1, visited[1]=0
# 이웃: [2, 3]
#   2 → visited={1:0, 2:1}, queue=[2]
#   3 → visited={1:0, 2:1, 3:1}, queue=[2, 3]

# --- 2번째 ---
# node = 2, visited[2]=1
# 이웃: [1, 4, 5]
#   1 → 이미 방문 스킵
#   4 → visited={..., 4:2}, queue=[3, 4]
#   5 → visited={..., 5:2}, queue=[3, 4, 5]

# --- 3번째 ---
# node = 3
# node == end(5)? → No
# 이웃: [1] → 이미 방문 스킵

# --- 4번째 ---
# node = 4
# node == end(5)? → No
# 이웃: [2] → 이미 방문 스킵

# --- 5번째 ---
# node = 5
# node == end(5)? → Yes!
# return visited[5] = 2 ✅

# visited 를 set 대신 dict 쓰는 이유
# set 방식 — 방문 여부만 저장
visited = {1, 2, 3}

# dict 방식 — 방문 여부 + 거리 동시 저장
visited = {1: 0, 2: 1, 3: 1}

# 거리 계산이 필요하면 dict 가 훨씬 편해요
