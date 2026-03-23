# 실습문제
import bisect
from collections import deque
# 문제 1 - 이진탐색으로 정렬된 리스트에서 target 의 개수 구하기
def count_target(nums: list, target: int) -> int:
    return bisect.bisect_right(nums, target) - bisect.bisect_left(nums, target)

nums = [1, 2, 2, 2, 3, 4, 5]
print(count_target(nums, 2))   # 3
print(count_target(nums, 6))   # 0


# 문제 2 - 정렬된 리스트에서 target 에 가장 가까운 값을 반환
def closest_value(nums: list, target: int) -> int:
    closet_index = bisect.bisect_left(nums, target)
    return nums[closet_index]

nums = [1, 3, 5, 7, 9]
print(closest_value(nums, 6))   # 5 또는 7 (둘 다 정답)
print(closest_value(nums, 4))   # 3 또는 5 (둘 다 정답)


# 문제 3 - 파라메트릭 서치 — 아래 조건을 이진탐색으로 풀기
# 리스트의 합이 target 이상이 되는
# 최소 원소 개수 구하기
def min_count(nums, target):
    nums.sort(reverse=True)   # 큰 수부터 정렬
    left, right = 1, len(nums)
    result = len(nums)

    while left <= right:
        mid = (left + right) // 2
        # mid 개 만큼 앞에서부터 더했을 때
        total = sum(nums[:mid])

        if total >= target:
            result = mid        # 일단 저장
            right = mid - 1     # 더 적은 개수로 가능한지 탐색
        else:
            left = mid + 1      # 개수가 부족하면?

    return result

nums = [1, 2, 3, 4, 5]
print(min_count(nums, 9))    # 2 ← 4+5=9
print(min_count(nums, 15))   # 5 ← 전부 합해야 15

# 문제 4 - 아래 그래프에서 DFS / BFS 탐색 순서를 각각 구하기
graph = {
    1: [2, 4],
    2: [1, 3],
    3: [2, 4],
    4: [1, 3, 5],
    5: [4]
}

# DFS 시작: 1 -> 2 -> 3 -> 4 -> 5
# BFS 시작: 1 -> 2 -> 4 -> 3 -> 5

# 문제 5 - 아래 2차원 배열에서 1로 연결된 영역의 개수를 구하기
graph = [
    [1, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1],
    [1, 1, 0, 0]
]

dx = [-1, 1, 0, 0]   # 상, 하, 좌, 우 (x 변화량)
dy = [0, 0, -1, 1]   # 상, 하, 좌, 우 (y 변화량)

def dfs_2d(graph, x, y, visited):

    if x < 0 or x >= len(graph): return 0
    if y < 0 or y >= len(graph[0]): return 0

    if visited[x][y] or graph[x][y] == 0: return 0

    visited[x][y] = True   
    count = 1             

    for i in range(4):
        count += dfs_2d(graph, x + dx[i], y + dy[i], visited)

    return count

def count_areas(graph):
    rows, cols = len(graph), len(graph[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0

    for x in range(rows):
        for y in range(cols):
            if graph[x][y] == 1 and not visited[x][y]:
                dfs_2d(graph, x, y, visited)
                count += 1
    
    return count

print(count_areas(graph))
# 결과: 4 (영역이 4개)

# 문제 6 - 노드 1에서 노드 5까지 최단 거리를 구하기
def bfs_shortest(graph, start, end):
    visited = {start : 0}
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node == end:
            return visited[end]
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)
    return -1   

graph = {
    1: [2, 3],
    2: [4],
    3: [4, 5],
    4: [5],
    5: []
}

print(bfs_shortest(graph, 1, 5))
# 결과: 2 (1→3→5)



# 문제 2번 개선된 풀이 => 양쪽 비교 추가!
def closest_value(nums, target):
    i = bisect.bisect_left(nums, target)

    # 경계 처리
    if i == 0:
        return nums[0]              # 왼쪽 없음
    if i == len(nums):
        return nums[-1]             # 오른쪽 없음

    # 양쪽 비교
    left_val  = nums[i - 1]
    right_val = nums[i]

    if abs(target - left_val) <= abs(target - right_val):
        return left_val
    return right_val

nums = [1, 3, 5, 7, 9]
print(closest_value(nums, 6))   # 5 또는 7
print(closest_value(nums, 4))   # 3 또는 5