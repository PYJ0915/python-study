# 리스트 컴프리헨션 
# => 반복문과 조건문을 사용하여 기존 리스트나 반복 가능한 객체를 기반으로 
#     새로운 리스트를 한 줄로 간결하게 생성하는 문법

# nums 리스트의 값이 두 배가 되는 새로운 리스트 만들기
nums = [1, 2, 3, 4, 5, 6]

# 기존 방식
result = []
for x in nums :
  result.append(x * 2)

print(result) # [2, 4, 6, 8, 10, 12]

# 리스트 컴프리헨션 방식 
res = [x * 2 for x in nums]
print(res) # [2, 4, 6, 8, 10, 12]

# 짝수만 뽑아 새로운 리스트 만들기

# 기존 방식
evens = []
for x in nums :
  if x % 2 == 0 :
    evens.append(x)
print(evens) # [2, 4, 6]

# 리스트 컴프리헨션 방식
even_list = [x for x in nums if x % 2 == 0]
print(even_list) # [2, 4, 6]

# 연습문제

# 문제 1 — 홀수만 추출
odds = [x for x in nums if x % 2 != 0]
print(odds)

# 문제 2 — 제곱 리스트 생성
num_list = [1, 2, 3, 4]
squares = [x * x for x in num_list]
print(squares)

# 문제 3 — 두 번째로 큰 수 찾기
nums = [4, 1, 9, 3, 7]
print(sorted(nums, reverse=True)[1])

# 위의 풀이에는 중복 방지가 없음!

# 중복방지 추가한 풀이
print(sorted(set(nums), reverse=True)[1])

# 문제 4 — 문자 빈도수 구하기
word = "banana"
freq = {}

for c in word :
  freq[c] = freq.get(c, 0) + 1

print(freq)