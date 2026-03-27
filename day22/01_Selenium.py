# Selenium - 브라우저를 직접 제어해서 동적 페이지를 크롤링하는 도구
# requests + BeautifulSoup → 정적 페이지 (HTML 고정)
# Selenium               → 동적 페이지 (JavaScript 로 렌더링)

# 예시
# - 로그인 후 데이터 수집
# - 버튼 클릭 / 스크롤 후 나타나는 데이터
# - 검색어 입력 후 결과 수집

# 1. 기본 설정
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import pandas as pd

# 드라이버 설정
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 페이지 열기
driver.get("https://books.toscrape.com")
time.sleep(2)   # 페이지 로딩 대기

# 종료
driver.quit()


# 2. 요소 찾기
# By.CSS_SELECTOR - 가장 많이 씀
driver.find_element(By.CSS_SELECTOR, "h3 a")
driver.find_elements(By.CSS_SELECTOR, ".product_pod")

# By.ID
driver.find_element(By.ID, "search")

# By.CLASS_NAME
driver.find_element(By.CLASS_NAME, "price_color")

# By.TAG_NAME
driver.find_elements(By.TAG_NAME, "li")

# By.XPATH
driver.find_element(By.XPATH, "//h1[@class='title']")


# 3. 텍스트 / 속성 추출
# 텍스트
element = driver.find_element(By.CSS_SELECTOR, "h1")
print(element.text)

# 속성
link = driver.find_element(By.CSS_SELECTOR, "h3 a")
print(link.get_attribute("href"))
print(link.get_attribute("title"))


# 4. 클릭 / 입력
# 클릭
button = driver.find_element(By.CSS_SELECTOR, ".next a")
button.click()
time.sleep(2)

# 텍스트 입력
search_box = driver.find_element(By.CSS_SELECTOR, "input[name='q']")
search_box.clear()
search_box.send_keys("파이썬")

from selenium.webdriver.common.keys import Keys
search_box.send_keys(Keys.RETURN)   # 엔터키
time.sleep(2)


# 5. 명시적 대기 - WebDriverWait
# time.sleep() 은 무조건 기다림 → 비효율
# WebDriverWait 은 조건 충족 시 바로 진행 → 효율적

wait = WebDriverWait(driver, 10)   # 최대 10초 대기

# 요소가 나타날 때까지 대기
element = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".product_pod"))
)

# 클릭 가능할 때까지 대기
button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".next a"))
)
button.click()


# 6. 스크롤
# 맨 아래로 스크롤
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(2)

# 특정 요소로 스크롤
element = driver.find_element(By.CSS_SELECTOR, ".footer")
driver.execute_script("arguments[0].scrollIntoView()", element)


# 7. 실전 패턴 - 페이지네이션
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
all_data = []

try:
    driver.get("https://books.toscrape.com")
    time.sleep(2)

    for page in range(3):   # 3페이지
        # BeautifulSoup 으로 파싱
        soup = BeautifulSoup(driver.page_source, "html.parser")

        for item in soup.select(".product_pod"):
            all_data.append({
                "title":  item.select_one("h3 a").get("title"),
                "price":  item.select_one(".price_color").text.strip(),
                "rating": item.select_one("p")["class"][1]
            })

        print(f"{page+1}페이지 완료")

        # 다음 페이지 버튼 클릭
        try:
            next_btn = driver.find_element(By.CSS_SELECTOR, ".next a")
            next_btn.click()
            time.sleep(2)
        except:
            print("마지막 페이지")
            break

finally:
    driver.quit()   # 항상 종료

df = pd.DataFrame(all_data)
print(df)


# 8. requests vs Selenium 비교
# requests + BS4    → 빠름, 가벼움, 정적 페이지
# Selenium          → 느림, 무거움, 동적 페이지

# 선택 기준
# HTML 소스에 데이터 있음 → requests + BS4 ✅
# JavaScript 로 렌더링    → Selenium ✅
# 로그인 필요             → Selenium ✅
