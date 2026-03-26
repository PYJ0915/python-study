# 📚 Day 21 파이썬 심화 — matplotlib/seaborn + 데이터 분석 + 웹 크롤링

---

# 1부 — matplotlib / seaborn 시각화

## 1️⃣ 기본 설정

```python
import matplotlib.pyplot as plt
import seaborn as sns

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
plt.scatter(x, y, color="red", s=100)

# 막대 그래프 — 비교
plt.bar(categories, values, color="skyblue")
plt.barh(categories, values)   # 수평

# 히스토그램 — 분포 (bins 는 데이터 수에 맞게)
plt.hist(data, bins=10, color="green", edgecolor="black")

# 파이 차트 — 비율
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
```

---

## 3️⃣ 그래프 꾸미기

```python
plt.figure(figsize=(10, 6))
plt.title("제목", fontsize=16)
plt.xlabel("x축")
plt.ylabel("y축")
plt.legend()        # 범례
plt.grid(True)      # 격자
plt.tight_layout()  # 레이아웃 자동 조정
plt.show()
```

---

## 4️⃣ subplot — 여러 그래프 한 번에

```python
# 1행 2열 → 1차원 배열
fig, axes = plt.subplots(1, 2, figsize=(10, 6))
axes[0].plot(x, y)
axes[1].bar(x, y)

# 2행 3열 → 2차원 배열
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes[0, 0].plot(x, y)
axes[0, 1].scatter(x, y)
axes[1, 0].bar(x, y)

plt.tight_layout()
plt.show()
```

---

## 5️⃣ seaborn

```python
# seaborn 은 matplotlib 위에서 동작
# 그리기 → seaborn / 꾸미기·출력 → matplotlib

sns.barplot(data=df, x="dept", y="score")        # 막대
sns.boxplot(data=df, x="dept", y="score")         # 박스플롯
sns.heatmap(corr, annot=True, cmap="coolwarm")    # 히트맵

# subplot 과 같이 쓸 때 ax 지정
fig, axes = plt.subplots(1, 2)
sns.barplot(data=df, x="dept", y="score", ax=axes[0])
sns.boxplot(data=df, x="dept", y="score", ax=axes[1])
plt.show()
```

---

## 6️⃣ corr() — 상관관계

```python
# -1 ~ 1 사이 값
# 1  → 양의 상관관계 / -1 → 음의 상관관계 / 0 → 없음

corr = df[["korean", "math", "english"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.show()

# 컬럼 1개 → 자기 자신과 1.0 만 나옴 (의미 없음)
# 컬럼 여러 개일 때 의미있음
```

---

# 2부 — 데이터 분석 프로젝트

## 전체 분석 흐름

```
0단계 — 데이터 생성
1단계 — 불러오기 + 기본 확인
2단계 — 전처리
3단계 — 기초 통계 분석
4단계 — 시각화
5단계 — 상관관계 분석
```

## 0단계 — 데이터 생성

```python
np.random.seed(42)
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

## 1단계 — 불러오기 + 기본 확인

```python
df = pd.read_csv("data.csv", encoding="utf-8-sig")
df.shape / df.head() / df.info() / df.describe() / df.isnull().sum()
```

## 2단계 — 전처리

```python
df["total"]   = df["korean"] + df["math"] + df["english"]
df["average"] = df["total"] / 3
df["grade"]   = df["average"].apply(lambda x:
    "A" if x >= 90 else "B" if x >= 80 else "C" if x >= 70 else "D")
```

## 3단계 — 기초 통계

```python
df[["korean", "math", "english"]].describe()
df.groupby("dept")[["korean", "math", "english", "average"]].mean().round(1)
df["grade"].value_counts().sort_index()
```

## 4단계 — 시각화

```python
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# 과목별 평균
subject_means = df[["korean", "math", "english"]].mean()
axes[0, 0].bar(subject_means.index, subject_means.values,
               color=["skyblue", "salmon", "lightgreen"])

# 평균 점수 분포
axes[0, 1].hist(df["average"], bins=10, color="purple", edgecolor="black")

# 부서별 평균
sns.barplot(data=df, x="dept", y="average", ax=axes[0, 2])

# 등급 분포 파이 차트
grade_counts = df["grade"].value_counts().sort_index()
axes[1, 0].pie(grade_counts, labels=grade_counts.index, autopct="%1.1f%%")

# 산점도
axes[1, 1].scatter(df["korean"], df["math"], alpha=0.6)

# 부서별 boxplot
sns.boxplot(data=df, x="dept", y="average", ax=axes[1, 2])

plt.tight_layout()
plt.show()
```

## 추가 분석 패턴

```python
# 상위 5명
df.sort_values("math", ascending=False)[["name", "math"]].head(5)

# 부서별 A등급 수
df[df["grade"] == "A"]["dept"].value_counts()

# 세 과목 모두 80점 이상
df["name"][
    (df["korean"] >= 80) &
    (df["math"] >= 80) &
    (df["english"] >= 80)
].values   # .values → 인덱스 없이 이름만 출력
```

---

# 3부 — 웹 크롤링

## 1️⃣ 웹 크롤링이란?

```
웹 페이지에서 데이터를 자동으로 수집하는 것
활용 — 뉴스 수집, 가격 비교, 주식 데이터 등
```

## 2️⃣ requests — 웹 페이지 가져오기

```python
import requests

response = requests.get("https://books.toscrape.com")
print(response.status_code)   # 200 → 성공
print(response.text)          # HTML 전체

# 상태 코드
# 200 → 성공 / 404 → 없음 / 403 → 접근 거부 / 500 → 서버 에러
```

## 3️⃣ BeautifulSoup — HTML 파싱

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, "html.parser")

# find() — 첫 번째만
soup.find("h2")
soup.find("li", class_="item")
soup.find("ul", id="list")

# find_all() — 전부
soup.find_all("li")

# 텍스트 / 속성 추출
soup.find("h2").text
soup.find("a").get("href")   # get() 이 더 안전

# select() — CSS 선택자
soup.select(".item")          # class
soup.select("#list li")       # 중첩
soup.select_one(".item")      # 첫 번째만
```

## 4️⃣ find() vs select()

```python
# 단순한 구조 → find()
soup.find("li", class_="item")

# 복잡한 구조 → select()
soup.select("article h3 a")   # 중첩 선택자 가능
```

## 5️⃣ 실전 크롤링 패턴

```python
import time

def crawl(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code != 200:
            return None
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    except requests.exceptions.Timeout:
        print("타임아웃 발생")
    except Exception as e:
        print(f"에러: {e}")
```

## 6️⃣ 페이지네이션

```python
def crawl_all_pages(max_page=3):
    all_data = []
    headers = {"User-Agent": "Mozilla/5.0"}

    for page in range(1, max_page + 1):
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
        try:
            response = requests.get(url, headers=headers, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")

            for item in soup.select(".product_pod"):
                all_data.append({
                    "title":  item.select_one("h3 a").get("title"),
                    "price":  item.select_one(".price_color").get_text().strip(),
                    "rating": item.select_one("p")["class"][1]
                })

            print(f"{page}페이지 완료")
            time.sleep(1)   # 딜레이 필수

        except Exception as e:
            print(f"에러: {e}")

    return pd.DataFrame(all_data)
```

## 7️⃣ 데이터 정제

```python
# 가격 — 문자열 → 숫자
df["price"] = df["price"].str.replace(r"[^0-9.]", "", regex=True).astype(float)
# 또는
df["price"] = df["price"].str.replace("£", "").astype(float)

# 별점 — 영어 → 숫자
rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
df["rating"] = df["rating"].map(rating_map)
```

## 8️⃣ 크롤링 → 분석 → 시각화 연결

```python
# 별점별 평균 가격
rating_price = df.groupby("rating")["price"].mean()
plt.bar(rating_price.index, rating_price.values)
plt.title("별점별 평균 가격")
plt.show()
```

## 9️⃣ CSV 저장

```python
df.to_csv("result.csv", index=False, encoding="utf-8-sig")
# utf-8-sig → 한글 깨짐 방지
```

---

## ✅ 오늘 주의사항

```python
# 1. seaborn 출력은 plt.show()
sns.barplot(...)
plt.show()   # ✅

# 2. subplot 차원 주의
plt.subplots(1, 2) → axes[0]        # 1차원
plt.subplots(2, 2) → axes[0, 0]     # 2차원

# 3. 딕셔너리 키는 고정값으로
{"title": ..., "link": ...}          # ✅ 나중에 DataFrame 변환 편함
{element.text: element.get("href")}  # ❌ 키가 동적 → 접근 불편

# 4. CSS 선택자로 간결하게
for a in soup.find_all("a"):
    if a.has_attr("title"):          # ❌ 조건문 필요
item.select_one("h3 a").get("title") # ✅ 바로 접근

# 5. 가격 변환 — 정규표현식이 더 범용적
df["price"].str.replace("£", "")              # £ 만 처리
df["price"].str.replace(r"[^0-9.]", "", regex=True)  # 모든 기호 처리 ✅

# 6. 크롤링 주의사항
# robots.txt 확인 → Disallow 경로 크롤링 금지
# time.sleep() → 서버 부하 방지 필수
# 개인정보 수집 금지
```
