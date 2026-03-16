# 📚 Day 01 학습 정리
> 입력 처리 + 기본 구조 + 반복문 + 문자열

---

## 1️⃣ 입력 처리

```python
# 숫자는 변환 필요
n = int(input("숫자 입력: "))   # "3" → 3

# 문자열은 그냥 받으면 됨
s = input("문자열 입력: ")      # "hello" → "hello" 그대로

# input()은 기본적으로 문자열 반환
x = input()       # "3" (문자열)
x = int(input())  # 3  (정수)

"3" + "2"   # "32" ← 문자열 이어붙이기
3 + 2       # 5   ← 숫자 더하기
```

---

## 2️⃣ 리스트

```python
nums = []               # 빈 리스트 생성
nums.append(x)          # 요소 추가
sum(nums)               # 합계
max(nums) / min(nums)   # 최댓값 / 최솟값
len(nums)               # 길이
```

---

## 3️⃣ 반복문 패턴

```python
# 개수 세기
count = 0
for x in nums:
    if 조건:
        count += 1

# 합계 누적
total = 0
for x in nums:
    if 조건:
        total += x

# 최댓값 추적 (조건 있을 때)
max_val = None
for x in nums:
    if 조건:
        if max_val is None or x > max_val:
            max_val = x
```

---

## 4️⃣ 문자열 메서드

```python
s.split()              # 공백 기준 리스트로 분리
"".join(list)          # 리스트 → 문자열로 합치기
s.replace("a", "b")    # 문자 치환
s.strip()              # 앞뒤 공백 제거
s.upper() / s.lower()  # 대소문자 변환
c.isdigit()            # 숫자인지 확인
c.isalpha()            # 알파벳인지 확인
```

---

## 5️⃣ 딕셔너리

```python
d = {}                      # 빈 딕셔너리
d["key"] = value            # 추가 / 수정
d.get("key", 0)             # 조회 (없으면 기본값 0)
"key" in d                  # 키 존재 확인
for k, v in d.items():      # 키 + 값 순회

# 문자 개수 세기 패턴
for c in s:
    count[c] = count.get(c, 0) + 1
```

---

## ✅ 오늘 주의사항

```python
# 파이썬 내장 함수 이름은 변수명으로 쓰지 않기
list = []    # ❌
input = ""   # ❌

# 네이밍은 snake_case
odd_count = 0   # ✅
oddCount = 0    # ❌

# 모음 순서 주의
"aeiouAEIOU"    # ✅
"aieouAIEOU"    # ❌

# join은 문자열 리스트만 가능
"".join([1, 2, 3])         # ❌ 에러
"".join(["1", "2", "3"])   # ✅
```
