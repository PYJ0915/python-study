# 📚 Day 20 파이썬 심화 — numpy + pandas 기초

---

# 1부 — numpy

## 1️⃣ numpy란?

```
수치 계산에 특화된 파이썬 라이브러리
행렬 / 배열 연산을 빠르고 간결하게 처리
데이터 분석의 기반 → pandas, matplotlib 전부 numpy 기반
```

---

## 2️⃣ 배열 생성

```python
import numpy as np

# 리스트 → numpy 배열
arr = np.array([1, 2, 3, 4, 5])

# numpy 스타일 생성 (더 간결)
np.arange(1, 21)             # 1~20 배열 ✅
np.zeros(5)                  # [0. 0. 0. 0. 0.]
np.ones(5)                   # [1. 1. 1. 1. 1.]
np.arange(0, 10, 2)          # [0 2 4 6 8]
np.linspace(0, 1, 5)         # [0. 0.25 0.5 0.75 1.]
np.random.randint(0, 10, size=5)  # 랜덤 정수 5개
np.random.rand(3, 3)         # 0~1 랜덤 3x3 배열

# 2차원 배열
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])
```

---

## 3️⃣ 배열 속성

```python
arr2d.shape    # (2, 3)  ← 행, 열
arr2d.ndim     # 2       ← 차원 수
arr2d.size     # 6       ← 전체 원소 수
arr2d.dtype    # int64   ← 데이터 타입
```

---

## 4️⃣ 인덱싱 / 슬라이싱

```python
arr = np.array([1, 2, 3, 4, 5])

# 1차원
arr[0]      # 1
arr[-1]     # 5
arr[1:4]    # [2 3 4]
arr[::2]    # [1 3 5]

# 2차원
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

arr2d[0]        # [1 2 3] ← 첫 번째 행
arr2d[0, 1]     # 2 ← numpy 스타일
arr2d[:, 1]     # [2 5 8] ← 두 번째 열 전체
arr2d[0:2, 1:]  # [[2 3] [5 6]]
```

---

## 5️⃣ 연산

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 원소별 연산
a + b    # [5 7 9]
a * b    # [4 10 18]
a ** 2   # [1 4 9]

# 행렬 곱셈
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
np.dot(a, b)
# [1*5+2*7, 1*6+2*8]   [19, 22]
# [3*5+4*7, 3*6+4*8] = [43, 50]

# 파이썬 리스트와 차이
[1, 2, 3] + [4, 5, 6]   # [1, 2, 3, 4, 5, 6] ← 이어붙임
a + b                    # [5 7 9]             ← 원소별 덧셈
```

---

## 6️⃣ 브로드캐스팅

```python
arr = np.array([1, 2, 3, 4, 5])

arr + 10     # [11 12 13 14 15] ← 전체에 10 더함
arr * 2      # [2 4 6 8 10]
arr > 3      # [False False False True True]
```

---

## 7️⃣ 통계 함수

```python
arr = np.array([85, 92, 78, 95, 88, 73, 90, 82])

np.sum(arr)      # 합계
np.mean(arr)     # 평균
np.std(arr)      # 표준편차
np.min(arr)      # 최솟값
np.max(arr)      # 최댓값
np.median(arr)   # 중앙값

# 2차원 — 축 기준
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
np.sum(arr2d, axis=0)   # [5 7 9]  ← 열 기준
np.sum(arr2d, axis=1)   # [6 15]   ← 행 기준
```

---

## 8️⃣ 조건 필터링

```python
arr = np.array([1, 2, 3, 4, 5, 6])

# 단일 조건
arr[arr > 3]              # [4 5 6]

# 복합 조건 — & 로 한 번에
arr[(arr > 3) & (arr < 6)]   # [4 5] ✅

# where — 조건에 따라 값 선택
np.where(arr > 3, arr, 0)    # [0 0 0 4 5 6]
np.where(arr >= 90, "A", "B")  # 성적 변환에 활용
```

---

## 9️⃣ 배열 변환

```python
arr = np.array([1, 2, 3, 4, 5, 6])

arr.reshape(2, 3)    # 2행 3열
arr.reshape(3, -1)   # -1 은 자동 계산
arr2d.flatten()      # 1차원으로 펼치기
arr2d.T              # 전치 (행열 바꾸기)
```

---

# 2부 — pandas

## 1️⃣ pandas란?

```
데이터 분석에 특화된 파이썬 라이브러리
엑셀처럼 행/열로 이루어진 데이터를 다루는 도구

numpy  → 수치 계산 (배열)
pandas → 데이터 분석 (표)
```

---

## 2️⃣ 핵심 자료구조

```python
import pandas as pd

# Series — 1차원 (인덱스 + 값)
s = pd.Series([85, 92, 78], index=["Tom", "Jane", "Mike"])
print(s["Tom"])   # 85

# DataFrame — 2차원 (행 + 열)
df = pd.DataFrame({
    "name":  ["Tom", "Jane", "Mike"],
    "score": [85, 92, 78],
    "grade": ["B", "A", "C"]
})
```

---

## 3️⃣ DataFrame 기본 속성

```python
df.shape      # (3, 3)
df.columns    # 컬럼명 목록
df.dtypes     # 컬럼별 데이터 타입
df.info()     # 전체 정보 요약
df.describe() # 수치형 컬럼 통계 요약
df.head(3)    # 상위 3행
df.tail(3)    # 하위 3행
```

---

## 4️⃣ 데이터 조회

```python
# 컬럼 선택
df["name"]              # 단일 컬럼 (Series)
df[["name", "score"]]   # 여러 컬럼 (DataFrame)

# 행 선택
df.loc[0]               # 인덱스 라벨로 접근
df.iloc[0]              # 정수 위치로 접근

# 조건 필터링
df[df["score"] >= 85]
df[(df["score"] >= 85) & (df["grade"] == "B")]
```

---

## 5️⃣ 데이터 수정

```python
# 컬럼 추가
df["bonus"] = df["score"] + 5

# 조건으로 컬럼 추가
df["pass/fail"] = np.where(df["score"] >= 90, "pass", "fail")

# apply — 함수 적용
df["grade"] = df["score"].apply(lambda x: "A" if x >= 90 else "B")

# 컬럼 / 행 삭제
df.drop("bonus", axis=1, inplace=True)   # 열 삭제
df.drop(0, axis=0, inplace=True)         # 행 삭제

# 값 변경
df.loc[0, "score"] = 100
```

---

## 6️⃣ 결측치 처리

```python
df.isnull().sum()     # 컬럼별 결측치 개수
df.dropna()           # 결측치 있는 행 삭제
df.fillna(0)          # 결측치 0으로 채우기
df.fillna(df.mean())  # 결측치 평균으로 채우기
```

---

## 7️⃣ 정렬 / 집계

```python
# 정렬
df.sort_values("score", ascending=False)    # 내림차순
df.sort_values(["dept", "score"])           # 다중 정렬

# 집계
df["score"].mean()
df["score"].max()
df["score"].min()
df["score"].count()
df["grade"].value_counts()   # 빈도수

# groupby
df.groupby("dept")["score"].mean()    # dept 별 평균
df.groupby("dept")["name"].count()    # dept 별 학생 수
```

---

## 8️⃣ CSV 파일

```python
df = pd.read_csv("data.csv", encoding="utf-8")
df.to_csv("output.csv", index=False)   # index=False → 인덱스 제외
```

---

## ✅ 오늘 주의사항

```python
# numpy
# 1. 배열 생성은 np.arange() 활용
np.array([x+1 for x in range(20)])   # ❌ 불필요하게 김
np.arange(1, 21)                      # ✅ 간결

# 2. 복합 조건은 & / | 사용
arr[arr > 3][arr[arr > 3] < 10]      # ❌ 두 번에 나눠서
arr[(arr > 3) & (arr < 10)]          # ✅ 한 번에

# pandas
# 3. sort_values / 필터링 결과 저장 또는 출력 필수
df.sort_values("score")              # ❌ 출력 안 됨
print(df.sort_values("score"))       # ✅
sorted_df = df.sort_values("score")  # ✅ 변수에 저장

# 4. 상위 N명 이름만 출력
df.sort_values("score", ascending=False).head(3)["name"].values  # ✅

# 5. inplace=True — 원본 직접 수정
df.drop("col", axis=1)              # 원본 유지
df.drop("col", axis=1, inplace=True) # 원본 수정
```
