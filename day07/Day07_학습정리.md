# 📚 Day 07 학습 정리
> while 반복문 + 예외처리 + 파일 입출력

---

## 1️⃣ while 반복문

```python
# 기본
i = 1
while i <= 5:
    print(i)
    i += 1
# 1 2 3 4 5

# break — 반복문 강제 종료
while True:
    x = input("입력: ")
    if x == "q":
        break

# continue — 다음 반복으로 넘어가기
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
# 1 2 4 5

# while + else
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("반복 종료")   # break 없이 정상 종료 시 실행
```

### while vs for

| 구분 | while | for |
|------|-------|-----|
| 기준 | 조건 기반 반복 | 횟수/범위 기반 반복 |
| 사용 | 조건이 중요할 때 | 정해진 반복 횟수 |
| 예 | 게임 루프 | 리스트 반복 |

---

## 2️⃣ 예외처리

```python
# 기본 구조
try:
    실행 코드
except ValueError:
    ValueError 발생 시
except ZeroDivisionError:
    ZeroDivisionError 발생 시
else:
    예외 없을 때만 실행
finally:
    항상 실행

# 자주 나오는 예외
int("abc")           # ValueError
10 / 0               # ZeroDivisionError
[1,2,3][5]           # IndexError
{"a":1}["b"]         # KeyError
open("없는파일.txt")  # FileNotFoundError
```

> ⚠️ 주의사항
> - try 블록에서 예외 발생 시 → 그 줄에서 즉시 멈춤
> - else → 예외 없을 때만 실행
> - finally → 예외 여부 상관없이 항상 실행
> - break 쓰면 else 실행 안 됨

---

## 3️⃣ 파일 입출력

```python
# 파일 모드
# "r" → 읽기 (파일 없으면 FileNotFoundError)
# "w" → 쓰기 (없으면 생성, 있으면 덮어씀 ⚠️)
# "a" → 추가 (없으면 생성, 있으면 이어씀 ✅)

# 쓰기
with open("test.txt", "w") as f:
    f.write("내용\n")

# 추가
with open("test.txt", "a") as f:
    f.write("추가 내용\n")

# 읽기 — 전체
with open("test.txt", "r") as f:
    data = f.read()

# 읽기 — 한 줄씩
with open("test.txt", "r") as f:
    for line in f:
        print(line.strip())

# 읽기 — 한 줄로
with open("test.txt", "r") as f:
    words = f.read().split()

# 파일 + 예외처리 패턴
try:
    with open("text.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
except:
    print("오류 발생")
```

---

## ✅ 오늘 주의사항

```python
# while — break 쓰면 else 실행 안 됨
# 짝수처럼 범위 정해진 건 for가 더 자연스러움
for i in range(2, 101, 2):   # 짝수 출력
    print(i)

# "w" vs "a"
"w"  # 덮어씀 (기존 내용 사라짐) ⚠️
"a"  # 이어씀 (기존 내용 유지) ✅

# try 블록 예외 발생 시 → 그 줄에서 즉시 멈춤
try:
    x = int("abc")   # ← 여기서 멈춤
    y = x / 0        # ← 실행 안 됨
except ValueError:
    print("A")
```
