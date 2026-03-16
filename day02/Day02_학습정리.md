# 📚 Day 02 학습 정리
> 튜플 + 정렬 + set + enumerate + zip

---

## 1️⃣ 튜플

```python
t = (1, 5)
t[0]        # 1
t[1]        # 5

# 언패킹
a, b = (1, 5)
a, b = 1, 5   # 괄호 생략 가능

# 리스트와 차이
nums = [1, 2, 3]
nums[0] = 99    # ✅ 수정 가능

t = (1, 2, 3)
t[0] = 99       # ❌ 수정 불가
```

---

## 2️⃣ sorted()

```python
arr = [5, 1, 9, 3]

sorted(arr)                         # [1, 3, 5, 9] 오름차순
sorted(arr, reverse=True)           # [9, 5, 3, 1] 내림차순
sorted(words, key=len)              # 길이 기준 정렬
sorted(data, key=lambda x: x[1])   # 튜플 두 번째 값 기준 정렬

# sorted() vs sort()
sorted(arr)   # 원본 유지, 새 리스트 반환
arr.sort()    # 원본 직접 수정
```

---

## 3️⃣ set

```python
s = set([1, 1, 2, 2, 3])   # 중복 제거 → {1, 2, 3}
list(s)                     # 다시 리스트로 변환

# 집합 연산
a & b   # 교집합
a | b   # 합집합
a - b   # 차집합

# 자주 쓰는 패턴
sorted(set(nums))   # 중복 제거 + 정렬 한 번에
```

---

## 4️⃣ enumerate

```python
for i, v in enumerate(arr):          # 0부터 시작
    print(i, v)

for i, v in enumerate(arr, start=1): # 1부터 시작
    print(i, v)
```

---

## 5️⃣ zip

```python
# 두 리스트 동시 순회
for n, s in zip(names, scores):
    print(n, s)

# 두 리스트 → 딕셔너리로 합치기
result = dict(zip(names, scores))
```

---

## ✅ 오늘 주의사항

```python
# set은 순서 없음 → 인덱스 접근 불가
s = {1, 2, 3}
s[0]   # ❌ 에러

# sorted()는 원본 안 바뀜
arr = [3, 1, 2]
sorted(arr)
print(arr)  # [3, 1, 2] 그대로

# sort()는 원본 바뀜
arr.sort()
print(arr)  # [1, 2, 3]
```
