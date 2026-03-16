# 📚 Day 04 학습 정리
> Counter + 딕셔너리 정렬 + 애너그램 + 리스트 메서드

---

## 1️⃣ import

```python
# 필요한 것만 가져오기 (더 많이 씀)
from collections import Counter

# 항상 파일 맨 위에 선언
```

---

## 2️⃣ Counter

```python
from collections import Counter

Counter("banana")              # Counter({'a': 3, 'n': 2, 'b': 1})
Counter([1, 2, 2, 3])         # Counter({2: 2, 1: 1, 3: 1})
freq.most_common(1)           # [('a', 3)] ← 1위만
freq.most_common()            # 전체 내림차순

# Counter는 dict 변환 없이 바로 사용 가능
count = Counter(words)        # ✅
count = dict(Counter(words))  # ⚠️ 불필요한 변환
```

---

## 3️⃣ 딕셔너리 정렬

```python
freq = {'a': 3, 'b': 1, 'c': 2}

# value 기준 오름차순
sorted(freq.items(), key=lambda x: x[1])
# [('b', 1), ('c', 2), ('a', 3)]

# value 기준 내림차순
sorted(freq.items(), key=lambda x: x[1], reverse=True)
# [('a', 3), ('c', 2), ('b', 1)]

# 언패킹으로 출력
for k, v in sorted(freq.items(), key=lambda x: x[1], reverse=True):
    print(k, ":", v)
```

---

## 4️⃣ 애너그램 검사

```python
s1, s2 = "listen", "silent"

sorted(s1) == sorted(s2)      # 방법 1
Counter(s1) == Counter(s2)    # 방법 2

# 대소문자 무시할 때
sorted(s1.lower()) == sorted(s2.lower())
```

---

## 5️⃣ 리스트 메서드

```python
nums = [1, 2, 3]

# 추가
nums.append(4)        # [1, 2, 3, 4] ← 맨 뒤에 추가
nums.insert(1, 5)     # [1, 5, 2, 3] ← 특정 위치에 삽입
a.extend([3, 4])      # [1, 2, 3, 4] ← 리스트 합치기

# 제거
nums.pop()            # 마지막 값 제거 후 반환
nums.pop(1)           # 특정 위치 제거
nums.remove(2)        # 특정 값 제거 (첫 번째만)

# 탐색
nums.index(20)        # 해당 값의 인덱스 반환
nums.count(2)         # 해당 값의 개수

# 정렬 / 뒤집기
nums.sort()           # 원본 정렬 (반환값 없음)
sorted(nums)          # 새 리스트 반환 (원본 유지)
nums.reverse()        # 원본 뒤집기
```

---

## ✅ 오늘 주의사항

```python
# Counter는 dict 변환 없이 바로 사용 가능
count = dict(Counter(words))   # ⚠️ 불필요한 변환
count = Counter(words)         # ✅

# 튜플 언패킹으로 간결하게
for c in sorted_list:
    print(c[0], c[1])          # ⚠️ 인덱스 접근
for k, v in sorted_list:
    print(k, v)                # ✅ 언패킹

# append() vs extend()
nums.append([3, 4])   # [1, 2, [3, 4]] ← 리스트 자체가 추가됨
nums.extend([3, 4])   # [1, 2, 3, 4]  ← 요소들이 추가됨

# remove() vs pop()
nums.remove(2)        # 값으로 제거 (첫 번째만)
nums.pop(1)           # 인덱스로 제거
```
