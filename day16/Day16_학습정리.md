# 📚 Day 16 파이썬 심화 — 해시 / 딕셔너리 활용

---

## 1️⃣ 해시란?

### 핵심 개념

```
임의의 데이터를 고정된 크기의 숫자로 변환하는 함수

특징
1. 같은 입력 → 항상 같은 출력
2. 다른 입력 → 대부분 다른 출력
3. 출력으로 입력을 역산할 수 없음
```

```python
hash("apple")    # 항상 같은 정수값 반환
hash("banana")   # 다른 정수값
hash("apple")    # 위와 항상 동일
```

### 해시 테이블 동작 원리

```
"apple"  → hash() → 3 → 배열[3] 에 저장
"banana" → hash() → 7 → 배열[7] 에 저장

찾을 때
"apple" 찾기 → hash("apple") → 3 → 배열[3] 바로 접근 → O(1)
```

### 리스트 vs 딕셔너리 속도 차이

```python
# 리스트 — 처음부터 끝까지 탐색
999999 in data_list   # O(n) 느림

# 딕셔너리 — 해시값으로 바로 접근
999999 in data_dict   # O(1) 빠름
```

### 해시 가능 / 불가능

```python
# 해시 가능 — 변경 불가능한 객체 (딕셔너리 키로 사용 가능)
hash(1)           # ✅ int
hash("hello")     # ✅ str
hash((1, 2, 3))   # ✅ tuple

# 해시 불가능 — 변경 가능한 객체 (딕셔너리 키로 사용 불가)
hash([1, 2, 3])   # ❌ list
hash({1: 2})      # ❌ dict
hash({1, 2, 3})   # ❌ set
```

### 해시 충돌

```
다른 입력인데 같은 해시값이 나오는 경우
→ 같은 인덱스에 연결 리스트로 이어서 저장
→ 최악의 경우 O(n)
→ 파이썬은 내부적으로 충돌 최소화 처리
```

### 정리

```
해시 함수   → 데이터를 숫자(인덱스)로 변환
해시 테이블 → 해시값을 인덱스로 쓰는 배열
딕셔너리    → 파이썬의 해시 테이블 구현체
핵심 장점   → 조회 / 삽입 / 삭제 모두 O(1)
핵심 단점   → 메모리를 리스트보다 많이 씀
              해시 충돌 발생 가능
```

---

## 2️⃣ 딕셔너리 심화 활용

### defaultdict

```python
from collections import defaultdict

# 기본값 int (0)
d = defaultdict(int)
d["apple"] += 1
d["apple"] += 1
d["banana"] += 1
print(dict(d))   # {'apple': 2, 'banana': 1}

# 기본값 list ([])
d = defaultdict(list)
d["a"].append(1)
d["a"].append(2)
d["b"].append(3)
print(dict(d))   # {'a': [1, 2], 'b': [3]}
```

### 딕셔너리 정렬

```python
freq = {"apple": 3, "banana": 2, "kiwi": 1}

# value 기준 내림차순
sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
# {'apple': 3, 'banana': 2, 'kiwi': 1}
```

### 딕셔너리 병합 (파이썬 3.9+)

```python
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
merged = a | b   # {'x': 1, 'y': 3, 'z': 4} ← b 가 우선
```

---

## 3️⃣ 해시 활용 패턴

### 애너그램 그룹핑

```python
from collections import defaultdict

def group_anagrams(words: list) -> list:
    groups = defaultdict(list)
    for w in words:
        key = "".join(sorted(w))   # 정렬하면 애너그램끼리 같은 키
        groups[key].append(w)
    return list(groups.values())   # 키 없이 값만 반환

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

### 처음으로 반복되지 않는 문자

```python
from collections import Counter

def first_unique(s: str) -> str:
    freq = Counter(s)
    for c in s:         # 원래 순서대로 순회
        if freq[c] == 1:
            return c
    return None

print(first_unique("leetcode"))   # "l"
print(first_unique("aabb"))       # None
```

### 애너그램 확인

```python
from collections import Counter

def is_anagram(s1: str, s2: str) -> bool:
    return Counter(s1.lower()) == Counter(s2.lower())

print(is_anagram("Listen", "Silent"))   # True
print(is_anagram("hello", "world"))     # False
```

### two_sum — O(n) 풀기

```python
def two_sum(nums: list, target: int) -> list:
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    return []

print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
```

### 중복 찾기

```python
def find_duplicates(nums: list) -> list:
    seen = set()
    result = []
    for n in nums:
        if n in seen:
            result.append(n)
        seen.add(n)
    return result

print(find_duplicates([1, 2, 3, 2, 4, 3]))  # [2, 3]
```

### 그룹핑

```python
students = [("Tom", "A"), ("Jane", "B"), ("Mike", "A")]

groups = defaultdict(list)
for name, dept in students:
    groups[dept].append(name)

print(dict(groups))   # {'A': ['Tom', 'Mike'], 'B': ['Jane']}
```

---

## ✅ 오늘 주의사항

```python
# 1. if ~ return True / return False → return 비교식으로 줄이기
def is_anagram(s1, s2):
    if Counter(s1) == Counter(s2):
        return True
    return False
# ↓ 더 간결하게
def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)   # ✅

# 2. sorted() 결과를 키로 쓸 때
key = str(sorted(w))        # "['a', 'e', 't']" ← 동작하지만 지저분
key = "".join(sorted(w))    # "aet" ✅ 더 간결

# 3. defaultdict vs dict
d = {}
d["key"] += 1               # ❌ KeyError
d = defaultdict(int)
d["key"] += 1               # ✅ 기본값 0 으로 자동 생성

# 4. 리스트는 해시 불가 → 딕셔너리 키로 사용 불가
d[[1, 2]] = 3               # ❌ TypeError
d[(1, 2)] = 3               # ✅ 튜플은 가능
```
