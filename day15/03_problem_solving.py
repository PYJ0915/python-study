# 실습 문제

# 문제 1 - 스택을 활용해서 문자열이 회문인지 검사하는 함수 구현
# ** 내 풀이 **
# def is_palindrome(s: str) -> bool:
#   stack = []
#   for c in s:
#     stack.append(c)
#   for i in range(len(stack)) :
#     if stack.pop() == stack[-i]:
#       return True
#     else:
#       return False
    
# print(is_palindrome("racecar"))   # True
# print(is_palindrome("hello"))     # False
# print(is_palindrome("madam"))     # True

# ** 개선된 풀이 - 스택 특성 활용 **
def is_palindrome(s: str) -> bool:
  stack = []
  for c in s:
    stack.append(c)
  
  reversed_s = ""
  while stack:
    reversed_s += stack.pop()  # 스택에서 하나씩 꺼내면 뒤집힌 문자열

  return s == reversed_s

print(is_palindrome("racecar"))   # True
print(is_palindrome("hello"))     # False
print(is_palindrome("madam"))     # True

# 문제 2 - 큐를 활용해서 프린터 대기열 시뮬레이션 구현
# 우선순위가 높은 것이 먼저 출력
# 우선순위가 같으면 먼저 들어온 것이 먼저 출력
from collections import deque

# ** 내 풀이 - 틀림 ** 

# def printer(jobs: list) -> list:
#   queue = deque(jobs)
#   result = []

#   while queue:
#     f = queue.popleft()
#     for n in queue:
#       if n > f:
#         queue.append(f)
#       else:
#         result.append(f)
  
#   return result

# jobs = [1, 3, 2, 3, 1]  # 우선순위 목록
# print(printer(jobs))

# ** 완성 풀이 — queue 에 더 높은 우선순위가 있는지 먼저 확인 **
def printer(jobs: list) -> list:
  queue = deque(jobs)
  result = []

  while queue:
    f = queue.popleft()
    if any(n > f for n in queue):
      queue.append(f)
    else:
      result.append(f)
  return result
  
job_list = [1, 3, 2, 3, 1]  # 우선순위 목록
print(printer(job_list))


# 문제 3 - 덱을 활용해서 최근 검색어 기능 구현

# ** 내 풀이 - 틀림 ** 
# history = deque(maxlen=5)

# def search(keyword: str) -> None:
#   for h in history:
#     if h == keyword:
#       history.popleft(h)
#     else:
#       history.appendleft(keyword)

# search("python")
# search("java")
# search("python")
# print(list(history))

# ** 완성 풀이 **
history = deque(maxlen=5)

def search(keyword: str) -> None:
  if keyword in history:
    history.remove(keyword)
  history.appendleft(keyword)

search("python")
search("java")
search("python")
print(list(history))   # ['python', 'java']

