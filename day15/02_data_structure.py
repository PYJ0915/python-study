# 자료 구조 - 데이터를 효율적으로 저장, 관리, 처리하기 위한 구조
# 예시 - 리스트, 튜플, 딕셔너리, set, 스택, 큐, 덱 ...

# 1. 스택(Stack) - 나중에 넣은 게 먼저 나오는 자료구조 (LIFO)
# 코드 구현
stack = []  # 파이썬 리스트로 구현

stack.append(1) # push [1]
stack.append(2) # push [1, 2]
stack.append(3) # push [1, 2, 3]

stack.pop()     # pop → 3  [1, 2]
stack.pop()     # pop → 2  [1]
stack[-1]       # peek → 1 (제거 안 함)

# 실용 예제 - 괄호 짝 검사
def is_valid(s: str) -> bool:
  stack= []
  for c in s:
    if c == "(":
      stack.append(c)
    elif c == ")":
      if not stack:
        return False
      stack.pop()
  return len(stack) == 0

print(is_valid("(())"))   # True
print(is_valid("(()"))    # False
print(is_valid(")("))     # False

# 2. 큐(Queue) - 먼저 넣은 게 먼저 나오는 자료 구조(FIFO)
# 코드 구현
from collections import deque

queue = deque() # 리스트 대신 deque 사용

queue.append(1) # enqueue [1]
queue.append(1) # enqueue [1, 2]
queue.append(1) # enqueue [1, 2, 3]

queue.popleft() # dequeue → 1  [2, 3]
queue.popleft() # dequeue → 2  [3]
queue[0]        # peek → 3 (제거 안 함)

# 큐는 리스트 대신 deque 를 쓰는 이유
# 리스트 pop(0) → O(n) 느림
# nums.pop(0)

# deque popleft() → O(1) 빠름
# queue.popleft()

# 3. 덱(Deque) - 앞 뒤 양쪽에서 넣고 뺄 수 있는 자료구조
# 코드 구현
dq = deque()

# 뒤에 추가 / 제거
dq.append(1)
dq.append(2)
dq.pop()

# 앞에 추가 / 제거
dq.appendleft(0)
dq.popleft()

# 회전
dq = deque([1, 2, 3, 4, 5])
dq.rotate(2)   # [4, 5, 1, 2, 3] 오른쪽으로 2칸
dq.rotate(-2)  # [1, 2, 3, 4, 5] 왼쪽으로 2칸


# ** 스택 vs 큐 vs 덱 한눈에 **
# 스택  → 뒤에서만 넣고 뺌  (LIFO) — 브라우저 뒤로가기, 실행취소
# 큐    → 뒤에 넣고 앞에서 뺌 (FIFO) — 프린터 대기열, BFS
# 덱    → 앞뒤 양쪽 다 가능        — 슬라이딩 윈도우