# 실습 문제
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# 문제 1 - 아래 데이터로 그래프를 그리기
months = ["1월", "2월", "3월", "4월", "5월", "6월"]
sales  = [120, 135, 110, 150, 160, 145]

# 1. 선 그래프 — 월별 매출 추이
plt.rcParams["font.family"] = "Malgun Gothic"   # Windows
plt.plot(months, sales)
plt.show()

# 2. 막대 그래프 — 월별 매출 비교
plt.bar(months, sales, color="purple")
plt.show()

# 3. 두 그래프를 subplot 으로 나란히 출력
fig, axes = plt.subplots(1, 2, figsize=(10, 6)) # [<Axes: > <Axes: >] => 1차원 배열

axes[0].plot(months, sales)
axes[0].set_title("선 그래프")

axes[1].bar(months, sales)
axes[1].set_title("막대 그래프")

plt.tight_layout()
plt.show()

# 문제 2 - 아래 성적 데이터를 시각화
df = pd.DataFrame({
    "name":  ["Tom", "Jane", "Mike", "Anna", "John", "Lisa"],
    "score": [85, 92, 78, 95, 88, 73],
    "dept":  ["A", "B", "A", "B", "A", "B"]
})

# 1. dept 별 평균 score 막대 그래프
sns.barplot(data=df, x="dept", y="score")
plt.show()

# 2. score 분포 히스토그램
plt.hist(df["score"], bins=5)
plt.show()

# 3. seaborn 으로 dept 별 boxplot
sns.boxplot(data=df, x="dept", y="score")
plt.show()