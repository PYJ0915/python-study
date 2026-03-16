import time
# 데코레이터 - 함수를 받아서 기능을 추가한 새 함수를 반환하는 것

# 1. 데코레이터 학습 전 핵심 개념
# 핵심 개념 - 함수도 객체!
def greet():
  print("Hello")

f = greet   # 함수를 변수에 담기
f()         # Hello

def run(func): # 함수를 인자로 받기
  func()

run(greet)  # Hello

# 2. 데코레이터 기본 구조
def decorator(func):    # 1. 함수를 인자로 받음
  def wrapper():        # 2. 새 함수 정의
    print("시작 전")
    func()              # 3. 원래 함수 실행
    print("시작 후")
  return wrapper        # 4. 새 함수 반환

def greet():
  print("Hello")

# 데코레이터 적용 방법 1 - 직접 호출
greet = decorator(greet)
greet()
# 시작 전
# Hello
# 시작 후

# 데코레이터 적용 방법 2 - @ 문법 (더 많이 사용)
@decorator
def greet():
  print("Hello")

greet()
# 시작 전
# Hello
# 시작 후

# 3. 인자가 있는 함수에 데코레이터 적용
def decorator(func):
  def wrapper(*args, **kwargs):
    print("시작 전")
    result = func(*args, **kwargs)
    print("시작 후")
    return result
  return wrapper

@decorator
def add(a, b):
  return a + b

print(add(3, 4))
# 시작 전
# 시작 후
# 7

# 4. 데코레이터 실용 예제

# 실행 시간 측정
def timer(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"{func.__name__} 실행 시간: {end - start:.4f}초")
    return result
  return wrapper

@timer
def slow_func():
  time.sleep(1)
  print("완료")

slow_func()
# 완료
# slow_func 실행 시간: 1.0010초

# 로그 남기기
def logger(func):
  def wrapper(*args, **kwargs):
    print(f"{func.__name__} 호출 - 인자: {args}, {kwargs}")
    return func(*args, **kwargs)
  return wrapper

@logger
def add(a, b):
  return a + b

print(add(3, 4))
# add 호출 - 인자: (3, 4), {}
# 7

# 데코레이터 중첩
# 1) @

@logger
@timer
def mul(a, b):
  return a * b

print(mul(3, 2))
# wrapper 호출 - 인자: (3, 2), {}
# mul 실행 시간: 0.0000초
# 6

# 2) 직접 호출
mul = logger(timer(mul))

# 적용 순서 — 아래에서 위로
# timer 먼저 적용 → logger 적용

# 연습 문제
# 문제 1 - 함수 실행 전후에 아래처럼 출력하는 데코레이터 log_decorator 를 만들기
def log_decorator(func):
  def wrapper(*args, **kwargs):
    print(f"[호출] {func.__name__}{args}")
    result = func(*args, **kwargs)
    print(f"[결과] {result}")
  return wrapper

@log_decorator
def multiply(a, b):
    return a * b

multiply(3, 4)
# [호출] multiply(3, 4)
# [결과] 12

# 문제 2 - 함수가 몇 번 호출됐는지 세는 데코레이터 count_calls 만들기
def count_calls(func):
  def wrapper(*args, **kwargs):
   wrapper.count += 1 
   return func(*args, **kwargs)
  wrapper.count = 0
  return wrapper

@count_calls
def say_hello():
    print("Hello")

say_hello()   # Hello
say_hello()   # Hello
say_hello()   # Hello
print(say_hello.count)  # 3

# 문제 풀이 개선점
# 문제 1 
# wrapper에 return 필수
def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # return result  ← 없으면 None 반환
        return result    # 항상 return 써야 함!

# 출력 형식 정확하게
# args_str = ", ".join(str(a) for a in args)
# print(f"[호출]{func.__name__}({args_str})")  # ✅
# print(f"[호출]{func.__name__}{args}")         # 인자 1개면 쉼표 붙음

# 문제 2
# count 속성은 wrapper에 달기
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1   # wrapper에 달아야 함
        return func(*args, **kwargs)
    wrapper.count = 0        # func.count ❌ wrapper.count ✅
    return wrapper