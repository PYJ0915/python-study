# 📚 Day 21 파이썬 심화 — matplotlib / seaborn + 데이터 분석 프로젝트

---

# 1부 — matplotlib / seaborn 시각화

## 1️⃣ 기본 설정

```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# 한글 폰트 설정 (Windows)
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False   # 마이너스 기호 깨짐 방지
```

---

## 2️⃣ 자주 쓰는 그래프

```python
# 선 그래프 — 추세
plt.plot(x, y, color="blue", linewidth=2, linestyle="--", marker="o")

# 산점도 — 분포
plt.scatter(x, y, color="red", s=100)   # s = 점 크기

# 막대 그래프 — 비교
plt.bar(categories, values, color="skyblue")

# 수평 막대 그래프
plt.barh(categories, values)

# 히스토그램 — 분포
plt.hist(data, bins=30, color="green", edgecolor="black")
# bins 는 데이터 수에 맞게 조정 (너무 크면 의미없음)

# 파이 차트 — 비율
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
```

---

## 3️⃣ 그래프 꾸미기

```python
plt.figure(figsize=(10, 6))   # 그래프 크기

plt.plot(x, y1, label="데이터1")
plt.plot(x, y2, label="데이터2")

plt.title("제목", fontsize=16)
plt.xlabel("x축", fontsize=12)
plt.ylabel("y축", fontsize=12)
plt.legend()          # 범례
plt.grid(True)        # 격자
plt.tight_layout()    # 레이아웃 자동 조정
plt.show()
```

---

## 4️⃣ subplot — 여러 그래프 한 번에

```python
# 1행 2열
fig, axes = plt.subplots(1, 2, figsize=(10, 6))
# axes = [ax1, ax2] ← 1차원 배열
axes[0].plot(x, y)
axes[1].bar(x, y)

# 2행 2열
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
# axes = [[ax1, ax2], [ax3, ax4]] ← 2차원 배열
axes[0, 0].plot(x, y)
axes[0, 1].scatter(x, y)
axes[1, 0].bar(x, y)
axes[1, 1].hist(data)

plt.tight_layout()
plt.show()
```

---

## 5️⃣ seaborn

```python
# seaborn 은 matplotlib 위에서 동작
# 그래프 그리기 → seaborn
# 꾸미기 / 출력 → matplotlib

# 막대 그래프
sns.barplot(data=df, x="dept", y="score")
plt.title("부서별 점수")
plt.show()

# 박스 플롯 — 분포 확인
sns.boxplot(data=df, x="dept", y="score")
plt.show()

# 히트맵 — 상관관계 시각화
corr = df[["korean", "math", "english"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.show()

# subplot 과 같이 쓸 때
fig, axes = plt.subplots(1, 2)
sns.barplot(data=df, x="dept", y="score", ax=axes[0])
sns.boxplot(data=df, x="dept", y="score", ax=axes[1])
plt.show()
```

---

## 6️⃣ corr() — 상관관계

```python
# 두 컬럼 간의 상관관계를 -1 ~ 1 로 나타냄
# 1  → 양의 상관관계 (같이 증가)
# -1 → 음의 상관관계 (반대로 움직임)
# 0  → 상관관계 없음

corr = df[["korean", "math", "english"]].corr()
#          korean  math  english
# korean     1.00  0.23     0.15
# math       0.23  1.00     0.31
# english    0.15  0.31     1.00

# 컬럼 1개면 자기 자신과 1.0 만 나옴 (의미 없음)
# 컬럼 여러 개일 때 의미있음
```

---

## 7️⃣ pandas 에서 바로 시각화

```python
df["score"].plot(kind="bar")
df["score"].plot(kind="hist", bins=10)
df["score"].plot(kind="line")
plt.show()
```

---

# 2부 — 데이터 분석 프로젝트

## 프로젝트 구조

```
data_analysis/
├── data.csv       ← 데이터
└── analysis.py    ← 분석 코드
```

## 전체 분석 흐름

```
0단계 — 데이터 생성
1단계 — 데이터 불러오기 + 기본 확인
2단계 — 데이터 전처리
3단계 — 기초 통계 분석
4단계 — 시각화
5단계 — 상관관계 분석
```

---

## 0단계 — 데이터 생성

```python
np.random.seed(42)   # 재현 가능한 랜덤값
data = {
    "name":    [f"학생{i}" for i in range(1, 21)],
    "korean":  np.random.randint(60, 100, 20),
    "math":    np.random.randint(60, 100, 20),
    "english": np.random.randint(60, 100, 20),
    "dept":    np.random.choice(["A", "B", "C"], 20)
}
df = pd.DataFrame(data)
df.to_csv("data.csv", index=False, encoding="utf-8-sig")
```

---

## 1단계 — 데이터 불러오기 + 기본 확인

```python
df = pd.read_csv("data.csv", encoding="utf-8-sig")

df.shape           # 행, 열 수
df.head()          # 상위 5행
df.info()          # 데이터 타입
df.describe()      # 기초 통계
df.isnull().sum()  # 결측치 확인
```

---

## 2단계 — 데이터 전처리

```python
# 총점 / 평균 컬럼 추가
df["total"]   = df["korean"] + df["math"] + df["english"]
df["average"] = df["total"] / 3

# 등급 컬럼 추가
df["grade"] = df["average"].apply(lambda x:
    "A" if x >= 90 else
    "B" if x >= 80 else
    "C" if x >= 70 else
    "D"
)
```

---

## 3단계 — 기초 통계 분석

```python
# 과목별 통계
df[["korean", "math", "english"]].describe()

# 부서별 평균
df.groupby("dept")[["korean", "math", "english", "average"]].mean().round(1)

# 등급 분포
df["grade"].value_counts().sort_index()
```

---

## 4단계 — 시각화

```python
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# 과목별 평균 막대 그래프
subject_means = df[["korean", "math", "english"]].mean()
axes[0, 0].bar(subject_means.index, subject_means.values,
               color=["skyblue", "salmon", "lightgreen"])
axes[0, 0].set_title("과목별 평균")

# 평균 점수 분포 히스토그램
axes[0, 1].hist(df["average"], bins=10, color="purple", edgecolor="black")
axes[0, 1].set_title("평균 점수 분포")

# 부서별 평균 점수
sns.barplot(data=df, x="dept", y="average", ax=axes[0, 2])
axes[0, 2].set_title("부서별 평균 점수")

# 등급 분포 파이 차트
grade_counts = df["grade"].value_counts().sort_index()
axes[1, 0].pie(grade_counts, labels=grade_counts.index, autopct="%1.1f%%")
axes[1, 0].set_title("등급 분포")

# 국어 vs 수학 산점도
axes[1, 1].scatter(df["korean"], df["math"], alpha=0.6)
axes[1, 1].set_xlabel("국어")
axes[1, 1].set_ylabel("수학")
axes[1, 1].set_title("국어 vs 수학")

# 부서별 boxplot
sns.boxplot(data=df, x="dept", y="average", ax=axes[1, 2])
axes[1, 2].set_title("부서별 점수 분포")

plt.tight_layout()
plt.show()
```

---

## 5단계 — 상관관계 분석

```python
corr = df[["korean", "math", "english"]].corr()
plt.figure(figsize=(6, 4))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("과목 간 상관관계")
plt.show()
```

---

## 추가 분석 패턴

```python
# 수학 점수 상위 5명
df.sort_values("math", ascending=False)[["name", "math"]].head(5)

# 부서별 A등급 학생 수
df[df["grade"] == "A"]["dept"].value_counts()   # ✅ 간결
df[df["grade"] == "A"].groupby("dept").size()   # ✅ 동일

# 세 과목 모두 80점 이상인 학생 이름
df["name"][
    (df["korean"] >= 80) &
    (df["math"] >= 80) &
    (df["english"] >= 80)
].values   # .values → 인덱스 없이 이름만 출력
```

---

## ✅ 오늘 주의사항

```python
# 1. seaborn 출력은 plt.show()
sns.barplot(...)
plt.show()   # seaborn 도 plt.show() 로 출력

# 2. subplot 차원 주의
plt.subplots(1, 2) → axes[0], axes[1]          # 1차원
plt.subplots(2, 2) → axes[0, 0], axes[0, 1]    # 2차원

# 3. seaborn + subplot 같이 쓸 때 ax 지정
sns.barplot(data=df, x="dept", y="score", ax=axes[0, 2])

# 4. bins 는 데이터 수에 맞게
plt.hist(data, bins=5)    # 데이터 적을 때
plt.hist(data, bins=30)   # 데이터 많을 때

# 5. 이름만 출력할 때 .values 추가
df["name"][조건].values   # 인덱스 없이 깔끔하게

# 6. CSV 저장 시 한글 깨짐 방지
df.to_csv("data.csv", encoding="utf-8-sig")   # utf-8-sig ✅
```
