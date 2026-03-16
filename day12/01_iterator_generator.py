# 1. 이터레이터 - 값을 하나씩 꺼낼 수 있는 객체

# 동작 방식
nums = [1, 2, 3]
it = iter(nums) # 이터레이터 생성
# print(next(it)) # 1
# print(next(it)) # 2
# print(next(it)) # 3
# print(next(it)) # StopIteration 에러 발생

# 2. 이터레이터 직접 만들기
class Counter:
  def __init__(self, start, end):
    self.current = start
    self.end = end

  def __iter__(self): # iter() 호출 시 실행
    return self
  
  def __next__(self): # next() 호출 시 실행
    if self.current > self.end:
      raise StopIteration
    value = self.current
    self.current += 1
    return value
  

for n in Counter(1, 5):
  print(n)
# 1 2 3 4 5

# 3. 제너레이터 - 이터레이터를 쉽게 만드는 방법 (return 대신 yield 사용)

# 일반 함수
def func():
  return 1  # 실행 끝

# 제너레이터 함수
def gen():
  yield 1   # 여기서 잠깐 멈추고 1 반환
  yield 2   # 다시 실행되면 여기서 멈추고 2 반환
  yield 3

g = gen()
print(next(g)) # 1
print(next(g)) # 2
print(next(g)) # 3

# for문으로도 사용 가능
for n in gen():
  print(n)
  # 1 2 3

# 4. return vs yield 핵심 차이
# return - 함수 종료, 값 한 번만 반환
def func():
  return 1
  return 2  # 실행 안 됨

# yield - 함수 일시 정지, 값 하나씩 반환
def gen():
  yield 1 # 여기서 멈춤
  yield 2 # 다음 호출 시 여기서 재개
  yield 3

# 5. 제너레이터를 사용하는 이유
# 리스트 - 100만 개를 전부 메모리에 올림
nums = [x for x in range(1000000)]  # 메모리 사용량 과다

# 제너레이터 - 필요할 때 하나씩 생성
nums = (x for x in range(1000000)) # 메모리를 거의 안씀

# 괄호 차이
[x for x in range(10)]   # [] → 리스트 컴프리헨션
(x for x in range(10))   # () → 제너레이터 표현식

# 6. 제너레이터 실용 예제

# 무한 수열 생성기
def infinite_counter(start=0):
  n = start
  while True:
    yield n
    n += 1

counter = infinite_counter()
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
# 무한히 계속 ...

# 파일 한 줄씩 읽기 (대용량 파일에서 유용)
def read_lines(filename):
  with open(filename, "r") as f:
    for line in f:
      yield line.strip()

# 연습 문제
# 문제 - 1부터 시작해서 제곱수를 하나씩 반환하는 제너레이터 square_gen(n) 만들기

# 내 풀이
def square_gen(start=1):
  n = start
  while True:
    yield n * n
    n += 1

counter = square_gen()
next(counter)  
next(counter)  
next(counter)  
next(counter)

# 완성 코드
def square_gen(n, start = 1):
  current = start
  for _ in range(n):
    yield current * current
    current += 1

for n in square_gen(5):
  print(n)
  # 1 4 9 16 25
