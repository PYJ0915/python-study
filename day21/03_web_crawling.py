# 웹 크롤링 - 웹 페이지에서 데이터를 자동으로 수집하는 것

# 활용 예시
# - 뉴스 기사 수집
# - 쇼핑몰 가격 비교
# - 부동산 정보 수집
# - 주식 데이터 수집

# 1. requests - 웹페이지 가져오기
import requests

response = requests.get("https://www.naver.com")

print(response.status_code)   # 200 → 성공
print(response.text)          # HTML 전체 내용
print(response.encoding)      # 인코딩 방식

# 상태 코드
# 200 → 성공
# 404 → 페이지 없음
# 403 → 접근 거부
# 500 → 서버 에러


# 2. BeautifulSoup - HTML 파싱

# 예시 HTML 구조
# <html>
#   <body>
#     <h1 class="title">안녕하세요</h1>
#     <ul id="list">
#       <li class="item">사과</li>
#       <li class="item">바나나</li>
#       <li class="item">딸기</li>
#     </ul>
#     <a href="https://naver.com">네이버</a>
#   </body>
# </html>

from bs4 import BeautifulSoup

soup = BeautifulSoup("예시 HTML 구조", "html.parser")

# 태그 찾기 — find() 첫 번째만
soup.find("h1")                   # <h1 class="title">안녕하세요</h1>
soup.find("li", class_="item")    # 첫 번째 li
soup.find("ul", id="list")        # id 로 찾기

# 태그 찾기 — find_all() 전부
soup.find_all("li")                # 모든 li 리스트
soup.find_all("li", class_="item")

# 텍스트 추출
soup.find("h1").text               # "안녕하세요"
soup.find("h1").get_text()         # "안녕하세요"

# 속성 추출
soup.find("a")["href"]             # "https://naver.com"
soup.find("a").get("href")         # "https://naver.com" (더 안전)


# 3. CSS 선택자 - select()
# find() 보다 더 강력한 선택자
soup.select("li")          # 모든 li
soup.select(".item")       # class="item"
soup.select("#list")       # id="list"
soup.select("ul li")       # ul 안의 li
soup.select("ul > li")     # ul 직속 자식 li

# 첫 번째만
soup.select_one(".item")   # find() 와 동일

# find() vs select() 차이
# find() — 태그 / class / id 로 찾기
soup.find("li", class_="item")

# select() — CSS 선택자로 찾기
soup.select(".item")        # class
soup.select("#list li")     # 중첩 선택자 가능 ← find() 로는 복잡함

# 보통 단순한 건 find()
# 복잡한 구조는 select()


# 4. 실전 크롤링 패턴
def crawl(url):
    # 1) 헤더 설정 — 봇 차단 우회
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    # 2) 요청
    response = requests.get(url, headers=headers)

    # 3) 상태 코드 확인
    if response.status_code != 200:
        print(f"에러: {response.status_code}")
        return None

    # 4) 파싱
    soup = BeautifulSoup(response.text, "html.parser")

    # 5) 데이터 추출
    items = soup.find_all("li", class_="item")
    result = []
    for item in items:
        result.append(item.text.strip())

    return result


# 5. 예외처리 + 딜레이
import time

urls = ["url1", "url2", "url3"]

for url in urls:
    try:
        response = requests.get(url, timeout=5)   # 5초 타임아웃
        soup = BeautifulSoup(response.text, "html.parser")
        print(soup.find("h1").text)

    except requests.exceptions.Timeout:
        print("타임아웃 발생")
    except requests.exceptions.ConnectionError:
        print("연결 에러")
    except Exception as e:
        print(f"에러: {e}")

    time.sleep(1)   # 1초 딜레이 ← 서버 부하 방지


# 6. 크롤링 데이터 → CSV 저장
import pandas as pd

data = []

items = []

for item in items:
    data.append({
        "title": item.find("h2").text.strip(),
        "price": item.find(".price").text.strip(),
        "link":  item.find("a").get("href")
    })

df = pd.DataFrame(data)
df.to_csv("result.csv", index=False, encoding="utf-8-sig")
# utf-8-sig → 한글 깨짐 방지


# 7. 실전 예제 - 날씨 크롤링
def get_weather():
    url = "https://wttr.in/Seoul?format=3"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            print(response.text)
    except Exception as e:
        print(f"에러: {e}")

get_weather()

# ⚠️ 크롤링 주의사항
# 1) robots.txt 확인
#    https://사이트주소/robots.txt
#    → Disallow 된 경로는 크롤링 금지

# 2) 서버 부하 방지
#    → time.sleep() 으로 딜레이

# 3) 개인정보 수집 금지

# 4) 상업적 이용 시 저작권 확인