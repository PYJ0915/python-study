# 📚 Day 14 파이썬 심화 — 가상환경 / 패키지 관리 + 타입 힌트

---

## 1️⃣ 가상환경

### 가상환경이란?

```
프로젝트마다 독립적인 파이썬 환경을 만드는 것

프로젝트 A — Django 3.0 필요
프로젝트 B — Django 4.0 필요

가상환경 없이 → 둘 중 하나만 설치 가능 ❌
가상환경 있으면 → 각각 독립적으로 관리 ✅
```

### venv 명령어

```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
source venv/Scripts/activate    # Windows Git Bash ✅
venv\Scripts\activate           # Windows CMD
source venv/bin/activate        # Mac / Linux

# 가상환경 비활성화
deactivate

# 활성화 확인 — 터미널 앞에 (venv) 붙으면 성공
(venv) PS C:\python_study>

# python 경로 확인
where python    # Windows
which python    # Mac / Linux
# 가상환경 안의 python 이 첫 번째로 나오면 정상
```

### ⚠️ Windows Git Bash 주의사항

```bash
source venv/Scripts/activate   # ✅ 슬래시(/) 사용
source venv\Scripts\activate   # ❌ 백슬래시 안 됨
```

---

## 2️⃣ pip — 패키지 관리

```bash
# 패키지 설치
pip install requests

# 특정 버전 설치
pip install requests==2.28.0

# 패키지 삭제
pip uninstall requests

# 설치된 패키지 목록
pip list

# 패키지 정보
pip show requests

# 업그레이드
pip install --upgrade requests

# pip 자체 업그레이드
python.exe -m pip install --upgrade pip
```

---

## 3️⃣ requirements.txt

```bash
# 현재 설치된 패키지 저장
pip freeze > requirements.txt

# requirements.txt 로 한 번에 설치
pip install -r requirements.txt
```

```
# requirements.txt 예시
certifi==2026.2.25
charset-normalizer==3.4.6
idna==3.11
requests==2.32.5
urllib3==2.6.3
```

> 💡 협업할 때 requirements.txt 를 공유하면
> 같은 환경을 쉽게 구성할 수 있어요.

---

## 4️⃣ 프로젝트 구조

```
python_study/
├── .gitignore          ← venv/ 추가 필수
├── venv/               ← 가상환경 (git에 올리지 않음)
├── requirements.txt    ← 패키지 목록
├── day01/
├── ...
└── day14/
```

```
# .gitignore 핵심
venv/
__pycache__/
*.pyc
.env
.DS_Store
```

---

## 5️⃣ 타입 힌트

### 기본 타입 힌트

```python
# 변수
name: str = "Tom"
age: int = 25
height: float = 175.5
is_student: bool = True

# 함수
def greet(name: str) -> str:
    return f"Hello {name}"

def add(a: int, b: int) -> int:
    return a + b

def nothing() -> None:       # 반환값 없을 때
    print("hello")
```

### 컬렉션 타입 힌트

```python
from typing import List, Dict, Tuple, Optional

# 리스트
def filter_words(words: List[str], min_len: int) -> List[str]:
    return [w for w in words if len(w) >= min_len]

# 딕셔너리
def word_count(sentence: str) -> Dict[str, int]:
    return dict(Counter(sentence.split()))

# 튜플
def min_max(nums: List[int]) -> Tuple[int, int]:
    return min(nums), max(nums)

# Optional — None 이 될 수 있을 때
def find(name: str) -> Optional[str]:
    if name == "Tom":
        return "찾았어요"
    return None
```

> 💡 파이썬 3.9 이상에서는 List 대신 list 바로 사용 가능
> ```python
> def filter_words(words: list[str], min_len: int) -> list[str]:
> ```

### 실용 예제 — Student 클래스

```python
from typing import List, Optional

class Student:
    def __init__(self, name: str, score: int) -> None:
        self.name = name
        self.score = score

    def is_pass(self) -> bool:
        return self.score >= 60

def top_students(students: List[Student], n: int = 3) -> List[Student]:
    return sorted(students, key=lambda s: s.score, reverse=True)[:n]

def find_student(students: List[Student], name: str) -> Optional[Student]:
    for s in students:
        if s.name == name:
            return s
    return None

# 활용
students = [
    Student("Tom", 85),
    Student("Jane", 92),
    Student("Mike", 45),
    Student("Anna", 78),
]

# 합격 여부
for s in students:
    result = "합격" if s.is_pass() else "불합격"
    print(f"{s.name}: {s.score}점 → {result}")

# 상위 3명
for s in top_students(students, n=3):
    print(f"{s.name}: {s.score}점")

# 학생 검색
found = find_student(students, "Jane")
if found:
    print(f"{found.name}: {found.score}점")
else:
    print("찾을 수 없어요")
```

---

## ✅ 오늘 주의사항

```bash
# Windows Git Bash 가상환경 활성화
source venv/Scripts/activate   # ✅ 슬래시(/)
source venv\Scripts\activate   # ❌ 백슬래시

# 가상환경 활성화 확인
(venv) 앞에 붙으면 성공 ✅
where python 첫 번째 줄이 venv 안이면 정상 ✅
```

```python
# 타입 힌트는 강제가 아님
# 실행에 영향 없고 가독성 + IDE 자동완성에 도움

# Optional — None 반환 가능할 때 반드시 명시
def find(name: str) -> Optional[str]:   # ✅
def find(name: str) -> str:             # ⚠️ None 반환 가능성 숨겨짐
```
