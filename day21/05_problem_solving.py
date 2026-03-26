# 실습 문제
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time

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


# 문제 3 - HTML 파싱 연습

html = """
<html>
  <body>
    <div class="news">
      <h2 class="title">파이썬 인기 급상승</h2>
      <p class="content">파이썬이 전 세계적으로...</p>
      <a href="https://news.com/1">자세히 보기</a>
    </div>
    <div class="news">
      <h2 class="title">AI 시대의 데이터 분석</h2>
      <p class="content">데이터 분석 수요가...</p>
      <a href="https://news.com/2">자세히 보기</a>
    </div>
    <div class="news">
      <h2 class="title">웹 크롤링 기초</h2>
      <p class="content">웹 크롤링을 배우면...</p>
      <a href="https://news.com/3">자세히 보기</a>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# 1. 모든 뉴스 제목 출력
for element in soup.select(".title"):
  print(element.get_text().strip())

# 2. 모든 링크(href) 출력
for element in soup.find_all("a"):
  print(element.get("href"))

# 3. 제목 + 링크를 딕셔너리 리스트로 만들기
result = []
for element in soup.select("div"):
  result.append({
    element.find("h2").get_text().strip() : element.find("a").get("href")
  })

print(result)

# 4. DataFrame 으로 변환 후 출력
items = soup.select("div")
data = []

for item in items:
  data.append({
    "title" : item.find("h2").get_text().strip(),
    "content" : item.find("p").get_text().strip(),
    "link": item.find("a").get("href")
  })

df = pd.DataFrame(data)
df.to_csv("result.csv", index=False, encoding="utf-8-sig")


# 문제 4 - 실전 크롤링
# 아래 URL 에서 크롤링해봐요
url = "https://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 1. 책 제목 전부 출력
for element in soup.find_all("a"):
  if(element.has_attr("title")):
    print(element.get("title"))

# 2. 책 가격 전부 출력
for element in soup.select(".price_color"):
  print(element.get_text())

# 3. 제목 + 가격 DataFrame 으로 저장
items = soup.select(".product_pod")
data = []

for item in items:
  title = None
  for element in item.find_all("a"):
     if(element.has_attr("title")):
       title = element.get("title")
  data.append({
    "title" : title,
    "price" : item.select_one(".price_color").get_text()
  })

df = pd.DataFrame(data)
print(df)


# 문제 5 — 페이지네이션
# books.toscrape.com 에서
# 1~3 페이지 책 전부 크롤링
# 제목 + 가격 + 별점 DataFrame 저장
def crawl_all_pages(max_page=5):
    all_data = []

    for page in range(1, max_page + 1):
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
        headers = {"User-Agent": "Mozilla/5.0"}

        try:
            response = requests.get(url, headers=headers, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")

            items = soup.select(".product_pod")
            for item in items:
                all_data.append({
                    "title": item.select_one("h3 a").get("title"),
                    "price": item.select_one(".price_color").get_text().strip(),
                    "rating": item.select_one("p")["class"][1]  
                })

            print(f"{page}페이지 완료 ({len(items)}개)")
            time.sleep(1) 

        except Exception as e:
            print(f"{page}페이지 에러: {e}")

    return pd.DataFrame(all_data)

df = crawl_all_pages(max_page=3)
print(df.head())
print(f"\n총 {len(df)}개 수집")


# 문제 6 — 데이터 정제 + 분석
# 크롤링한 데이터에서
# 1. 가격을 숫자로 변환
df["price"] = df["price"].str.replace(r"[^0-9.]", "", regex=True).astype(float)

# 2. 별점을 숫자로 변환
rating_map = {
   "One" : 1, "Two" : 2, "Three" : 3, "Four" : 4, "Five" : 5
}
df["rating"] = df["rating"].map(rating_map)

print(df.head(5))

# 3. 별점 4 이상인 책만 추출
print(df[df["rating"] >= 4])

# 4. 가격 기준 내림차순 정렬 후 상위 5개 출력
print(df.sort_values("price", ascending=False).head(5))



# 실습 문제 풀이 개선
# 문제 3-3 — 딕셔너리 구조 개선
# 지금 코드 — 키가 제목, 값이 링크
result.append({
    element.find("h2").get_text().strip() : element.find("a").get("href")
})
# [{'파이썬 인기 급상승': 'https://news.com/1'}, ...]

# 더 일반적인 방식
result.append({
    "title": element.find("h2").get_text().strip(),
    "link":  element.find("a").get("href")
})
# [{'title': '파이썬 인기 급상승', 'link': 'https://news.com/1'}, ...]


# 문제 4-1 - 더 간결하게
# 지금 코드
for element in soup.find_all("a"):
    if element.has_attr("title"):
        print(element.get("title"))

# 더 간결하게
for element in soup.select("article h3 a"):
    print(element.get("title"))   # ✅ CSS 선택자로 바로 접근


# 문제 4-3 - 깔끔하게
# 지금 코드 — for 루프 안에 for 루프
for item in items:
    title = None
    for element in item.find_all("a"):
        if element.has_attr("title"):
            title = element.get("title")

# 더 간결하게
for item in items:
    title = item.select_one("h3 a").get("title")   # ✅ 바로 접근
    price = item.select_one(".price_color").get_text()