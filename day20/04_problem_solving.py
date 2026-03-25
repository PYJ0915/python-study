# 실습 문제
import numpy as np
import pandas as pd
# 문제 1 - 아래 조건으로 numpy 배열을 만들고 출력

# 1. 1부터 20까지 배열 생성
arr = np.array([x + 1 for x in range(20)])

# 2. 4행 5열로 변환
print(arr.reshape(4, 5))

# 3. 3보다 크고 10보다 작은 값만 추출
arr1 = arr[arr > 3]
print(arr1[arr1 < 10])


# 문제 2 - 아래 성적 데이터를 numpy 로 분석
scores = np.array([85, 92, 78, 95, 88, 73, 90, 82])

# 1. 평균, 최고점, 최저점 출력
print(np.mean(scores))
print(np.max(scores))
print(np.min(scores))

# 2. 평균 이상인 점수만 추출
print(scores[scores >= np.mean(scores)])

# 3. 모든 점수에 5점 보너스 추가
print(scores + 5)

# 4. 90점 이상이면 "A", 아니면 "B" 로 변환
print(np.where(scores >= 90, "A", "B"))


# 문제 3 - 아래 두 행렬의 연산
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# 1. 원소별 곱셈
print(a * b)

# 2. 행렬 곱셈 (np.dot)
print(np.dot(a, b))
# a = [[1,2],[3,4]]
# b = [[5,6],[7,8]]

# [1*5+2*7, 1*6+2*8]   [19, 22]
# [3*5+4*7, 3*6+4*8] = [43, 50]

# 3. a 의 전치행렬
print(a.T)

# 4. a + b 의 각 행 합계
print(np.sum(a + b, axis=1))


# 문제 4 -  아래 데이터로 DataFrame 만들고 분석
data = {
    "name":   ["Tom", "Jane", "Mike", "Anna", "John"],
    "score":  [85, 92, 78, 95, 88],
    "dept":   ["A", "B", "A", "B", "A"]
}

# 1. DataFrame 생성
df = pd.DataFrame(data)

# 2. score 내림차순 정렬
df.sort_values("score", ascending=False)

# 3. score 가 85 이상인 학생만 추출
df[df["score"] >= 85]

# 4. 평균, 최고점, 최저점 출력
print(df["score"].mean())
print(df["score"].max())
print(df["score"].min())

# 5. score 가 90 이상이면 "pass", 아니면 "fail" 컬럼 추가
df["pass/fail"] = np.where(df["score"] >= 90, "pass", "fail")
print(df)


# 문제 5 - 아래 조건으로 데이터를 분석
# 위 data 에서

# 1. dept 별 평균 score
print(df.groupby("dept")["score"].mean())

# 2. dept 별 학생 수
print(df.groupby("dept")["name"].count())

# 3. score 상위 3명 이름 출력
print(df.sort_values("score", ascending=False).head(3))


# 문제 6 - 아래 데이터로 groupby 분석
df = pd.DataFrame({
    "name":   ["Tom", "Jane", "Mike", "Anna", "John", "Lisa"],
    "dept":   ["A", "B", "A", "B", "A", "B"],
    "score":  [85, 92, 78, 95, 88, 73],
    "gender": ["M", "F", "M", "F", "M", "F"]
})

# 1. dept 별 평균, 최고점, 최저점, 인원수
print(df.groupby("dept")["score"].agg(["mean", "max", "min", "count"]))

# 2. dept + gender 별 평균 score
print(df.groupby(["dept", "gender"])["score"].mean())

# 3. 전체 평균보다 높은 dept 만 출력
print(df["dept"][df["score"] > df["score"].mean()])


# 문제 7 - 아래 두 테이블을 merge
students = pd.DataFrame({
    "id":   [1, 2, 3, 4],
    "name": ["Tom", "Jane", "Mike", "Anna"]
})

scores = pd.DataFrame({
    "id":    [1, 2, 3, 5],
    "score": [85, 92, 78, 90]
})

# 1. inner join
print(pd.merge(students, scores, on="id"))

# 2. left join
left_join = pd.merge(students, scores, on="id", how="left")

# 3. 합친 결과에서 score 가 없는 학생 이름 출력
print(left_join[left_join["score"].isnull()]["name"])


# 문제 8 - apply 로 아래 컬럼을 추가
# df 에서
# 1. score 가 90 이상 → "A"
#           80 이상 → "B"
#           70 이상 → "C"
#           나머지  → "D"
df["grade"] = df["score"].apply(lambda x:
  "A" if x >= 90 else
  "B" if x >= 80 else
  "C" if x >= 70 else
  "D"
)

print(df)


# 2. "이름(부서): 점수점" 형식의 summary 컬럼 추가
df["summary"] = df.apply(
  lambda row : f"{row['name']}({row['dept']}): {row['score']}점",
  axis=1
)

print(df)


# 개선된 풀이
# 문제 1 - 더 간결하게

# 지금 코드
arr = np.array([x + 1 for x in range(20)])

# numpy 스타일
arr = np.arange(1, 21)   # ✅ 더 간결

# 지금 코드 — 두 번에 나눠서
arr1 = arr[arr > 3]
print(arr1[arr1 < 10])

# 한 번에
print(arr[(arr > 3) & (arr < 10)])   # ✅ & 로 조건 합치기

# 문제 5 - 이름만 출력
# 지금 코드 — 전체 행 출력
print(df.sort_values("score", ascending=False).head(3))

# 이름만 출력
print(df.sort_values("score", ascending=False).head(3)["name"].values)
# ['Anna' 'Jane' 'John']

# 문제 6 - 의도 파악
# 지금 코드 — score 가 평균보다 높은 행의 dept 출력
print(df["dept"][df["score"] > df["score"].mean()])
# 0    A
# 1    B
# 4    A

# 문제 의도는 dept 별 평균이 전체 평균보다 높은 dept
dept_mean = df.groupby("dept")["score"].mean()
total_mean = df["score"].mean()
print(dept_mean[dept_mean > total_mean].index.tolist())
# ['B']  ← B부서 평균(86.67) > 전체 평균(85.17)


