from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import pandas as pd

# books.toscrape.com 1~5페이지 크롤링
# 제목 / 가격 / 별점 수집
# books.csv 로 저장
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
all_data = []
i = 1

try:
    driver.get("https://books.toscrape.com")
    time.sleep(2)

    for page in range(5):
       soup = BeautifulSoup(driver.page_source, "html.parser")

       for item in soup.select(".product_pod"):
          all_data.append({
             "id": i,
             "title": item.select_one("h3 a").get("title"),
             "price": item.select_one(".price_color").get_text().strip(),
             "rating": item.select_one("p")["class"][1]
          })
          i = i + 1

       print(f"{page+1}페이지 완료")

        # 다음 페이지 버튼 클릭
       try:
          next_btn = driver.find_element(By.CSS_SELECTOR, ".next a")
          next_btn.click()
          time.sleep(2)
       except:
          print("마지막 페이지입니다.")
          break

finally:
  driver.quit()

df = pd.DataFrame(all_data)
df.to_csv("books.csv", index=False, encoding="utf-8-sig")