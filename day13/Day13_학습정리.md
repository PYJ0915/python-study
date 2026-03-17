# 📚 Day 13 파이썬 심화 — 컨텍스트 매니저 + 정규표현식

---

## 1️⃣ 컨텍스트 매니저

### 핵심 개념

```
"작업 전 준비 → 작업 → 작업 후 정리" 를 자동으로 해주는 객체
with문 과 함께 사용
핵심 장점 → 에러가 나도 정리(finally)는 무조건 실행
```

### 왜 필요할까?

```python
# ❌ 컨텍스트 매니저 없이
f = open("file.txt", "r")
data = f.read()
# 여기서 에러 발생하면 f.close() 실행 안 됨 → 메모리 누수

# ✅ 컨텍스트 매니저 사용
with open("file.txt", "r") as f:
    data = f.read()
# 에러나도 무조건 f.close() 실행
```

### __enter__ / __exit__ 직접 구현

```python
class MyContext:
    def __enter__(self):
        print("1. 준비")      # with 블록 진입 시 실행
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("3. 정리")      # with 블록 종료 시 실행 (에러 여부 상관없이)
        return False          # False → 예외 그대로 전달
                              # True  → 예외 무시

with MyContext():
    print("2. 작업")
# 1. 준비
# 2. 작업
# 3. 정리
```

### @contextmanager — 더 간단하게

```python
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    f = open(filename, mode)
    try:
        yield f         # with 블록에 f 전달, 여기서 with 블록 실행
    finally:
        f.close()       # 블록 끝나면 항상 실행

with file_manager("test.txt", "w") as f:
    f.write("hello")
```

### yield 역할

```python
@contextmanager
def timer():
    start = time.time()
    yield               # 여기서 with 블록에 제어권 넘김
    end = time.time()   # with 블록 끝나면 여기서 재개

# yield 값 없음 → as 로 받으면 None
with timer() as t:
    print(t)   # None

# yield 값 있음 → as 로 받을 수 있음
@contextmanager
def temp_dir(path):
    os.makedirs(path, exist_ok=True)
    try:
        yield path      # path 전달
    finally:
        os.rmdir(path)

with temp_dir("temp") as p:
    print(p)   # "temp"
```

### 실용적인 활용 예제

```python
import time
import os
from contextlib import contextmanager

# 실행 시간 측정
@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f"실행 시간: {end - start:.4f}초")

with timer():
    time.sleep(1)
# 실행 시간: 1.0012초

# 임시 디렉토리
@contextmanager
def temp_dir(path):
    os.makedirs(path, exist_ok=True)
    try:
        yield path
    finally:
        os.rmdir(path)

# 로그 출력
@contextmanager
def log_context(s):
    print("[시작]", s)
    try:
        yield
    finally:
        print("[완료]", s)

with log_context("데이터 처리"):
    print("처리 중...")
# [시작] 데이터 처리
# 처리 중...
# [완료] 데이터 처리
```

### 컨텍스트 매니저가 쓰이는 곳

```python
with open("file.txt") as f:         # 파일 입출력
with db.connect() as conn:          # DB 연결
with requests.Session() as s:       # 네트워크 요청
with lock:                          # 멀티스레딩 락
with timer():                       # 실행 시간 측정
```

### 자바와 비교

```
자바 try-with-resources  ↔  파이썬 with문
자바 AutoCloseable       ↔  파이썬 __exit__
```

---

## 2️⃣ 정규표현식

### 자주 쓰는 패턴

```python
# 문자 종류
\d        # 숫자 [0-9]
\D        # 숫자 아닌 것
\w        # 문자 + 숫자 + _ [a-zA-Z0-9_]
\s        # 공백 (스페이스, 탭, 줄바꿈)
.         # 아무 문자 1개 (줄바꿈 제외)

# 반복
*         # 0번 이상
+         # 1번 이상
?         # 0번 또는 1번
{n}       # 정확히 n번
{n,m}     # n번 이상 m번 이하

# 위치
^         # 문자열 시작
$         # 문자열 끝

# 묶음
[abc]     # a 또는 b 또는 c
[a-z]     # a 부터 z 까지
[^abc]    # a, b, c 제외한 모든 문자
```

### re 모듈 주요 함수

```python
import re

text = "apple 123 banana 456"

# findall — 모든 매칭 리스트로 반환
re.findall(r"\d+", text)            # ['123', '456']

# search — 첫 번째 매칭 찾기 (위치 상관없이)
m = re.search(r"\d+", text)
m.group()                           # "123"
m.start()                           # 6 ← 시작 인덱스
m.end()                             # 9 ← 끝 인덱스

# match — 문자열 시작부터만 매칭
re.match(r"\d+", text)              # None ← 시작이 숫자 아님
re.match(r"\w+", text).group()      # "apple"

# sub — 매칭된 부분 치환
re.sub(r"\d+", "###", text)         # "apple ### banana ###"

# split — 패턴 기준으로 분리
re.split(r"\s+", text)              # ['apple', '123', 'banana', '456']
```

### search vs match 차이

```python
text = "hello 123"

re.search(r"\d+", text)   # ✅ 중간에서도 찾음 → "123"
re.match(r"\d+", text)    # ❌ 시작부터 매칭 안 됨 → None
re.match(r"\w+", text)    # ✅ 시작부터 매칭 → "hello"
```

### 그룹 — 패턴 일부만 추출

```python
# () 로 원하는 부분만 감싸기
text = "2026-03-17"
m = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
m.group(0)   # "2026-03-17" ← 전체
m.group(1)   # "2026" ← 첫 번째 그룹
m.group(2)   # "03"   ← 두 번째 그룹
m.group(3)   # "17"   ← 세 번째 그룹

# findall + 그룹 → 그룹만 반환
text = "hello@gmail.com world@naver.com"
re.findall(r"([\w]+)@", text)       # ['hello', 'world'] ✅
re.findall(r"[\w]+@", text)         # ['hello@', 'world@'] ❌ @ 포함
re.findall(r"[\w]+(?=@)", text)     # ['hello', 'world'] ✅ lookahead
```

### 실용적인 예제

```python
import re

# 날짜 추출
text = "회의: 2026-03-17, 마감: 2026-04-01"
re.findall(r"\d{4}-\d{2}-\d{2}", text)
# ['2026-03-17', '2026-04-01']

# 이메일 추출
text = "hello@gmail.com world@naver.com"
re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)
# ['hello@gmail.com', 'world@naver.com']

# 전화번호 추출
text = "010-1234-5678 또는 02-123-4567"
re.findall(r"\d{2,3}-\d{3,4}-\d{4}", text)
# ['010-1234-5678', '02-123-4567']

# 숫자만 제거
re.sub(r"\d", "", "abc123def456")   # "abcdef"

# 공백 여러 개 → 하나로
re.sub(r"\s+", " ", "hello    world")  # "hello world"
```

---

## ✅ 오늘 주의사항

```python
# 1. r"..." — raw string 필수
re.findall("\d+", text)    # ⚠️ \d 가 특수문자로 해석될 수 있음
re.findall(r"\d+", text)   # ✅ raw string 으로 써야 안전

# 2. findall + 그룹 → 그룹만 반환
re.findall(r"([\w]+)@", text)   # @ 제외하고 앞부분만 반환

# 3. search vs match
re.search → 문자열 어디서든 찾음
re.match  → 문자열 시작부터만 찾음

# 4. yield 는 with 블록에 제어권 넘기는 것
# with 블록 안 함수 결과는 yield 와 무관
with timer():
    result = some_function()   # 결과는 직접 변수에 담아야 함
```
