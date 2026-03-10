# 표준 라이브러리

# 1. math
import math
print(math.sqrt(16))    # 4.0 - 제곱근
print(math.ceil(3.2))   # 4 - 올림
print(math.floor(3.9))  # 3 - 내림
print(math.pi)          # 3.141592653589793 - 파이

# math 라이브러리와 비슷한 자주 쓰는 파이썬 내장함수
print(abs(-5))        # 5 - 절댓값
print(round(3.14))    # 3 - 반올림
print(pow(2, 3))      # 8 - 거듭제곱 
print(max([1,2,3]))   # 3 - 최댓값
print(min([1,2,3]))   # 1 - 최솟값
print(sum([1,2,3]))   # 6 - 합계
print(len([1,2,3]))   # 3 - 길이

# 2. random
import random
print(random.randint(1, 10)) # 1~10 사이 랜덤 정수
print(random.choice(["apple", "banana", "kiwi"])) # 리스트에서 랜덤 선택

nums = [1, 2, 3, 4, 5]
random.shuffle(nums) # 리스트 섞기
print(nums) # [4, 1, 5, 2, 3], [2, 3, 4, 1, 5] ...

print(random.random()) # 0.0 ~ 1.0 사이의 랜덤 실수

# 3. datetime
# 일반 import 사용 시 (번거로움)
# import datetime
# now = datetime.datetime.now()

# from import 사용 시 (간결함)
from datetime import datetime
now = datetime.now()

print(now.year) # 2026
print(now.month) # 3
print(now.day) # 10
print(now.hour) # 9
print(now.minute) # 12

# 포맷 출력
print(now.strftime("%Y-%m-%d")) # 2026-03-10
print(now.strftime("%Y-%m-%d %H:%M")) # 2026-03-10 09:13

# 연습 문제
# 문제 1-2. 예상 출력 결과 작성
# 문제 1
import math

print(math.ceil(2.3)) # 내 답 : 3
print(math.floor(2.9))  # 내 답 : 2
print(math.sqrt(25)) # 내 답 : 5

# 문제 2
import random

nums = [1, 2, 3, 4]
print(random.choice(nums)) # 내 답 : 1, 2, 3, 4 중 랜덤 숫자 선택

# 문제 3 - 현재 날짜를 2024년 01월 01일 형식으로 출력
from datetime import datetime
now = datetime.now()
print(now.strftime("%Y년 %m월 %d일"))

# 문제 1-3 개선
# math.sqrt()는 항상 실수 반환!
