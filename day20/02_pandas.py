# pandas - 데이터 분석에 특화된 파이썬 라이브러리
# 엑셀처럼 행/열로 이루어진 데이터를 다루는 도구
# numpy  → 수치 계산 (배열)
# pandas → 데이터 분석 (표)
import pandas as pd
import numpy as np

# 1. 핵심 자료 구조
# Series - 1차원 (인덱스 + 값)
s = pd.Series([1, 2, 3, 4, 5])
print(s)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

# 인덱스 직접 설정
s = pd.Series([85, 92, 78], index=["Tom", "Jane", "Mike"])
print(s)
# Tom     85
# Jane    92
# Mike    78
# dtype: int64
print(s["Tom"]) # 85

# DataFrame - 2차원 (행 + 열)
df = pd.DataFrame({
    "name":  ["Tom", "Jane", "Mike"],
    "score": [85, 92, 78],
    "grade": ["B", "A", "C"]
})
print(df)
#    name  score grade
# 0   Tom     85     B
# 1  Jane     92     A
# 2  Mike     78     C

# 2. DataFrame 기본 속성
print(df.shape)     # (3, 3)   ← 행, 열 수
print(df.columns)   # Index(['name', 'score', 'grade'], dtype='str')
print(df.index)     # RangeIndex(start=0, stop=3, step=1)
print(df.dtypes)    # 각 컬럼 데이터 타입
print(df.info())    # 전체 정보 요약
print(df.describe())  # 수치형 컬럼 통계 요약

# 3. 데이터 조회
# 컬럼 선택
print(df["name"])               # name 컬럼 (Series 반환)
print(df[["name", "score"]])    # 여러 컬럼 (DataFrame 반환)

# 행 선택
print(df.loc[0])       # 명시적인 인덱스 레이블(이름)을 기반으로 접근
print(df.iloc[0])      # 정수 기반의 위치(0부터 시작)를 기반으로 접근
print(df.iloc[0:2])    # 0~1번 행

# 조건 필터링
print(df[df["score"] >= 85])
print(df[(df["score"] >= 85) & (df["grade"] == "B")])

# 상위 / 하위
print(df.head(3))   # 상위 3행
print(df.tail(3))   # 하위 3행


# 4. 데이터 수정
# 컬럼 추가
df["bonus"] = df["score"] + 5
print(df)
#    name  score grade  bonus
# 0   Tom     85     B     90
# 1  Jane     92     A     97
# 2  Mike     78     C     83

# 컬럼 수정
df["grade"] = df["score"].apply(lambda x: "A" if x >= 90 else "B")
print(df)
#    name  score grade  bonus
# 0   Tom     85     B     90
# 1  Jane     92     A     97
# 2  Mike     78     B     83

# 컬럼 삭제
df.drop("bonus", axis=1, inplace=True)
print(df)
#    name  score grade
# 0   Tom     85     B
# 1  Jane     92     A
# 2  Mike     78     B

# 값 변경
df.loc[0, "score"] = 100
print(df)
#    name  score grade
# 0   Tom    100     B
# 1  Jane     92     A
# 2  Mike     78     B


# 5. 결측치 처리
df = pd.DataFrame({
    "name":  ["Tom", "Jane", None],
    "score": [85, None, 78],
    "grade": ["B", "A", "C"]
})

print(df.isnull())          # 결측치 여부 (True/False)
#     name  score
# 0  False  False
# 1  False   True
# 2   True  False

print(df.isnull().sum())    # 컬럼별 결측치 개수
# name     1
# score    1
# dtype: int64

print(df.dropna())          # 결측치 있는 행 삭제
#   name  score
# 0  Tom   85.0

print(df.fillna(0))         # 결측치 0으로 채우기
#    name  score
# 0   Tom   85.0
# 1  Jane    0.0
# 2     0   78.0


# 6. 정렬 / 집계
# 정렬
print(df.sort_values("score"))                    # score 오름차순
#    name  score grade
# 2   NaN   78.0     C
# 0   Tom   85.0     B
# 1  Jane    NaN     A

print(df.sort_values("score", ascending=False))   # 내림차순
#   name  score grade
# 0   Tom   85.0     B
# 2   NaN   78.0     C
# 1  Jane    NaN     A

print(df.sort_values(["grade", "score"]))         # 다중 정렬
#    name  score grade
# 1  Jane    NaN     A
# 0   Tom   85.0     B
# 2   NaN   78.0     C

# 집계
print(df["score"].mean())    # 평균   81.5
print(df["score"].sum())     # 합계   163.0
print(df["score"].max())     # 최댓값 85.0
print(df["score"].min())     # 최솟값 78.0
print(df["score"].count())   # 개수   2

# value_counts - 빈도 수
print(df["grade"].value_counts())
# grade
# B    1
# A    1
# C    1
# Name: count, dtype: int64


# 7. CSV 파일 읽기 / 쓰기
# 읽기
df = pd.read_csv("data.csv")
df = pd.read_csv("data.csv", encoding="utf-8")

# 쓰기
df.to_csv("output.csv", index=False)  # index=False → 인덱스 제외