# 📚 Day 06 학습 정리
> 재귀 함수 + 클래스 + Python 스타일 코드

---

## 1️⃣ 재귀 함수

```python
# 핵심 구조
def f(n):
    if n == 0:          # 1. 종료 조건 (Base Case) 먼저
        return 0
    return n + f(n-1)   # 2. 문제를 작게 쪼개기

# 팩토리얼
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

# 피보나치
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

# 리스트 합계
def list_sum(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + list_sum(nums[1:])
```

> 💡 재귀 핵심
> 1. 종료 조건 (Base Case) 먼저 생각하기
> 2. 문제를 작게 쪼개기
> 3. 흐름을 손으로 추적해보기

---

## 2️⃣ 클래스

```python
class Person:
    def __init__(self, name, age):  # 생성자
        self.name = name            # 속성
        self.age = age

    def greet(self):                # 메서드 (항상 self 첫 번째)
        print(f"Hello {self.name}")

# 객체 생성
p = Person("Tom", 25)
p.greet()

# 속성 직접 접근 / 수정
print(p.name)
p.age = 26
```

### 자바 vs 파이썬 클래스

```python
# 자바                          파이썬
# new Person("Tom")         →   Person("Tom")
# this.name                 →   self.name
# Person() { }              →   def __init__(self):
# void greet() { }          →   def greet(self):
# getter/setter 필수         →   직접 접근 가능
```

### 클래스 설계 팁

```python
def __init__(self, sentence):
    # 자주 쓰는 데이터는 __init__ 에서 미리 계산
    self.words = sentence.split()
    self.count = Counter(self.words)
    self.char_count = Counter(sentence.replace(" ", ""))

# 속성 없으면 __init__ 생략 가능
class Calculator:
    def add(self, a, b):
        return a + b
```

---

## 3️⃣ Python 스타일 코드

```python
# 딕셔너리 컴프리헨션 + 조건 필터링
{k: v for k, v in d.items() if v >= 80}

# enumerate + 조건
[v for i, v in enumerate(words) if i % 2 == 0]

# zip + 리스트 컴프리헨션
[x * y for x, y in zip(a, b)]

# 평균 미리 계산 후 필터링
avg = sum(scores) / len(scores)
[x for x in scores if x >= avg]

# 문자열 메서드
"hELLO".capitalize()    # "Hello" ← 첫 글자 대문자, 나머지 소문자
"hello world".title()   # "Hello World" ← 각 단어 첫 글자 대문자
```

---

## ✅ 오늘 주의사항

```python
# 재귀 — 종료 조건 없으면 무한 루프
def f(n):
    return n + f(n-1)   # ❌ 종료 조건 없음

def f(n):
    if n == 0:
        return 0        # ✅ 종료 조건 있음
    return n + f(n-1)

# 평균은 미리 계산
avg = sum(scores) / len(scores)
[x for x in scores if x >= avg]   # ✅ 효율적

# 속성 없으면 __init__ 생략 가능
class Calculator:
    def add(self, a, b):   # __init__ 없어도 됨
        return a + b
```
