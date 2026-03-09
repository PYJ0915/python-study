# 예외 처리 
# 프로그램 실행 중 발생할 수 있는 예상치 못한 오류(예외)에 미리 대처하여 
# 프로그램의 갑작스러운 종료를 막고 안정성을 유지하는 기능

# 예외 처리 없을 때 → 프로그램 종료
# x = int("abc") # ValueError: invalid literal for int() with base 10: 'abc'

# 예외 처리 있을 때 → 오류 처리 후 계속 실행
try:
  x = int("abc")
except :
  print("오류 발생")
print("프로그램 실행 중...") # 출력됨

# 기본 구조 4가지
# try:
#     실행 코드
# except:
#     오류 발생 시
# else:
#     오류 없을 시
# finally:
#     항상 실행

# 특정 예외 처리
try:
  x = int("abc")
except ValueError :
  print("숫자 변환 오류 발생")

try:
  x = 10 / 0
except ZeroDivisionError:
  print("0으로 나눌 수 없음")

# 자주 나오는 예외 종류 모음
#       예외        |   발생 상황
#  ValueError       |  잘못된 타입 변환 (int("abc"))
# ZeroDivisionError |  0으로 나누기 (10 / 0)
#   IndexError      |  범위 벗어난 인덱스 ([1,2,3][5])
#   KeyError        |  없는 딕셔너리 키 (d["없는키"])
# FileNotFoundError |  없는 파일 열기


# 연습 문제
# 문제 1-2 예상 출력 결과 작성
# 문제 1 - X 
try:
    x = int("10")
    y = x / 0
except ValueError:
    print("A")
except ZeroDivisionError:
    print("B")
else:
    print("C")
finally:
    print("D")

# 내 답 : A B D
# 실제 답 : B D

# 문제 2 - O
try:
    nums = [1, 2, 3]
    print(nums[5])
except IndexError:
    print("인덱스 오류")
except:
    print("기타 오류")
finally:
    print("종료")

# 내 답 : 인덱스 오류 종료

# 문제 3 — 사용자로부터 숫자를 입력받아 100을 나누는 프로그램 직접 구현 - O

# 두 가지 예외 처리 추가하기
# 1. 숫자가 아닌 값 입력 시 → "숫자를 입력하세요"
# 2. 0 입력 시 → "0으로 나눌 수 없습니다"

try :
   print(100 / int(input("입력 : ")))
except ValueError:
   print("숫자를 입력해주세요.")
except ZeroDivisionError:
   print("0으로 나눌 수 없습니다.")


# 문제 1 오답정리
# "10" 은 숫자 모양의 문자열이라 int() 로 변환 가능!
#  그래서 ValueError 가 안 나고 다음 줄 x / 0 에서 ZeroDivisionError 발생

# 정리
# int("10")     # ✅ 성공 → 10
# int("10.5")   # ❌ ValueError
# int("abc")    # ❌ ValueError
# int("")       # ❌ ValueError

try:
    x = int("10")   # ← "10"은 숫자로 변환 가능 → 성공 / 만약 여기서 에러 발생 시 바로 ValueError로 넘어가게 되어 정답은 A D
    y = x / 0       # ← 0으로 나누기 → ZeroDivisionError 발생
except ValueError:
    print("A")
except ZeroDivisionError:
    print("B")      # ← 여기 걸림
else:
    print("C")      # ← 예외 발생했으니 실행 안 됨
finally:
    print("D")      # ← 항상 실행
 