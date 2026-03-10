# 랜덤 비밀번호 생성기

# 기본 버전
import random
chars = "abcdefghijklmnopqrstuvwxyz0123456789"
password = ""
for i in range(8):
  password += random.choice(chars)

print(password) # igx5p80n

# 파이써닉한 버전
chars = "abcdefghijklmnopqrstuvwxyz0123456789"
password = "".join(random.choice(chars) for _ in range(8))
print(password)

# 연습 문제 

# 문제 1 — 기본 생성기
# 조건
# - 길이 6
# - 숫자 + 소문자
chars = "abcdefghijklmnopqrstuvwxyz0123456789"
password = "".join(random.choice(chars) for _ in range(6))
print(password)

# 문제 2
# 조건
# - 길이는 사용자가 입력
# - 소문자 + 대문자 + 숫자 + 특수문자(!@#$%)
# - 생성된 비밀번호 강도 출력
#   길이 6 미만  → "약함"
#   길이 6~9    → "보통"
#   길이 10 이상 → "강함"
chars = "ABCDEFGHIZKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%"
password = "".join(random.choice(chars) for _ in range(int(input("비밀번호 길이를 입력하세요 : "))))

print(password)

length = len(password)

if length < 6 :
  print("비밀번호 강도 : 약함")
elif length < 10 :
  print("비밀번호 강도 : 보통")
else :
  print("비밀번호 강도 : 강함")

# 문제 3 - 예상 출력결과 작성
import random
chars = "abc"
result = [random.choice(chars) for _ in range(3)]
print(result) # 내 답 : [c, b, a], [b, c, b] 등의 abc를 섞은 리스트 발생
# 문제 3 핵심 - 리스트의 값이 중복될 수 있다! ex) [c, c, c]


# 문제 1-2 참고 - 스트링 모듈을 사용하면 더 간결해질 수 있음!
import string

string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits           # 0123456789
string.punctuation      # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# 전부 합치기
chars = string.ascii_letters + string.digits + "!@#$%"
