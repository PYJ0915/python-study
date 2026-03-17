# 컨텍스트 매니저 - "작업 전 준비 → 작업 → 작업 후 정리" 를 자동으로 해주는 것

# 1. with문 복습
with open("test.txt", "r") as f:
  data = f.read()
# with 블록이 끝나면 자동으로 f.close() 호출 => 블록이 끝나면 자동으로 정리

# 2. 컨텍스트 매니저 직접 만들기
class FileManager:
  def __init__(self, filename, mode):
    self.filename = filename
    self.mode = mode

  def __enter__(self):  # with 블록 시작 시 실행
    self.file = open(self.filename, self.mode)
    return self.file
  
  def __exit__(self, exc_type, exc_val, exc_tb): # with 블록 끝날 때 실행
    self.file.close()
    return False  # 예외 발생 시 그대로 전달
  
with FileManager("test.txt", "w") as f:
  f.write("hello")
# 블록 끝나면 자동으로 __exit__ 실행 → f.close()

# 3. contextlib - 더 간단하게 만들기 (클래스 없이 함수로)
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
  f = open(filename, mode)
  try:
    yield f   # with 블록에 f전달
  finally:
    f.close()  # 블록 끝나면 항상 실행

with file_manager("test.txt", "a") as f:
  f.write("\nHI")

# 4. 실전 활용 예제
# 실행 시간 측정
import time

@contextmanager
def timer():
  start = time.time()
  yield    # ← 여기서 with 블록에 제어권 넘김
  end = time.time() # ← with 블록 끝나면 여기서 재개
  print(f"실행 시간: {end - start:.4f}초")

with timer():
  time.sleep(1)

# 임시 디렉토리
import os
@contextmanager
def temp_dir(path):
  os.makedirs(path, exist_ok=True)
  try:
    yield path
  finally:
    os.rmdir(path)

# 임시 디렉토리 테스트
print("before:", os.path.exists("temp"))  # False — 아직 없음

with temp_dir("temp") as p:
  print("inside:", os.path.exists("temp"))  # True — 생성됨
  print("path:", p)   # "temp"

try:
    with temp_dir("temp") as p:
        print("inside:", os.path.exists("temp"))  # True
        raise Exception("에러 발생!")              # 강제 에러
except Exception as e:
    print("에러:", e)

print("after:", os.path.exists("temp"))   # False — 에러나도 삭제됨
