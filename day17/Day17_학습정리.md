# 📚 Day 17 파이썬 심화 — 정렬 알고리즘

---

## 1️⃣ 버블 정렬 (Bubble Sort)

### 핵심 아이디어
```
옆에 있는 두 값을 비교해서 교환
한 라운드가 끝나면 가장 큰 값이 맨 뒤로 확정
```

### 동작 과정
```
[5, 3, 8, 1, 4]

1라운드
5,3 비교 → 교환 [3, 5, 8, 1, 4]
5,8 비교 → 유지 [3, 5, 8, 1, 4]
8,1 비교 → 교환 [3, 5, 1, 8, 4]
8,4 비교 → 교환 [3, 5, 1, 4, 8] ← 8 확정

2라운드
3,5 비교 → 유지
5,1 비교 → 교환 [3, 1, 5, 4, 8]
5,4 비교 → 교환 [3, 1, 4, 5, 8] ← 5 확정
... 반복
```

### 코드

```python
def bubble_sort(nums: list) -> list:
    n = len(nums)
    for i in range(n):
        # i 번 라운드 후 뒤에서 i개는 이미 정렬됨
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

# 내림차순 — 부등호만 반대로
def bubble_sort_desc(nums: list) -> list:
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] < nums[j + 1]:   # < 로 변경
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

print(bubble_sort([5, 3, 8, 1, 4]))       # [1, 3, 4, 5, 8]
print(bubble_sort_desc([5, 3, 8, 1, 4]))  # [8, 5, 4, 3, 1]
```

```
시간복잡도: O(n²)
공간복잡도: O(1)
특징: 구현 쉽지만 느림
```

---

## 2️⃣ 선택 정렬 (Selection Sort)

### 핵심 아이디어
```
가장 작은 값을 찾아서 맨 앞으로 가져오기
한 라운드가 끝나면 가장 작은 값이 앞에 확정
```

### 동작 과정
```
[5, 3, 8, 1, 4]

1라운드 — 전체에서 최솟값 찾기
최솟값 = 1 (인덱스 3)
인덱스 0 과 교환
[1, 3, 8, 5, 4] ← 1 확정

2라운드 — 나머지에서 최솟값 찾기
[3, 8, 5, 4] 에서 최솟값 = 3 (이미 맨 앞)
[1, 3, 8, 5, 4] ← 3 확정

3라운드
[8, 5, 4] 에서 최솟값 = 4
[1, 3, 4, 5, 8] ← 4 확정
```

### 코드

```python
def selection_sort(nums: list) -> list:
    n = len(nums)
    for i in range(n):
        min_idx = i                      # 현재 위치를 최솟값으로 가정
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j              # 더 작은 값 발견 → 인덱스 업데이트
        nums[i], nums[min_idx] = nums[min_idx], nums[i]   # 교환
    return nums

print(selection_sort([5, 3, 8, 1, 4]))   # [1, 3, 4, 5, 8]
```

```
시간복잡도: O(n²)
공간복잡도: O(1)
특징: 교환 횟수가 적음
```

---

## 3️⃣ 삽입 정렬 (Insertion Sort)

### 핵심 아이디어
```
카드 게임처럼 하나씩 뽑아서 올바른 위치에 끼워넣기
왼쪽은 항상 정렬된 상태 유지
```

### 동작 과정
```
[5, 3, 8, 1, 4]

i=1, key=3
5 > 3 → 5를 한 칸 뒤로 [_, 5, 8, 1, 4]
key(3) 삽입 → [3, 5, 8, 1, 4]

i=2, key=8
5 < 8 → 멈춤
key(8) 삽입 → [3, 5, 8, 1, 4]

i=3, key=1
8 → 5 → 3 전부 뒤로 밀기
key(1) 삽입 → [1, 3, 5, 8, 4]
... 반복
```

### 코드

```python
def insertion_sort(nums: list) -> list:
    for i in range(1, len(nums)):
        key = nums[i]     # 현재 삽입할 값
        j = i - 1         # 왼쪽 끝부터 비교

        # key 보다 큰 값들을 한 칸씩 뒤로 밀기
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key   # 올바른 위치에 삽입
    return nums

print(insertion_sort([5, 3, 8, 1, 4]))   # [1, 3, 4, 5, 8]
```

```
시간복잡도: O(n²) / 거의 정렬된 경우 O(n)
공간복잡도: O(1)
특징: 거의 정렬된 데이터에서 빠름
```

---

## 4️⃣ 퀵 정렬 (Quick Sort)

### 핵심 아이디어
```
기준값(pivot) 을 정하고
작은 것은 왼쪽, 큰 것은 오른쪽으로 나눈 후 재귀
```

### 동작 과정
```
[5, 3, 8, 1, 4]

pivot = 3 (중간값)
left  = [1]       ← 3 보다 작은 것
mid   = [3]       ← 3 과 같은 것
right = [5, 8, 4] ← 3 보다 큰 것

right 재귀 정렬 → [4, 5, 8]
최종: [1] + [3] + [4, 5, 8] = [1, 3, 4, 5, 8]
```

### 코드

```python
def quick_sort(nums: list) -> list:
    if len(nums) <= 1:
        return nums

    pivot = nums[len(nums) // 2]

    left  = [x for x in nums if x < pivot]
    mid   = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)

# 길이 기준 정렬
def quick_sort_by_len(words: list) -> list:
    if len(words) <= 1:
        return words

    pivot = words[len(words) // 2]
    left  = [x for x in words if len(x) < len(pivot)]
    mid   = [x for x in words if len(x) == len(pivot)]
    right = [x for x in words if len(x) > len(pivot)]

    return quick_sort_by_len(left) + mid + quick_sort_by_len(right)

print(quick_sort([5, 3, 8, 1, 4]))   # [1, 3, 4, 5, 8]
words = ["banana", "apple", "kiwi", "fig"]
print(quick_sort_by_len(words))       # ['fig', 'kiwi', 'apple', 'banana']
```

```
시간복잡도: 평균 O(n log n) / 최악 O(n²)
공간복잡도: O(log n)
특징: 평균적으로 가장 빠름
```

---

## 5️⃣ 병합 정렬 (Merge Sort)

### 핵심 아이디어
```
반씩 나누고 정렬된 두 리스트를 합치기
분할 정복 (Divide and Conquer)
```

### 동작 과정
```
[5, 3, 8, 1, 4]

나누기
[5, 3] + [8, 1, 4]
[5] + [3] + [8] + [1, 4]
[5] + [3] + [8] + [1] + [4]

합치기
[3, 5] ← [5] + [3]
[1, 4] ← [1] + [4]
[1, 4, 8] ← [8] + [1, 4]
[1, 3, 4, 5, 8] ← [3, 5] + [1, 4, 8]
```

### 코드

```python
def merge_sort(nums: list) -> list:
    if len(nums) <= 1:
        return nums

    mid   = len(nums) // 2
    left  = merge_sort(nums[:mid])   # 왼쪽 절반 재귀 정렬
    right = merge_sort(nums[mid:])   # 오른쪽 절반 재귀 정렬

    return merge(left, right)

def merge(left: list, right: list) -> list:
    result = []
    i = j = 0

    # 두 리스트 앞에서부터 비교하면서 작은 것부터 추가
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result + left[i:] + right[j:]   # 남은 것 전부 추가

print(merge_sort([5, 3, 8, 1, 4]))   # [1, 3, 4, 5, 8]
```

```
시간복잡도: O(n log n) 항상 보장
공간복잡도: O(n)
특징: 안정적 — 항상 O(n log n)
```

---

## ✅ 정렬 알고리즘 한눈에 비교

```
버블 정렬  → O(n²)      옆끼리 비교해서 교환
선택 정렬  → O(n²)      최솟값 찾아서 앞으로
삽입 정렬  → O(n²)      올바른 위치에 끼워넣기 (거의 정렬된 데이터에 빠름)
퀵 정렬    → O(n log n) pivot 기준으로 나누기 (평균 가장 빠름)
병합 정렬  → O(n log n) 반씩 나누고 합치기 (항상 안정적)
sorted()   → O(n log n) Tim Sort (삽입 + 병합)
```

---

## ✅ 오늘 주의사항

```python
# 1. 내림차순 — 부등호만 반대로
if nums[j] > nums[j + 1]:   # 오름차순
if nums[j] < nums[j + 1]:   # 내림차순

# 2. 퀵 정렬 — 비교 기준 변경
left = [x for x in nums if x < pivot]          # 숫자 기준
left = [x for x in words if len(x) < len(pivot)]  # 길이 기준

# 3. sorted() 사용 가능하면 활용
sorted(students, key=lambda x: x["score"], reverse=True)  # ✅ 간결

# 4. 코딩테스트에서 직접 구현이 필요한 경우
# 선택 정렬로 딕셔너리 리스트 정렬
def sort_students(students):
    n = len(students)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if students[j]["score"] > students[max_idx]["score"]:
                max_idx = j
        students[i], students[max_idx] = students[max_idx], students[i]
    return students
```
