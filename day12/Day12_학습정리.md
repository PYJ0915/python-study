# 📚 Day 12 파이썬 심화 — 제너레이터 / 이터레이터 + 데코레이터

---

## 1️⃣ 이터레이터

```python
# for문 내부 동작 원리
nums = [1, 2, 3]
it = iter(nums)       # 이터레이터 생성
print(next(it))       # 1
print(next(it))       # 2
print(next(it))       # 3
print(next(it))       # StopIteration 에러 발생

# for문은 내부적으로 iter() → next() 반복
# StopIteration 발생하면 자동으로 멈춤

# 이터레이터 직접 만들기
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):     # iter() 호출 시 실행
        return self

    def __next__(self):     # next() 호출 시 실행
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

for n in Counter(1, 5):
    print(n)
# 1 2 3 4 5
```

---

## 2️⃣ 제너레이터

```python
# yield — 함수 일시정지, 값 하나씩 반환
def gen():
    yield 1     # 여기서 멈추고 1 반환
    yield 2     # 다음 호출 시 재개
    yield 3

g = gen()
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3

# for문으로도 사용 가능
for n in gen():
    print(n)
```

### return vs yield

```python
# return — 함수 종료, 값 한 번만 반환
def func():
    return 1
    return 2    # 실행 안 됨

# yield — 함수 일시정지, 값 하나씩 반환
def gen():
    yield 1     # 여기서 멈춤
    yield 2     # 다음 호출 시 재개
    yield 3
```

### 제너레이터가 유용한 이유

```python
# 리스트 — 전부 메모리에 올림
nums = [x for x in range(1000000)]      # 메모리 많이 씀

# 제너레이터 — 필요할 때 하나씩 생성
nums = (x for x in range(1000000))      # 메모리 거의 안 씀

# 괄호 차이
[x for x in range(10)]   # [] → 리스트 컴프리헨션
(x for x in range(10))   # () → 제너레이터 표현식
```

### 실용적인 패턴

```python
# 무한 수열 생성기
def infinite_counter(start=0):
    n = start
    while True:
        yield n
        n += 1

# 파일 한 줄씩 읽기 (대용량 파일에 유용)
def read_lines(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()

# n개 제곱수 반환
def square_gen(n, start=1):
    current = start
    for _ in range(n):
        yield current * current
        current += 1

for n in square_gen(5):
    print(n)
# 1 4 9 16 25
```

---

## 3️⃣ 데코레이터

```python
# 기본 구조
def decorator(func):        # 1. 함수를 인자로 받음
    def wrapper(*args, **kwargs):   # 2. 새 함수 정의
        print("시작 전")
        result = func(*args, **kwargs)  # 3. 원래 함수 실행
        print("시작 후")
        return result       # 4. 결과 반환 필수
    return wrapper          # 5. 새 함수 반환

# @ 문법으로 적용
@decorator
def greet():
    print("Hello")

greet()
# 시작 전
# Hello
# 시작 후
```

### 실용적인 데코레이터

```python
import time

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
# slow_func 실행 시간: 1.0012초

# 로그 남기기
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} 호출 — 인자: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

# 호출 횟수 세기
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)
    wrapper.count = 0       # wrapper 에 속성 달기
    return wrapper

@count_calls
def say_hello():
    print("Hello")

say_hello()
say_hello()
say_hello()
print(say_hello.count)  # 3
```

### 데코레이터 중첩

```python
@logger
@timer
def add(a, b):
    return a + b

# 아래와 동일
add = logger(timer(add))
# 적용 순서 — 아래에서 위로 (timer 먼저 → logger)
```

---

## ✅ 오늘 주의사항

```python
# 1. wrapper에 return 필수
def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # return result  ← 없으면 None 반환
        return result    # ✅ 항상 return 써야 해요

# 2. count 속성은 wrapper에 달기
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1   # wrapper에 달아야 함
        return func(*args, **kwargs)
    wrapper.count = 0        # func.count ❌ wrapper.count ✅
    return wrapper

# 3. 출력 형식 정확하게
args_str = ", ".join(str(a) for a in args)
print(f"[호출] {func.__name__}({args_str})")  # ✅
print(f"[호출] {func.__name__}{args}")         # ⚠️ 인자 1개면 쉼표 붙음
```
