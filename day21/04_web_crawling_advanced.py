# 웹 크롤링 심화
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# 1. 여러 페이지 크롤링 (페이지네이션)

# books.toscrape.com 은 총 50페이지
# URL 패턴: https://books.toscrape.com/catalogue/page-{n}.html

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
                    "rating": item.select_one("p")["class"][1]  # 별점
                })

            print(f"{page}페이지 완료 ({len(items)}개)")
            time.sleep(1)   # 딜레이

        except Exception as e:
            print(f"{page}페이지 에러: {e}")

    return pd.DataFrame(all_data)

df = crawl_all_pages(max_page=3)
print(df.head())
print(f"\n총 {len(df)}개 수집")


# 2. 상세 페이지 크롤링
# 목록 페이지 → 상세 페이지 링크 추출 → 상세 페이지 크롤링

def crawl_detail(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    return {
        "title":       soup.find("h1").text,
        "price":       soup.select_one(".price_color").text,
        "stock":       soup.select_one(".availability").text.strip(),
        "description": soup.select_one("#product_description + p").text
                       if soup.select_one("#product_description + p") else "없음"
    }

# 목록에서 링크 추출 후 상세 크롤링
base_url = "https://books.toscrape.com/catalogue/"
response = requests.get("https://books.toscrape.com")
soup = BeautifulSoup(response.text, "html.parser")

links = [base_url + item.select_one("h3 a")["href"]
         for item in soup.select(".product_pod")[:3]]  # 3개만

for link in links:
    detail = crawl_detail(link)
    print(detail)
    time.sleep(1)


# 3. 데이터 정제
df = crawl_all_pages(max_page=3)

# 가격 — 문자열 → 숫자
df["price"] = df["price"].str.replace(r"[^0-9.]", "", regex=True).astype(float)

# 별점 — 영어 → 숫자
rating_map = {
    "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5
}
df["rating"] = df["rating"].map(rating_map)

print(df.head(5))
print(df.dtypes)
print(df.describe())


# 4. 크롤링 + 분석 + 시각화 연결
import matplotlib.pyplot as plt

# 별점별 평균 가격
rating_price = df.groupby("rating")["price"].mean()

plt.rcParams["font.family"] = "Malgun Gothic" 
plt.figure(figsize=(8, 5))
plt.bar(rating_price.index, rating_price.values, color="skyblue")
plt.title("별점별 평균 가격")
plt.xlabel("별점")
plt.ylabel("가격 (£)")
plt.show()

# 가격 분포
plt.hist(df["price"], bins=20, color="salmon", edgecolor="black")
plt.title("책 가격 분포")
plt.show()


# 5. Selenium — 동적 페이지 크롤링
# requests + BeautifulSoup → 정적 페이지 (HTML 고정)
# Selenium → 동적 페이지 (JavaScript 로 렌더링)

# 설치
# pip install selenium
# ChromeDriver 설치 필요

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com")

# 요소 찾기
titles = driver.find_elements(By.CSS_SELECTOR, "h3 a")
for title in titles:
    print(title.get_attribute("title"))

# 클릭
button = driver.find_element(By.CSS_SELECTOR, ".next a")
button.click()
time.sleep(2)

driver.quit()   # 브라우저 종료