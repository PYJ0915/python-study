# 📚 Day 08 학습 정리
> 표준 라이브러리 + 모듈/import + 파일 구조 분리 + 랜덤 비밀번호 생성기

---

## 1️⃣ 표준 라이브러리

```python
# math
import math
math.sqrt(16)    # 4.0 — 제곱근 (항상 float 반환)
math.ceil(3.2)   # 4   — 올림
math.floor(3.9)  # 3   — 내림
math.pi          # 3.141592...

# 절댓값 — math 아닌 내장 함수
abs(-5)          # 5 ✅
math.abs(-5)     # ❌ 에러 (math에 없음)
math.fabs(-5)    # 5.0 ← float 반환

# random
import random
random.randint(1, 10)           # 1~10 랜덤 정수
random.choice(["a", "b", "c"])  # 리스트에서 랜덤 선택
random.shuffle([1, 2, 3])       # 리스트 섞기

# datetime
from datetime import datetime
now = datetime.now()
now.year / now.month / now.day
now.strftime("%Y년 %m월 %d일")   # 포맷 출력

# string
import string
string.ascii_lowercase   # abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase   # ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits            # 0123456789
```

---

## 2️⃣ import 3가지 방식

```python
# 방식 1 — 모듈 전체
import math
math.sqrt(16)

# 방식 2 — 필요한 것만 (더 많이 씀)
from math import sqrt
sqrt(16)

# 방식 3 — 별명
import math as m
m.sqrt(16)

# 여러 개 한 번에
from math import sqrt, ceil, floor
```

---

## 3️⃣ 모듈 만들기 + if __name__

```python
# utils.py
def add(a, b):
    return a + b

# 직접 실행할 때만 실행
if __name__ == "__main__":
    print(add(3, 4))

# main.py
import utils
utils.add(3, 4)

# utils.py 직접 실행  → __name__ == "__main__" → print 실행 ✅
# main.py 에서 import → __name__ == "utils"    → print 실행 안 됨 ✅
```

---

## 4️⃣ 기능사 스타일 코드 해석 핵심 패턴

```python
# 기본값 인자
def func(x, y=10):
    return x * y

func(3)     # y=10 기본값 사용 → 30
func(3, 4)  # y=4 로 덮어씀 → 12

# 다중 반환 + 언패킹
def calc(a, b):
    return a + b, a * b, a - b

x, y, z = calc(4, 2)   # 6 8 2

# 클래스 흐름 추적
c = Counter()   # count = 0
c.up()          # count = 1
c.up()          # count = 2
c.up()          # count = 3
c.down()        # count = 2
c.value()       # 2

# 리스트 안 리스트 펼치기
def flatten(lst):
    result = []
    for item in lst:
        if type(item) == list:
            result += item       # 리스트면 요소 추가
        else:
            result.append(item)  # 아니면 그대로 추가
    return result

flatten([1, [2, 3], 4, [5, 6]])  # [1, 2, 3, 4, 5, 6]
```

---

## 5️⃣ 파일 구조 분리 패턴

```python
# 폴더 구조
# project/
# ├── main.py       ← 실행 파일
# ├── analyzer.py   ← 클래스 / 함수
# └── data.txt      ← 데이터

# main.py
from analyzer import TextAnalyzer

try:
    with open("data.txt", "r") as f:
        t = TextAnalyzer(f.read())
        t.word_count()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
except:
    print("오류 발생")
```

---

## 6️⃣ 랜덤 비밀번호 생성기 패턴

```python
import random
import string

chars = string.ascii_letters + string.digits + "!@#$%"
length = int(input("길이 입력: "))
password = "".join(random.choice(chars) for _ in range(length))

if length < 6:
    print("약함")
elif length < 10:
    print("보통")
else:
    print("강함")
```

---

## ✅ 오늘 주의사항

```python
# math.sqrt() 는 항상 float
math.sqrt(25)       # 5.0 (5 아님)
int(math.sqrt(25))  # 5 로 변환하려면 int() 필요

# append() vs +=
result.append([2, 3])  # [1, [2, 3]] ← 리스트 자체 추가
result += [2, 3]       # [1, 2, 3]   ← 요소들 추가

# _ 는 사용하지 않는 변수
for _ in range(8):     # i 안 쓸 때 관례적으로 사용
    password += random.choice(chars)

# if __name__ 없으면 import 할 때 코드도 같이 실행됨
```
