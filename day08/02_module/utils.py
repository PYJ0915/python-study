# 직접 모듈 만들기
def add(a, b):
  return a + b

def sub(a, b) :
  return a - b

def is_even(n) :
  return n % 2 == 0

# if __name__ == "__main__" 코드가 존재하지 않을 시 아래 코드가 임포트 시 같이 실행!
# => 원하지 않는 결과 출력!
# print(add(3, 4))   # 테스트용 코드

# __name__ 내장 변수를 이용한 해결법

# __name__ - 스크립트 파일이 직접 실행되는지, 
# 아니면 다른 모듈에 의해 import되어 실행되는지 구분하는 내장 변수 (모든 파일에 자동 생성되는 변수)

# 직접 실행 시 - __name__ == "__main__"
# import 시 - __name__ == "모듈 파일명"

if __name__ == "__main__" :
  print(add(3,4))
# 자바에서의 메인 메서드와 비슷한 역할!
# 해당 파일에서 직접 테스트를 하고싶을 때 사용!

# 실습
def add(a, b):
  return a + b

def mul(a, b):
  return a * b

def is_odd(n):
  return n % 2 != 0

if __name__ == "__main__" :
  print(add(2, 9))
  print(mul(3, 7))
  print(is_odd(9))