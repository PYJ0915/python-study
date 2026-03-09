# while 반복문 - 조건 기반 반복문 (조건이 참인 동안 반복)
# while 조건:
#     실행할 코드

# 기본 예제
i = 1
while i <= 5 :
  print(i)
  i += 1

# 출력
# 1
# 2
# 3
# 4
# 5

# while 무한 루프 - 조건이 항상 참
# while True :
#   print("계속 실행")

# break - 반복문 강제 종료
i = 1
while True : 
  print(i)
  if i == 5 :
    break
  i += 1

# 무한 루프를 break와 함께 사용할 수 있음!
while True :
  quit = input("종료하려면 q 입력 : ")
  if quit == "q" :
    break

# continue - 다음 반복으로 넘어가기
i = 0
while i < 5 :
  i += 1
  if i == 3 :
    continue
  print (i)

  # 출력
  # 1
  # 2
  # 4
  # 5

# while + else - 파이썬에서는 while에도 else가 존재!
i = 1
while i <= 3 :
  print(i)
  i += 1
else :
  print("반복 종료")
  
  # 출력
  # 1
  # 2
  # 3
  # 반복 종료

# else - break 없이 정상 종료될 시 실행되는 코드

# 실전 예제
password = ""

while password != "1234" :
  password = input("비밀번호 입력 : ")

print("로그인 성공!")

# while vs for 차이
# 구분	    while	       |        for
# 기준	조건 기반 반복   | 	횟수/범위 기반 반복
# 사용	조건이 중요할 때 |	정해진 반복 횟수
# 예	  게임 루프	       |  리스트 반복


# 연습 문제
# 문제 1 - 1부터 10까지 숫자를 while문을 사용해서 출력하세요.
i = 0
while i < 10 :
  i += 1
  print(i)

# 문제 2 - 사용자가 q를 입력할 때까지 계속 입력을 받는 프로그램을 만드세요.
text = ""
while True :

  text = input("입력 : ")
  
  if text == "q" :
    print("프로그램 종료")
    break

# 문제 3 - 1부터 100까지 숫자 중에서 짝수만 출력하세요.
i = 0
while i < 100 :
  i += 1
  if i % 2 == 0:
    print(i)