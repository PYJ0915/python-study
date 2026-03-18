# 타입 힌트 - 변수나 함수에 타입 정보를 명시하는 것
# 1. 예시
# 타입 힌트 X
def add(a, b):
  return a + b

# 타입 힌트 O
def add(a: int, b: int) -> int:
  return a + b
# 타입 힌트는 강제가 아님! -> 실행에는 영향 없고, 코드 가독성과 자동완성에 도움!

# 2. 기본 타입 힌트
# 변수
name: str = "Tom"
age: int = 25
height : float = 175.5
is_student: bool = True

# 함수
def greet(name: str) -> str:
  return f"Hello {name}"

def add(a:int, b:int) -> int:
  return a + b

def nothing() -> None:  # 반환값 없을 때
  print("Hello")

# 3. 컬렉션 타입 힌트
from typing import List, Dict, Tuple, Optional
# 리스트
def sum_nums(nums: List[int]) -> int:
  return sum(nums)

# 딕셔너리
def get_info() -> Dict[str, int]:
  return {"age" : 25}

# 튜플
def min_max(nums: List[int]) -> Tuple[int, int]:
  return min(nums), max(nums)

# Optional - None이 될 수 있을 때
def find(name: str) -> Optional[str]:
  if name == "Tom":
    return "찾았어요!"
  return None

# 4. 실용 예제
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
  
# 1) 학생 데이터 생성
students = [
    Student("Tom", 85),
    Student("Jane", 92),
    Student("Mike", 45),
    Student("Anna", 78),
    Student("John", 60),
    Student("Lisa", 33),
]

# 2) 합격 / 불합격 출력
print("=== 합격 여부 ===")
for s in students:
    result = "합격" if s.is_pass() else "불합격"
    print(f"{s.name}: {s.score}점 → {result}")

# 3) 상위 3명 출력
print("\n=== 상위 3명 ===")
for s in top_students(students, n=3):
    print(f"{s.name}: {s.score}점")

# 4) 특정 학생 찾기
print("\n=== 학생 검색 ===")
name = "Jane"
found = find_student(students, name)
if found:
    print(f"{found.name}: {found.score}점")
else:
    print(f"{name}을 찾을 수 없어요")

# 5) 없는 학생 검색
found = find_student(students, "없는학생")
if found:
    print(f"{found.name}: {found.score}점")
else:
    print("없는학생을 찾을 수 없어요")


