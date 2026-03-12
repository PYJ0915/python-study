# 1️⃣ Python 코드 해석 (6문제)

# 문제 1 
def mystery(n):
    if n == 1:
        return 1
    return n * mystery(n-1)

print(mystery(5)) # 내 답 : 5 * 4 * 3 * 2 * 1 = 120

# 문제 2
nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
print(result) # 내 답 : [4, 16]

# 문제 3
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} 소리를 냅니다"

class Dog(Animal):
    def speak(self):
        return f"{self.name}: 왈왈!"

a = Animal("고양이")
d = Dog("초코")

print(a.speak()) # 내 답 : 고양이 소리를 냅니다
print(d.speak()) # 내 답 : 초코 왈왈!

# 문제 4
d = {"a": 1, "b": 2, "c": 3, "d": 4}
result = {k: v for k, v in d.items() if v % 2 == 0}
print(result) # 내 답 : {"b" : 2, "d" : 4}

# 문제 5 
def func(lst, target=0):
    return [x for x in lst if x > target]

nums = [5, -3, 8, -1, 4]
print(func(nums)) # 내 답 : [5, 8, 4]
print(func(nums, 3)) # 내 답 : [5, 8, 4]

# 문제 6
from collections import Counter

s = "mississippi"
c = Counter(s)
print(c.most_common(2)) # 내 답 : [("i", 4), ("s", 4)]

# 2️⃣ Python 구현 문제 (4문제)

# 문제 7
# 아래 조건으로 함수 구현하기
# - 문자열을 입력받아
# - 각 문자의 빈도수를 딕셔너리로 반환
# - 공백 제외
# - 빈도수 내림차순 정렬해서 반환

# 입력: "hello world"
# 결과: [('l', 3), ('o', 2), ('h', 1), ('e', 1), ('w', 1), ('r', 1), ('d', 1)]
from collections import Counter
def char_freq():
  s = input("문자열 입력 : ")
  return(Counter(s.replace(" ", "")).most_common())
    
print(char_freq())

# 문제 8
# 아래 조건으로 클래스 구현하기
# 클래스명: Stack
# 메서드:
#     push(x)  → 값 추가
#     pop()    → 마지막 값 제거 후 반환 (없으면 "비어있음" 출력)
#     peek()   → 마지막 값 확인 (제거 안 함)
#     size()   → 현재 스택 크기 반환

class Stack:
  def __init__(self):
    self.data = []
    
  def push(self,x):
    self.data.append(x)
  
  def pop(self):
    if len(self.data) == 0:
       print("비어있음")
    else :
      return self.data.pop()

  def peek(self):
     return self.data[len(self.data) - 1]
      
  def size(self):
    return len(self.data)
        
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())   # 3
print(s.pop())    # 3
print(s.size())   # 2

# 문제 9 - 두 리스트에서 공통 요소만 추출 후 정렬
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
# 결과: [3, 4, 5]

result = [x for x in a for y in b if x == y]
print(result)

# 문제 10 - 피보나치 수열 n번째 값 반환 함수 구현
def fib(n) :
   if n <= 2:
      return 1
   return fib(n - 1) + fib(n - 2)

print(fib(5))