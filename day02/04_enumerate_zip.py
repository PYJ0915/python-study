# enumerate(열거하다) - 인덱스 + 값 동시에
# => 반복 가능한(iterable) 객체를 순회할 때, 인덱스(순번)와 요소를 동시에 반환해주는 내장 함수
arr = ["a", "b", "c"]

# 자바 Ver.
for i in range(len(arr)) :
  print(i, arr[i])

# 파이썬 Ver.
for i, v in enumerate(arr) :
  print(i, v)

  # 0 a
  # 1 b
  # 2 c

# 시작 인덱스 변경 가능!
for i, v in enumerate(arr, start=1) :
  print(i, v) 
  # 1 a
  # 2 b
  # 3 c

# zip — 두 리스트 동시에 순회
# => 반복 가능한(iterable) 객체(리스트, 튜플, 문자열 등)를 인자로 받아, 
#     각 객체의 동일한 인덱스 요소를 튜플 형태로 묶어주는 내장 함수
names = ["철수", "영희", "민수"]
scores = [80, 90, 70]

for n, s in zip(names, scores) :
  print(n, s) 
  # 철수 80
  # 영희 90
  # 민수 70

# zip + dict — 자주 쓰는 패턴
result = dict(zip(names, scores))
print(result)

# 연습 문제

# 문제 4 — zip으로 묶어 출력
name_list = ["Tom", "Jane", "Mike"]
ages = [25, 30, 22]

for n, a in zip(name_list, ages) :
  print(n, a)

# 문제 5 — enumerate로 출력
words = ["apple", "banana", "kiwi"]

for i, v in enumerate(words) :
  print(i, v)