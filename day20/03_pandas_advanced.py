# pandas 심화
import pandas as pd
import numpy as np

# 1. groupby
df = pd.DataFrame({
    "name":   ["Tom", "Jane", "Mike", "Anna", "John", "Lisa"],
    "dept":   ["A", "B", "A", "B", "A", "B"],
    "score":  [85, 92, 78, 95, 88, 73],
    "gender": ["M", "F", "M", "F", "M", "F"]
})

# 기본 groupby
print(df.groupby("dept")["score"].mean())
# dept
# A    83.666667
# B    86.666667

# 여러 집계 함수 한 번에 - agg()
print(df.groupby("dept")["score"].agg(["mean", "max", "min", "count"]))
#            mean  max  min  count
# dept
# A     83.666667   88   78      3
# B     86.666667   95   73      3

# 여러 컬럼 groupby
print(df.groupby(["dept", "gender"])["score"].mean())
# dept  gender
# A     M         83.666667
# B     F         86.666667

# 커스텀 집계
print(df.groupby("dept")["score"].agg(
  평균=("mean"),
  최고점=("max"),
  최저점=("min")
))
#          평균  최고점  최저점
# dept
# A     83.666667   88   78
# B     86.666667   95   73

# 2. merge (테이블 합치기)
# SQL JOIN 과 동일한 개념

students = pd.DataFrame({
    "id":   [1, 2, 3, 4],
    "name": ["Tom", "Jane", "Mike", "Anna"]
})

scores = pd.DataFrame({
    "id":    [1, 2, 3, 5],
    "score": [85, 92, 78, 90]
})

# inner join — 양쪽 다 있는 것만
pd.merge(students, scores, on="id")
#    id  name  score
# 0   1   Tom     85
# 1   2  Jane     92
# 2   3  Mike     78

# left join — 왼쪽 전부
pd.merge(students, scores, on="id", how="left")
#    id  name  score
# 0   1   Tom   85.0
# 1   2  Jane   92.0
# 2   3  Mike   78.0
# 3   4  Anna    NaN  ← 오른쪽에 없으면 NaN

# right join - 오른쪽 전부
pd.merge(students, scores, on="id", how="right")
#    id  name  score
# 0   1   Tom     85
# 1   2  Jane     92
# 2   3  Mike     78
# 3   5   NaN     90

# outer join - 합집합
pd.merge(students, scores, on="id", how="outer")
#    id  name  score
# 0   1   Tom   85.0
# 1   2  Jane   92.0
# 2   3  Mike   78.0
# 3   4  Anna    NaN
# 4   5   NaN   90.0


# 3. pivot_table - 데이터를 요약하거나 재구조화 할때 유용하게 사용
df = pd.DataFrame({
    "name":   ["Tom", "Jane", "Mike", "Anna", "John", "Lisa"],
    "dept":   ["A", "B", "A", "B", "A", "B"],
    "gender": ["M", "F", "M", "F", "M", "F"],
    "score":  [85, 92, 78, 95, 88, 73]
})

pd.pivot_table(
    df,
    values="score",      # 집계할 값
    index="dept",        # 행 기준
    columns="gender",    # 열 기준
    aggfunc="mean"       # 집계 함수
)
# gender      F     M
# dept
# A         NaN  83.67
# B       86.67    NaN


# 4. apply
# 함수를 각 행/열에 적용

# 컬럼에 적용 (기본값)
df["grade"] = df["score"].apply(lambda x:
    "A" if x >= 90 else
    "B" if x >= 80 else
    "C"
)

print(df)
#    name dept gender  score grade
# 0   Tom    A      M     85     B
# 1  Jane    B      F     92     A
# 2  Mike    A      M     78     C
# 3  Anna    B      F     95     A
# 4  John    A      M     88     B
# 5  Lisa    B      F     73     C

# 행에 적용 (axis=1)
df["summary"] = df.apply(
    lambda row: f"{row['name']}({row['dept']}): {row['score']}점",
    axis=1
)

print(df)
#    name dept gender  score grade       summary
# 0   Tom    A      M     85     B   Tom(A): 85점
# 1  Jane    B      F     92     A  Jane(B): 92점
# 2  Mike    A      M     78     C  Mike(A): 78점
# 3  Anna    B      F     95     A  Anna(B): 95점
# 4  John    A      M     88     B  John(A): 88점
# 5  Lisa    B      F     73     C  Lisa(B): 73점


# 5. 문자열 처리 - str accessor
df["name"] = pd.Series(["  Tom  ", "jane", "MIKE"])

print(df["name"].str.strip())       # 공백 제거
# 0     Tom
# 1    jane
# 2    MIKE
# 3     NaN
# 4     NaN
# 5     NaN

print(df["name"].str.lower())       # 소문자
# 0      tom
# 1       jane
# 2       mike
# 3        NaN
# 4        NaN
# 5        NaN

print(df["name"].str.upper())       # 대문자
# 0      TOM
# 1       JANE
# 2       MIKE
# 3        NaN
# 4        NaN
# 5        NaN

print(df["name"].str.contains("a")) # 포함 여부
# 0    False
# 1     True
# 2    False
# 3    False
# 4    False
# 5    False

print(df["name"].str.startswith("T")) # 해당 문자 시작 여부
# 0    False
# 1    False
# 2    False
# 3    False
# 4    False
# 5    False

print(df["name"].str.len())         # 문자열 길이
# 0    7.0
# 1    4.0
# 2    4.0
# 3    NaN
# 4    NaN
# 5    NaN

print(df["name"].str.replace("T", "t")) # 새로운 값으로 일괄적으로 대체


# 6. 날짜 처리
df = pd.DataFrame({
    "date":  ["2026-01-01", "2026-02-15", "2026-03-20"],
    "sales": [100, 200, 150]
})

# 문자열 → datetime 변환
df["date"] = pd.to_datetime(df["date"])

df["year"]  = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"]   = df["date"].dt.day

print(df)
#         date  sales  year  month  day
# 0 2026-01-01    100  2026      1    1
# 1 2026-02-15    200  2026      2   15
# 2 2026-03-20    150  2026      3   20

# 월별 매출 합계
print(df.groupby(df["date"].dt.month)["sales"].sum())
# date
# 1    100
# 2    200
# 3    150


# 7. 데이터 전처리 패턴
# 중복 제거
df.drop_duplicates()
df.drop_duplicates(subset=["name"])   # 특정 컬럼 기준

# 인덱스 재설정
df.reset_index(drop=True)

# 컬럼명 변경
df.rename(columns={"name": "학생명", "score": "점수"})

# 데이터 타입 변환
df["score"] = df["score"].astype(float)

# 구간 나누기
pd.cut(df["score"], bins=[0, 70, 80, 90, 100],
       labels=["D", "C", "B", "A"])


