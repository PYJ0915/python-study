# 파일 입출력
# 프로그램 실행 중 외부 파일(txt, csv 등)을 열어 데이터를 읽어오거나(Input), 
# 새로운 데이터를 파일로 저장(Output)하여 영구적으로 보관하는 기능

# 1. 파일 쓰기 - "w" 모드
with open("test.txt", "w") as f:
  f.write("apple\n")
  f.write("banana\n")
  f.write("kiwi\n")

  # test.txt 내용
  # apple
  # banana
  # kiwi

# 2. 파일 읽기 - "r" 모드

# 방법 1 - 한 번에 읽기
with open("test.txt", "r") as f:
  data = f.read()
  print(data)
  # 출력
  # apple
  # banana
  # kiwi

# 방법 2 - 한 줄 씩 읽기
with open("test.txt", "r") as f:
  for line in f:
    print(line.strip())
    # 출력
    # apple
    # banana
    # kiwi

# 방법 3 - 줄 단위 리스트로 읽기
with open("test.txt", "r") as f:
  lines = f.readlines()
  print(lines) # ['apple\n', 'banana\n', 'kiwi\n']


# 3. 파일 추가 - "a" 모드
with open("test.txt", "a") as f:
  f. write("melon\n")
  # test.txt 내용
  # apple
  # banana
  # kiwi
  # melon  ← 추가됨

# 4. "w" 와 "a"의 차이
with open("test.txt", "w") as f:
  f.write("new content\n") 
  # test.txt → "new content" 만 남음

with open("test.txt", "a") as f:
  f.write("add content\n")
  # test.txt → 기존 내용 + "add content"

# 5. 예외 처리 같이 사용
# 파일이 존재하지 않을 때, FileNotFoundError 발생!

try:
  with open("존재하지않는파일.txt", "r") as f:
    data = f.read()
except FileNotFoundError:
  print("파일을 찾을 수 없습니다.")

# 6. 실제 흐름 한 번에 보기
# 1) 파일 쓰기
with open("test.txt", "w") as f:
    f.write("apple\n")
    f.write("banana\n")

# 2) 파일 읽기
with open("test.txt", "r") as f:
    data = f.read()

# 3) 읽은 데이터 활용
words = data.split()
print("단어 개수:", len(words))   # 2

# 연습 문제
# 문제 1. `test.txt` 파일에 아래 내용 쓰고 읽어서 출력하기
# apple
# banana
# kiwi

with open("test.txt", "w") as f:
  f.write("apple\n")
  f.write("banana\n")
  f.write("kiwi\n")

with open("test.txt", "r") as f:
  print(f.read())

# 문제 2. test.txt 파일을 읽어서 단어 개수 출력하기
with open("test.txt", "r") as f:
  data = f.read()

words = data.split()
print("단어 개수 : ", len(words))

# 문제 3 - 예외 처리 추가
try :
  with open("없는파일.txt", "r") as f:
    data = f.read()
except FileNotFoundError:
  print("파일이 존재하지 않습니다.")

