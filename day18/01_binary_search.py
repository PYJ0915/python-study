# 이진탐색 - 정렬된 리스트에서 절반씩 줄여가며 탐색하는 방법

# 1. 이진탐색이란?
# 순차 탐색 — 처음부터 끝까지 O(n)
# 이진탐색 — 절반씩 줄여가며 O(log n)

# 100만 개 데이터에서 찾기
# 순차 탐색 → 최대 100만 번
# 이진탐색 → 최대 20번 (log₂ 1,000,000 ≈ 20)

# 2. 동작 과정
# [1, 3, 5, 7, 9, 11, 13] 에서 9 찾기

# 1단계
# left=0, right=6, mid=3
# nums[3] = 7 < 9 → 오른쪽 탐색
# left = mid + 1 = 4

# 2단계
# left=4, right=6, mid=5
# nums[5] = 11 > 9 → 왼쪽 탐색
# right = mid - 1 = 4

# 3단계
# left=4, right=4, mid=4
# nums[4] = 9 → 찾았다!

# 3. 기본 구현
def binary_search(nums: list, target: int) -> int:
  left, right  = 0, len(nums) -1

  while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
      return mid       # 찾으면 인덱스 반환
    elif nums[mid] < target:
      left = mid + 1   # 오른쪽 탐색
    else:
      right = mid - 1  # 왼쪽 탐색
  
  return -1

nums = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(nums, 7))    # 3
print(binary_search(nums, 9))    # 4
print(binary_search(nums, 4))    # -1


# 4. 재귀로 구현
def binary_search_recursive(nums, target, left, right):
  if left > right:
    return -1
  
  mid = (left + right) // 2

  if nums[mid] == target:
    return mid
  elif nums[mid] < target:
    return binary_search_recursive(nums, target, mid + 1, right)
  else:
    return binary_search_recursive(nums, target, left, mid - 1)
  
nums = [1, 3, 5, 7, 9, 11, 13]
print(binary_search_recursive(nums, 7, 0, len(nums) - 1))   # 3

# 5. 파이썬 biscet 모듈 - 오름차순 리스트에 끼워넣는 위치 찾기
# => 정렬된 리스트 전용 (정렬 안 되어 있으면 → 결과 신뢰 ❌)
import bisect 

nums = [1, 3, 5, 7, 9]

# 삽입 위치 찾기
bisect.bisect_left(nums, 5)    # 2 ← 5를 넣을 수 있는 가장 왼쪽 위치
bisect.bisect_right(nums, 5)   # 3 ← 5를 넣을 수 있는 가장 오른쪽 위치

# 정렬 유지하면서 삽입
bisect.insort(nums, 6)
print(nums)  # [1, 3, 5, 6, 7, 9]

# 값 존재 확인
def contains(nums, target):
  i = bisect.bisect_left(nums, target)
  return i < len(nums) and nums[i] == target # len(nums) => IndexError 방지

print(contains(nums, 5))   # True
print(contains(nums, 4))   # False

# 6. 이진탐색 응용 — 조건을 만족하는 최솟값/최댓값 찾기
# 특정 값 이상인 첫 번째 인덱스 찾기
def find_first_ge(nums: list, target: int) -> int:
    left, right = 0, len(nums) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            result = mid      # 일단 저장
            right = mid - 1   # 더 왼쪽에 있을 수도 있으니 계속 탐색
        else:
            left = mid + 1

    return result

nums = [1, 3, 5, 7, 9, 11]
print(find_first_ge(nums, 6))   # 3 ← nums[3]=7 이 6 이상인 첫 번째






