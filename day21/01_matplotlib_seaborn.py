# matplotlib - 파이썬의 대표적인 2D 그래프 시각화 표준 라이브러리
# seaborn - Matplotlib을 기반으로 구축된 통계 중심의 시각화 라이브러리

# 1. matplotlib 기본
import matplotlib.pyplot as plt
import numpy as np

# 기본 선 그래프
x  = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title("기본 선 그래프")
plt.xlabel("x축")
plt.ylabel("y축")
plt.show()

# 2. 자주 쓰는 그래프
# 선그래프 - 추세
plt.plot(x, y, color="blue", linewidth=2, linestyle="--", marker="o")
plt.show()

# 산점도 - 분포
plt.scatter(x, y, color="red", s=100)   # s = 점 크기
plt.show()

# 막대 그래프 - 비교
categories = ["A", "B", "C", "D"]
values = [10, 20, 15, 30]
plt.bar(categories, values, color="skyblue")
plt.show()

# 수평 막대 그래프
plt.barh(categories, values)
plt.show()

# 히스토그램 - 분포
data = np.random.randn(1000)
plt.hist(data, bins=30, color="green", edgecolor="black")
plt.show()

# 파이 차트 - 비율
sizes = [30, 25, 20, 15, 10]
labels = ["A", "B", "C", "D", "E"]
plt.pie(sizes, labels=labels, autopct="%1.1f")
plt.show()


# 3. 그래프 꾸미기
plt.figure(figsize=(10, 6))   # 그래프 크기, figsize(w, h) -> 인치 단위 크기

plt.plot(x, y, label="data1", color="blue") # 색상

plt.title("title", fontsize=16) # 제목 및 글씨 크기
plt.xlabel("x", fontsize=12)    # x축 이름 및 글씨 크기
plt.ylabel("y", fontsize=12)    # y축 이름 및 글씨 크기
plt.legend()                    # 범례
plt.grid(True)                  # 격자
plt.tight_layout()              # 레이아웃 자동 조정
plt.show()


# 4. 여러 그래프 한 번에 - subplot
# plt.subplots(행 개수, 열 개수, ...)
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
# fig - 전체 캔버스(도화지)
# axes = 각 subplot들을 담고 있는 배열(2차원 배열)
# axes = [
#   [axes[0,0], axes[0,1]],
#   [axes[1,0], axes[1,1]]
# ]

# 각 subplot에 그래프 그리기
axes[0, 0].plot(x, y)
axes[0, 0].set_title("선 그래프")

axes[0, 1].scatter(x, y)
axes[0, 1].set_title("산점도")

axes[1, 0].bar(categories, values)
axes[1, 0].set_title("막대 그래프")

axes[1, 1].hist(data, bins=20)
axes[1, 1].set_title("히스토그램")

plt.tight_layout()
plt.show()


# 5. seaborn - 더 예쁜 그래프
import seaborn as sns
import pandas as pd

df = pd.DataFrame({
    "name":  ["Tom", "Jane", "Mike", "Anna", "John"],
    "score": [85, 92, 78, 95, 88],
    "dept":  ["A", "B", "A", "B", "A"]
})

# 1) 막대 그래프
sns.barplot(data=df, x="dept", y="score")
plt.show()

# 2) 박스 플롯 — 분포 확인
sns.boxplot(data=df, x="dept", y="score")
plt.show()

# 3) 히트맵 — 상관관계
corr = df[["score"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()

# 4) 산점도 + 회귀선
sns.regplot(data=df, x="score", y="score")
plt.show()

# 5) pairplot — 전체 컬럼 간 관계
sns.pairplot(df)
plt.show()


# cf) corr() - 두 컬럼 간의 상관관계를 -1 ~ 1 사이 값으로 나타내는 것
# 1  에 가까울수록 → 양의 상관관계 (같이 증가)
# -1 에 가까울수록 → 음의 상관관계 (반대로 움직임)
# 0  에 가까울수록 → 상관관계 없음

# 키 vs 몸무게      → 0.8  (양의 상관관계)
# 공부시간 vs 성적  → 0.9  (양의 상관관계)
# 운동량 vs 체지방  → -0.7 (음의 상관관계)
# 신발 크기 vs 성적 → 0.0  (상관관계 없음)

# 컬럼이 한 개
df = pd.DataFrame({
    "name":  ["Tom", "Jane", "Mike", "Anna", "John"],
    "score": [85, 92, 78, 95, 88],
    "dept":  ["A", "B", "A", "B", "A"]
})

# df[["score"]] → 컬럼 1개짜리 DataFrame
# df["score"]  → Series (1차원)
# df[["score"]] → DataFrame (2차원) ← 대괄호 2개!

corr = df[["score"]].corr()
print(corr)
#        score
# score    1.0   ← 자기 자신과의 상관관계는 항상 1


# 컬럼이 여러개
df = pd.DataFrame({
    "score":   [85, 92, 78, 95, 88],
    "study_h": [5, 8, 3, 9, 6],    # 공부 시간
    "sleep_h": [7, 6, 8, 5, 7]     # 수면 시간
})

corr = df.corr()
print(corr)
#          score  study_h  sleep_h
# score     1.00     0.98    -0.95
# study_h   0.98     1.00    -0.97
# sleep_h  -0.95    -0.97     1.00

# score vs study_h = 0.98 → 공부 많이 할수록 성적 높음
# score vs sleep_h = -0.95 → 잠 많이 잘수록 성적 낮음

sns.heatmap(corr, annot=True, cmap="coolwarm")
# annot=True  → 숫자 표시
# cmap="coolwarm" → 양수는 빨강, 음수는 파랑으로 색상 표현
# → 숫자보다 색으로 보면 한눈에 파악 가능
plt.show()

# 정리
# corr()   → 컬럼 간 상관관계 계산 (-1 ~ 1)
# heatmap  → 상관관계를 색으로 시각화
# 컬럼 1개 → 자기 자신과 1.0 만 나옴 (의미 없음)
# 컬럼 여러개 → 각 컬럼 간 관계 파악 가능


# 6. pandas에서 바로 시각화
# pandas 자체 plot 기능
df["score"].plot(kind="bar")
plt.show()

df["score"].plot(kind="hist", bins=10)
plt.show()

df["score"].plot(kind="line")
plt.show()

df.plot(kind="scatter", x="score", y="score")
plt.show()

# 7. 한글 폰트 설정
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

plt.rcParams["font.family"] = "Malgun Gothic"   # Windows
plt.rcParams["axes.unicode_minus"] = False       # 마이너스 기호 깨짐 방지

x  = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title("기본 선 그래프")
plt.xlabel("x축")
plt.ylabel("y축")
plt.show()
