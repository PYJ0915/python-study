# 📚 Day 15 파이썬 심화 — 시간복잡도 + 스택 / 큐 / 덱

---

## 1️⃣ 시간복잡도 / 공간복잡도

### Big-O 표기법

```
O(1)       → 상수 시간   — 입력 크기 상관없이 항상 같은 시간
O(log n)   → 로그 시간   — 입력이 2배 → 시간이 1 증가
O(n)       → 선형 시간   — 입력이 2배 → 시간도 2배
O(n log n) → 선형 로그   — 정렬 알고리즘 평균
O(n²)      → 이차 시간   — 입력이 2배 → 시간이 4배
O(2ⁿ)      → 지수 시간   — 입력이 1 증가 → 시간이 2배

빠른 순서
O(1) > O(log n) > O(n) > O(n log n) > O(n²) > O(2ⁿ)
```

### 코드로 보는 시간복잡도

```python
# O(1) — 인덱스 접근
nums[0]

# O(n) — 반복문 1개
for n in nums:
    print(n)

# O(n²) — 반복문 2개 중첩
for i in nums:
    for j in nums:
        print(i, j)
```

### 공간복잡도

```python
# O(1) — 추가 공간 없음
def sum_nums(nums):
    total = 0           # 변수 1개만 사용
    for n in nums:
        total += n
    return total

# O(n) — 입력 크기만큼 추가 공간
def double(nums):
    return [x * 2 for x in nums]   # 새 리스트 생성
```

---

## 2️⃣ 스택 (Stack)

```
나중에 넣은 게 먼저 나오는 자료구조 (LIFO)
활용 — 브라우저 뒤로가기, 실행취소, 괄호 검사
```

```python
stack = []

stack.append(1)   # push [1]
stack.append(2)   # push [1, 2]
stack.append(3)   # push [1, 2, 3]

stack.pop()       # pop  → 3  [1, 2]
stack[-1]         # peek → 2  (제거 안 함)
```

### 스택 활용 패턴

```python
# 뒤집기 패턴
reversed_s = ""
while stack:
    reversed_s += stack.pop()
# pop() 은 뒤에서부터 꺼내니까 자동으로 뒤집힘

# 회문 검사
def is_palindrome(s: str) -> bool:
    stack = []
    for c in s:
        stack.append(c)

    reversed_s = ""
    while stack:
        reversed_s += stack.pop()

    return s == reversed_s

# 괄호 짝 검사
def is_valid(s: str) -> bool:
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0
```

---

## 3️⃣ 큐 (Queue)

```
먼저 넣은 게 먼저 나오는 자료구조 (FIFO)
활용 — 프린터 대기열, BFS
```

```python
from collections import deque

queue = deque()

queue.append(1)     # enqueue [1]
queue.append(2)     # enqueue [1, 2]
queue.append(3)     # enqueue [1, 2, 3]

queue.popleft()     # dequeue → 1  [2, 3]
queue[0]            # peek → 2 (제거 안 함)
```

### 리스트 대신 deque 쓰는 이유

```python
# 리스트 pop(0) → O(n) 느림
nums.pop(0)

# deque popleft() → O(1) 빠름
queue.popleft()
```

### 큐 활용 패턴

```python
# 프린터 대기열 시뮬레이션
def printer(jobs: list) -> list:
    queue = deque(jobs)
    result = []

    while queue:
        f = queue.popleft()
        if any(n > f for n in queue):   # 더 높은 우선순위 있으면
            queue.append(f)              # 다시 맨 뒤에
        else:
            result.append(f)             # 없으면 출력
    return result

print(printer([1, 3, 2, 3, 1]))   # [3, 3, 2, 1, 1]
```

---

## 4️⃣ 덱 (Deque)

```
앞뒤 양쪽에서 넣고 뺄 수 있는 자료구조
활용 — 최근 검색어, 슬라이딩 윈도우
```

```python
from collections import deque

dq = deque()

dq.append(1)        # 뒤에 추가
dq.appendleft(0)    # 앞에 추가
dq.pop()            # 뒤에서 제거
dq.popleft()        # 앞에서 제거

# 최대 크기 설정
dq = deque(maxlen=5)   # 5개 초과 시 반대쪽 자동 제거

# 회전
dq = deque([1, 2, 3, 4, 5])
dq.rotate(2)        # [4, 5, 1, 2, 3] 오른쪽으로 2칸
dq.rotate(-2)       # [1, 2, 3, 4, 5] 왼쪽으로 2칸
```

### 덱 활용 패턴

```python
# 최근 검색어
history = deque(maxlen=5)

def search(keyword: str) -> None:
    if keyword in history:
        history.remove(keyword)   # 기존 것 삭제
    history.appendleft(keyword)   # 맨 앞에 추가

search("python")
search("java")
search("python")
print(list(history))   # ['python', 'java']
```

---

## 5️⃣ any() / all()

```python
# any() — 하나라도 True 면 True
any([True, False, False])       # True
any(n > 3 for n in [1,2,3,4])  # True  (4 있음)

# all() — 전부 True 여야 True
all([True, True, True])         # True
all(n > 0 for n in [1,2,3])    # True

# 기존 방식 vs any()
# 기존
found = False
for n in queue:
    if n > f:
        found = True
        break
if found: ...

# any() 로 한 줄로
if any(n > f for n in queue): ...
```

---

## ✅ 스택 / 큐 / 덱 한눈에 비교

```
스택  → append() / pop()                  LIFO
큐    → append() / popleft()              FIFO
덱    → append() / appendleft()
        pop() / popleft() / remove()      양방향

공통  → deque 는 리스트보다 앞쪽 삽입/삭제가 빠름 O(1)
```

---

## ✅ 오늘 주의사항

```python
# 큐는 리스트 말고 deque 사용
nums.pop(0)         # O(n) ❌
queue.popleft()     # O(1) ✅

# deque.popleft() 는 인자 없음
history.popleft(x)  # ❌ 없는 메서드
history.remove(x)   # ✅ 특정 값 제거

# any() 루프 안에서 쓸 때 무한루프 주의
for n in queue:
    if n > f:
        queue.append(f)  # ❌ 루프 안에서 append → 무한루프

if any(n > f for n in queue):
    queue.append(f)      # ✅ 루프 밖에서 append
```
