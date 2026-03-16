# 📚 Day 03 학습 정리
> 슬라이싱 + 리스트/딕셔너리 컴프리헨션 + 빈도수 패턴

---

## 1️⃣ 슬라이싱

```python
s = "hello"

s[0:3]    # "hel" ← 0, 1, 2 (끝 미포함)
s[:3]     # "hel" ← 처음부터
s[1:]     # "ello" ← 끝까지
s[:]      # "hello" ← 전체
s[::-1]   # "olleh" ← 뒤집기
s[::2]    # "hlo" ← 2칸씩

# 리스트도 동일
nums[::-1]   # 리스트 뒤집기
```

---

## 2️⃣ 리스트 컴프리헨션

```python
# 기본
result = [x * 2 for x in nums]

# 조건 추가
evens = [x for x in nums if x % 2 == 0]

# 기존 방식과 비교
result = []
for x in nums:
    result.append(x * 2)
# ↓ 한 줄로
result = [x * 2 for x in nums]
```

---

## 3️⃣ 딕셔너리 컴프리헨션

```python
words = ["apple", "cat", "banana"]

# 단어 : 길이 딕셔너리
result = {w: len(w) for w in words}
# {'apple': 5, 'cat': 3, 'banana': 6}
```

---

## 4️⃣ dict.get() 빈도수 패턴

```python
freq = {}
for c in word:
    freq[c] = freq.get(c, 0) + 1

# "banana" → {'b': 1, 'a': 3, 'n': 2}
```

---

## 5️⃣ 문자열 알고리즘

```python
# 뒤집기
s[::-1]

# 회문 검사
s == s[::-1]   # "level" → True
```

---

## ✅ 오늘 주의사항

```python
# 두 번째로 큰 수 — 중복 있을 때 set() 먼저
sorted(set(nums), reverse=True)[1]  # ✅
sorted(nums, reverse=True)[1]       # ⚠️ 중복 있으면 틀림

# 최댓값/최솟값 — sorted()[0] 보다 max/min이 간결
max(words, key=len)                         # ✅
sorted(words, reverse=True, key=len)[0]     # ⚠️ 불필요하게 길다

# 괄호 한 글자 차이
[x for x in nums]   # [] → 리스트 컴프리헨션 ✅
(x for x in nums)   # () → 제너레이터 (지금 단계에선 안 씀)
{x for x in nums}   # {} → 셋 컴프리헨션
```
