# numpy - 수치 계산에 특화된 파이썬 라이브러리
# => 행렬 / 배열 연산을 빠르고 간결하게 처리, 데이터 분석의 기반 → pandas, matplotlib 전부 numpy 기반
import numpy as np

# 1. 배열 생성
# 리스트 → numpy 배열 
arr = np.array([1, 2, 3, 4, 5])
print(arr)  # [1 2 3 4 5]
print(type(arr))  # <class 'numpy.ndarray'>

# 2차원 배열
arr2d = np.array([[1, 2, 3],
                 [4, 5, 6]])
print(arr2d.shape)  # (2, 3) ← 2행 3열

# 자주 쓰는 생성 함수
np.zeros(5) # [0. 0. 0. 0. 0.]
np.ones(5)  # [1. 1. 1. 1. 1.]
np.arange(0, 10, 2)  # [0 2 4 6 8]
np.linspace(0, 1, 5) # [0. 0.25 0.5 0.75 1.]
np.random.randint(0, 10, size=5)  # 랜덤 정수 5개
np.random.rand(3, 3)   # 0~1 랜덤 3x3 배열
# [[0.05143447 0.91975963 0.52966339]
#  [0.88411848 0.22949148 0.9142984 ]
#  [0.41399409 0.48244057 0.82210636]]

# NumPy 기본값은 float => 그래서 0이 아니라 0. (= 0.0) 형태로 출력
# => NumPy는 과학 계산용이라서:
# 정수보다 실수 연산이 훨씬 자주 사용됨
# 나눗셈, 평균, 행렬 연산 등에서 자동 변환을 줄이려고 기본을 float로 둠

# cf) 정수로 만들고 싶으면 dtype 지정!
np.zeros(5, dtype=int)  # [0 0 0 0 0]


# 2. 배열 속성
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr.shape)   # (2, 3)  ← 행, 열
print(arr.ndim)     # 2       ← 차원 수
print(arr.size)     # 6       ← 전체 원소 수
print(arr.dtype)    # int64   ← 데이터 타입


# 3. 인덱싱 / 슬라이싱
# 1차원
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])  # 1
print(arr[-1])  # 5
print(arr[1:4])  # [2 3 4]
print(arr[::2])  # [1 3 5]

# 2차원
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print(arr2d[0])         # [1 2 3] ← 첫 번째 행
print(arr2d[0][1])      # 2 
print(arr2d[0, 1])      # 2 ← numpy 스타일 (더 많이 씀)
print(arr2d[:, 1])      # [2 5 8] ← 두 번째 열 전체
print(arr2d[0:2, 1:])   # [[2 3] [5 6]] ← 0~1행, 1~끝 열


# 4. 연산
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 사칙 연산 - 원소별 연산
print(a + b)    # [5 7 9]
print(a - b)    # [-3 -3 -3]
print(a * b)    # [4 10 18]
print(a / b)    # [0.25 0.4  0.5]
print(a ** 2)    # [1 4 9]

# 파이썬 리스트와 차이
print([1, 2, 3] + [4, 5, 6])  # [1, 2, 3, 4, 5, 6]  ← 이어붙임
print(a + b)                  # [5 7 9]          ← 원소별 덧셈


# 5. 브로드캐스팅
# 크기가 다른 배열끼리 연산
arr = np.array([1, 2, 3, 4, 5])

print(arr + 10)   # [11 12 13 14 15]  ← 전체에 10 더함
print(arr * 2)    # [2 4 6 8 10]
print(arr > 3)    # [False False False True True]

# 2차원에서 브로드캐스팅
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])

print(arr2d + 10)
# [[11 12 13]
#  [14 15 16]]


# 6. 통계 함수
# 1차원
arr = np.array([1, 2, 3, 4, 5])

print(np.sum(arr))      # 15      합계
print(np.mean(arr))     # 3.0     평균
print(np.std(arr))      # 1.414   표준편차
print(np.min(arr))      # 1       최솟값
print(np.max(arr))      # 5       최댓값
print(np.median(arr))   # 3.0     중앙값

# 2차원 — 축(axis) 기준
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])

print(np.sum(arr2d, axis=0))   # [5 7 9]  ← 열 기준 합계
print(np.sum(arr2d, axis=1))   # [6 15]   ← 행 기준 합계


# 7. 조건 필터링
arr = np.array([1, 2, 3, 4, 5, 6])

# 조건으로 필터링
print(arr[arr > 3])          # [4 5 6]
print(arr[arr % 2 == 0])     # [2 4 6]

# where — 조건에 따라 값 선택 
# => np.where(조건, true일때 값, false일때 값)
print(np.where(arr > 3, arr, 0))   # [0 0 0 4 5 6]
# 조건 True → arr 값, False → 0


# 8. 배열 반환
arr = np.array([1, 2, 3, 4, 5, 6])

# 형태 변환
# numpy.reshape(행, 열)
print(arr.reshape(2, 3))
# [[1 2 3]
#  [4 5 6]]

print(arr.reshape(3, -1))   # -1 은 자동 계산
# [[1 2]
#  [3 4]
#  [5 6]]

# 펼치기
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])

print(arr2d.flatten())   # [1 2 3 4 5 6]

# 전치 (행열 바꾸기)
print(arr2d.T)
# [[1 4]
#  [2 5]
#  [3 6]]
