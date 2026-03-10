# 모듈 - 함수, 클래스, 변수들을 모아놓은 .py 파일 (파이썬 파일 자체)

# import 3가지 방식
# 방식 1 - 모듈 전체 가져오기
import math
math.sqrt(16) # 사용 시 모듈명 붙여야함!

# 방식 2 - 필요한 것만 가져오기
from math import sqrt
sqrt(16) # 바로 사용 가능

# 방식 3 - 별명 붙이기
import math as m
m.sqrt(16) # 별명으로 사용

# cf) 여러 개 한 번에
from math import sqrt, ceil, floor
sqrt(16)
ceil(3.2)
floor(2.6)

# 직접 만든 모듈 임포트해서 사용
import utils # 7 (if __name__ == "__main__" 코드가 없을 시)
print(utils.add(3, 4))  # 7
print(utils.sub(5, 2))  # 3
print(utils.is_even(3)) # false

# 실습
import utils
print(utils.add(3, 4))
print(utils.mul(2, 5))
print(utils.is_odd(3))

from utils import is_even
print(is_even(4))

import utils as u
print(u.mul(3, 6))