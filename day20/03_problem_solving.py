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


