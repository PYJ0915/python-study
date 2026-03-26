# 데이터 분석 프로젝트
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# 0단계 - 샘플 데이터 생성
np.random.seed(42)
data = {
  "name": [f"학생{i}" for i in range(1, 21)],
  "korean": np.random.randint(60, 100, 20),
  "math":   np.random.randint(60, 100, 20),
  "english":np.random.randint(60, 100, 20),
  "dept":   np.random.choice(["A", "B", "C"], 20)
}

df = pd.DataFrame(data)
df.to_csv("data.csv", index=False, encoding="utf-8-sig")


# 1단계 - 데이터 불러오기 + 기본 확인
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

df = pd.read_csv("data.csv", encoding="utf-8-sig")

# 기본 확인
print(df.shape)       # 행, 열 수
print(df.head())      # 상위 5행
print(df.info())      # 데이터 타입
print(df.describe())  # 기초 통계
print(df.isnull().sum())  # 결측치 확인


# 2단계 - 데이터 전처리
# 총점 / 평균 컬럼 추가
df["total"] = df["korean"] + df["math"] + df["english"]
df["average"] = df["total"] / 3

# 등급 컬럼 추가
df["grade"] = df["average"].apply(lambda x:
  "A" if x >= 90 else
  "B" if x >= 80 else
  "C" if x >= 70 else
  "D"                               
)

print(df.head())

# 3단계 - 기초 통계 분석
# 과목별 통계
print("=== 과목별 통계 ===")
print(df[["korean", "math", "english"]].describe())

# 부서별 평균
print("\n=== 부서별 평균 ===")
print(df.groupby("dept")[["korean", "math", "english", "average"]].mean().round(1))

# 등급 분포
print("\n=== 등급 분포 ===")
print(df["grade"].value_counts().sort_index())


# 4단계 - 시각화
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# 1. 과목별 평균 막대 그래프
subject_means = df[["korean", "math", "english"]].mean()
axes[0, 0].bar(subject_means.index, subject_means.values, color=["skyblue", "salmon", "lightgreen"])
axes[0, 0].set_title("과목별 평균")

# 2. 점수 분포 히스토그램
axes[0, 1].hist(df["average"], bins=10, color="purple", edgecolor="black")
axes[0, 1].set_title("평균 점수 분포")

# 3. 부서별 평균 점수 barplot
sns.barplot(data=df, x="dept", y="average", ax=axes[0, 2])
axes[0, 2].set_title("부서별 평균 점수")

# 4. 등급 분포 파이 차트
grade_counts = df["grade"].value_counts().sort_index()
axes[1, 0].pie(grade_counts, labels=grade_counts.index, autopct="%1.1f%%")
axes[1, 0].set_title("등급 분포")

# 5. 국어 vs 수학 산점도
axes[1, 1].scatter(df["korean"], df["math"], alpha=0.6)
axes[1, 1].set_xlabel("국어")
axes[1, 1].set_ylabel("수학")
axes[1, 1].set_title("국어 vs 수학")

# 6. 부서별 boxplot
sns.boxplot(data=df, x="dept", y="average", ax=axes[1, 2])
axes[1, 2].set_title("부서별 점수 분포")

plt.tight_layout()
plt.show()


# 5단계 - 상관관계 분석
# 과목 간 상관관계
corr = df[["korean", "math", "english"]].corr()

plt.figure(figsize=(6, 4))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("과목 간 상관관계")
plt.show()


# 실습
# 추가 분석 문제
# 1. 수학 점수 상위 5명 출력
print(df.sort_values("math", ascending=False)[["name", "math"]].head(5))

# 2. 부서별 A등급 학생 수
print(df[df["grade"] == "A"].groupby("dept")["dept"].count())

# 3. 세 과목 모두 80점 이상인 학생 이름
print(df["name"][(df["korean"] >= 80) & (df["math"] >= 80) & (df["english"] >= 80)])


# 추가 분색 개선
# 추가 분석 2번 — 더 깔끔하게
# 지금 코드
print(df[df["grade"] == "A"].groupby("dept")["dept"].count())

# 더 깔끔하게
print(df[df["grade"] == "A"].groupby("dept").size())   # ✅ size() 가 더 자연스러움

# 또는
print(df[df["grade"] == "A"]["dept"].value_counts())   # ✅ 한 줄로

# 추가 분석 3번 — values 추가하면 더 깔끔해요
# 지금 코드
print(df["name"][(df["korean"] >= 80) & (df["math"] >= 80) & (df["english"] >= 80)])
# 0    학생1
# 3    학생4
# Name: name, dtype: object  ← 인덱스랑 같이 출력

# 이름만 출력
print(df["name"][(df["korean"] >= 80) & (df["math"] >= 80) & (df["english"] >= 80)].values)
# ['학생1' '학생4']  ← 깔끔하게 ✅

