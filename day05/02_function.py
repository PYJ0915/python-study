# 함수 - 파이썬 함수는 def 키워드로 정의하며, 특정 작업을 수행하는 독립적인 코드 블록
# 함수 기본
def add(a, b) :
    return a + b

print(add(3, 4)) # 7

# 기본값 인자
def greet(name="guest") : 
    print("Hello", name)

greet() # Hello guest
greet("Tom") # Hello Tom

# 여러 값 반환 - 튜플 언패킹
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 4, 1, 5]) # (1, 5)
print(lo, hi) # 1 5

# map(함수, 리스트) 
# 리스트, 튜플 등 반복 가능한 자료형의 모든 요소에 
# 특정 함수를 일괄 적용하여 변환된 결과를 반환하는 내장 함수

# 리스트 컴프리헨션과 비교
nums = [1, 2, 3]

# 리스트 컴프리헨션
print([x * 2 for x in nums]) # [2, 4, 6]

# map()
print(list(map(lambda x: x*2, nums)))
# map() 은 결과가 리스트가 아니라서 리스트로 감싸야함!

# lambda 간단 복습
d = {'a' : 1, 'c' : 3, 'b' : 2}

add = lambda a, b: a + b
sorted(nums, key=lambda x: -x)
sorted(d.items(), key=lambda x: x[1])

# 연습 문제
# 문제 1 - 3 : 아래 코드의 예상 출력 결과를 작성
def add(a, b=2):
    return a + b

print(add(3)) # 내 답 : 5
print(add(3, 4)) # 내 답 : 7

nums = [1, 2, 3]
result = list(map(lambda x: x * 2, nums))
print(result) # 내 답 : [2, 4, 6]

def calc(a, b):
    return a + b, a * b

x, y = calc(3, 4)
print(x, y) # 내 답 : 7 12

# 문제 4 - 두 리스트를 받아서 각 요소의 합을 리스트로 반환하는 함수 만들기
a = [1, 2, 3]
b = [4, 5, 6]

result = []

def list_add(list_a, list_b) :
    for a, b in zip(list_a, list_b) :
        result.append(a + b)
    return print(result)

list_add(a, b)

# 오답 정리
# 1. result를 함수 밖에서 선언
# 2. 값 반환 X, print() 반환하지 않고 출력만 함!

# 내 풀이를 개선한 코드
def list_add(list_a, list_b) :
    result = [] # result를 함수 안에서 선언
    for a, b in zip(list_a, list_b) :
        result.append(a + b)
    return result

a = [1, 2, 3]
b = [4, 5, 6]

print(list_add(a, b))

# 더 파이써닉하게 개선한 코드 (리스트 컴프리헨션과 zip 조합)
def list_add(list_a, list_b) :
    return [a + b for a, b in zip(list_a, list_b)]
