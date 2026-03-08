# 클래스 - 객체를 만들기 위해 데이터 + 기능을 묶어놓은 것
class Person :
  def __init__(self, name, age): # 생성자
    self.name = name  # this → self
    self.age = age

  def greet(self) : # 메서드 첫 번째 인자는 항상 self
      print("Hello", self.name)

  def info(self):
    print(f"{self.name}은 {self.age}살입니다.")

# 객체 생성
p = Person("Tom", 25)
p.greet() # Hello Tom
p.info() # Tom은 25살 입니다.

# 속성 직접 접근 및 수정도 가능!

# 직접 접근
print(p.name) # Tom
print(p.age) # 25

# 수정
p.age = 26
p.name = "Andy"

p.greet() # Hello Andy
p. info() # Andy은 26살입니다.



# 연습 문제
# 문제 1 - 아래 조건으로 클래스를 직접 구현
# 클래스명: Calculator
# 속성: 없음
# 메서드:
#     add(a, b) → a + b 반환
#     sub(a, b) → a - b 반환
#     mul(a, b) → a * b 반환

class Calculator :
   def add(self, a, b) :
      return a + b
   
   def sub(self, a, b) :
      return a - b
   
   def mul(self, a, b) :
      return a * b
   
c = Calculator()
print(c.add(3, 4))
print(c.sub(5, 2))   
print(c.mul(2, 6))

# 문제 2 - 코드 해석
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name}: 왈왈!")

    def info(self):
        print(f"이름: {self.name}, 나이: {self.age}")

d1 = Dog("초코", 3)
d2 = Dog("콩이", 5)

d1.bark() # 내 답 : 초코: 왈왈!
d2.info() # 내 답 : 이름: 콩이, 나이: 5
