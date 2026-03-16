# 📚 Day 05 학습 정리
> 참조 복사 + 함수 + map() + lambda

---

## 1️⃣ 참조 복사 vs 진짜 복사

```python
# 참조 복사 — 같은 리스트를 가리킴
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4] ← a도 바뀜

# 진짜 복사 — 독립적인 복사본
b = a.copy()
b = a[:]
```

> 💡 자바의 참조(reference) 복사와 같은 개념

---

## 2️⃣ 함수 기본

```python
# 기본 구조
def add(a, b):
    return a + b

# 기본값 인자
def greet(name="guest"):
    print("Hello", name)

greet()        # Hello guest
greet("Tom")   # Hello Tom

# 여러 값 반환 — 튜플 언패킹
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 5])
```

---

## 3️⃣ 함수 작성 주의사항

```python
# ❌ 전역 변수 사용
result = []
def list_add(a, b):
    result.append(a + b)   # 함수 밖 변수 사용

# ✅ 함수 안에서 선언
def list_add(a, b):
    result = []            # 함수 안에서 선언
    return result

# ❌ return print()
def func():
    return print("hello")  # None 반환

# ✅ return 값
def func():
    print("hello")
    return result          # 값 반환
```

---

## 4️⃣ map()

```python
nums = [1, 2, 3]

# map(함수, 리스트) — 각 요소에 함수 적용
list(map(lambda x: x * 2, nums))   # [2, 4, 6]

# 리스트 컴프리헨션과 동일
[x * 2 for x in nums]              # [2, 4, 6]

# map()은 결과가 리스트가 아니라 list()로 감싸야 함
```

---

## 5️⃣ lambda 정리

```python
# 기본
add = lambda a, b: a + b

# 정렬 기준
sorted(nums, key=lambda x: -x)              # 내림차순
sorted(words, key=lambda x: len(x))         # 길이 기준
sorted(d.items(), key=lambda x: x[1])       # value 기준
```

---

## 6️⃣ 오늘 배운 패턴 모음

```python
# 리스트 중복값만 추출
from collections import Counter
nums = [1, 2, 2, 3, 3, 3, 4]
[k for k, v in Counter(nums).items() if v > 1]  # [2, 3]

# 두 리스트 요소합 — 파이써닉
def list_add(a, b):
    return [x + y for x, y in zip(a, b)]

# 공백 제외 문자 빈도수
Counter(sentence.replace(" ", "")).most_common(3)
```

---

## ✅ 오늘 주의사항

```python
# 괄호 한 글자 차이
[x for x in nums]   # [] → 리스트 컴프리헨션 ✅
(x for x in nums)   # () → 제너레이터 ❌ (지금 단계에선 안 씀)

# 평균은 미리 계산
avg = sum(scores) / len(scores)
[x for x in scores if x >= avg]   # ✅ 효율적

# 함수는 독립적으로 동작해야 함
# 전역 변수 사용 ❌ / 함수 안에서 선언 ✅
# return print() ❌ / return 값 ✅
```
