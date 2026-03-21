# 실습 문제
# 문제 1 - 버블 정렬을 내림차순으로 구현
def bubble_sort_desc(nums: list) -> list:
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

print(bubble_sort_desc([5, 3, 8, 1, 4]))   # [8, 5, 4, 3, 1]

# 문제 2 - 퀵 정렬로 문자열 리스트를 길이 기준으로 정렬
def quick_sort_by_len(words: list) -> list:
  if len(words) <= 1:
      return words
    
  pivot = words[len(words) // 2]

  left = [x for x in words if len(x) < len(pivot)]
  mid = [x for x in words if len(x) == len(pivot)]
  right = [x for x in words if len(x) > len(pivot)]

  return quick_sort_by_len(left) + mid + quick_sort_by_len(right)

words = ["banana", "apple", "kiwi", "fig"]
print(quick_sort_by_len(words))   # ['fig', 'kiwi', 'apple', 'banana']

# 문제 3 - 아래 데이터를 score 기준 내림차순으로 정렬
students = [
    {"name": "Tom", "score": 85},
    {"name": "Jane", "score": 92},
    {"name": "Mike", "score": 78},
]

print(sorted(students, key=lambda x: x["score"], reverse=True))


# 💡 문제 3 — 직접 구현 버전도 알아두기
# 코딩테스트에서 sorted() 못 쓰는 경우 대비
# 선택 정렬로 구현
def sort_students(students):
    n = len(students)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if students[j]["score"] > students[max_idx]["score"]:
                max_idx = j
        students[i], students[max_idx] = students[max_idx], students[i]
    return students
