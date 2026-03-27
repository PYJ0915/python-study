# 📚 Day 22 파이썬 심화 — Selenium + HTTP/REST API + Flask

---

# 1부 — Selenium

## 1️⃣ Selenium이란?

```
브라우저를 직접 제어해서 동적 페이지를 크롤링하는 도구

requests + BeautifulSoup → 정적 페이지 (HTML 고정)
Selenium               → 동적 페이지 (JavaScript 로 렌더링)

활용
- 로그인 후 데이터 수집
- 버튼 클릭 / 스크롤 후 나타나는 데이터
- 검색어 입력 후 결과 수집
```

---

## 2️⃣ 기본 설정

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# 드라이버 설정
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://books.toscrape.com")
time.sleep(2)   # 페이지 로딩 대기

driver.quit()   # 항상 종료
```

---

## 3️⃣ 요소 찾기

```python
# CSS 선택자 — 가장 많이 씀
driver.find_element(By.CSS_SELECTOR, "h3 a")
driver.find_elements(By.CSS_SELECTOR, ".product_pod")

# ID / CLASS / TAG
driver.find_element(By.ID, "search")
driver.find_element(By.CLASS_NAME, "price_color")
driver.find_elements(By.TAG_NAME, "li")

# 텍스트 / 속성 추출
element.text
element.get_attribute("href")
element.get_attribute("title")
```

---

## 4️⃣ 클릭 / 입력

```python
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
```

---

## 5️⃣ 명시적 대기 — WebDriverWait

```python
# time.sleep() → 무조건 기다림 (비효율)
# WebDriverWait → 조건 충족 시 바로 진행 (효율적)

wait = WebDriverWait(driver, 10)   # 최대 10초 대기

element = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".product_pod"))
)
button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".next a"))
)
```

---

## 6️⃣ 스크롤

```python
# 맨 아래로
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# 특정 요소로
element = driver.find_element(By.CSS_SELECTOR, ".footer")
driver.execute_script("arguments[0].scrollIntoView()", element)
```

---

## 7️⃣ 실전 패턴 — 페이지네이션

```python
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
all_data = []

try:
    driver.get("https://books.toscrape.com")
    time.sleep(2)

    for page in range(3):
        soup = BeautifulSoup(driver.page_source, "html.parser")

        for item in soup.select(".product_pod"):
            all_data.append({
                "title":  item.select_one("h3 a").get("title"),
                "price":  item.select_one(".price_color").text.strip(),
                "rating": item.select_one("p")["class"][1]
            })

        print(f"{page+1}페이지 완료")

        try:
            next_btn = driver.find_element(By.CSS_SELECTOR, ".next a")
            next_btn.click()
            time.sleep(2)
        except:
            print("마지막 페이지")
            break

finally:
    driver.quit()   # 항상 finally 에서 종료

df = pd.DataFrame(all_data)
```

---

## 8️⃣ requests vs Selenium

```
requests + BS4    → 빠름, 가벼움, 정적 페이지
Selenium          → 느림, 무거움, 동적 페이지

선택 기준
HTML 소스에 데이터 있음 → requests + BS4 ✅
JavaScript 로 렌더링    → Selenium ✅
로그인 필요             → Selenium ✅
```

---

# 2부 — HTTP / REST API

## 1️⃣ HTTP란?

```
웹에서 데이터를 주고받는 규칙

클라이언트 → 요청(Request) → 서버
클라이언트 ← 응답(Response) ← 서버

HTTP 메서드
GET    → 데이터 조회
POST   → 데이터 생성
PUT    → 데이터 전체 수정
PATCH  → 데이터 일부 수정
DELETE → 데이터 삭제
```

---

## 2️⃣ REST API란?

```
HTTP 를 활용해서 데이터를 주고받는 규칙

GET    /users     → 전체 사용자 조회
GET    /users/1   → 1번 사용자 조회
POST   /users     → 사용자 생성
PUT    /users/1   → 1번 사용자 수정
DELETE /users/1   → 1번 사용자 삭제
```

---

## 3️⃣ requests 기본

```python
import requests

# GET
response = requests.get("https://jsonplaceholder.typicode.com/users")
print(response.status_code)   # 200
print(response.json())        # JSON → 파이썬 딕셔너리 자동 변환

# POST
response = requests.post(url, json={"title": "hello", "userId": 1})
print(response.status_code)   # 201 Created

# PUT / DELETE
requests.put(url, json={"title": "수정"})
requests.delete(url)

# 쿼리 파라미터
params = {"userId": 1, "_limit": 5}
response = requests.get(url, params=params)
# → URL: /posts?userId=1&_limit=5 자동 변환

# 헤더
headers = {"Authorization": "Bearer 토큰값"}
response = requests.get(url, headers=headers)
```

---

## 4️⃣ 응답 처리

```python
response.status_code    # 상태 코드
response.json()         # JSON → dict
response.text           # 문자열
response.headers        # 응답 헤더

# 에러 처리
try:
    response.raise_for_status()   # 에러면 예외 발생
    data = response.json()
except requests.exceptions.HTTPError as e:
    print(f"HTTP 에러: {e}")
except requests.exceptions.Timeout:
    print("타임아웃")
except requests.exceptions.ConnectionError:
    print("연결 에러")
```

---

## 5️⃣ 실전 예제

```python
BASE_URL = "https://jsonplaceholder.typicode.com"

# 전체 사용자 → DataFrame
response = requests.get(f"{BASE_URL}/users")
df = pd.DataFrame(response.json())
print(df[["name", "email"]])

# 특정 사용자 직접 조회
response = requests.get(f"{BASE_URL}/users/1")
user = response.json()

# userId 별 게시글 수
response = requests.get(f"{BASE_URL}/posts")
df = pd.DataFrame(response.json())
print(df.groupby("userId").size())

# 사용자 정보 + 게시글 수 함수
def get_user_info(user_id: int) -> dict:
    try:
        user = requests.get(f"{BASE_URL}/users/{user_id}").json()
        posts = requests.get(f"{BASE_URL}/posts", params={"userId": user_id}).json()
        return {
            "name":       user["name"],
            "email":      user["email"],
            "post_count": len(posts)
        }
    except Exception as e:
        print(f"에러: {e}")
```

---

## 6️⃣ Session

```python
# 일반 requests → 매 요청마다 독립적
# Session → 쿠키 / 헤더 유지 (로그인 상태 유지)

with requests.Session() as s:
    s.post(url, data={"username": "user", "password": "pass"})
    response = s.get(mypage_url)   # 로그인 상태 유지
```

---

# 3부 — Flask

## 1️⃣ Flask란?

```
파이썬으로 웹 서버를 만드는 경량 프레임워크
활용 — REST API 서버, 웹 애플리케이션, 크롤링 데이터 API 제공
```

---

## 2️⃣ 기본 서버

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Flask!"

if __name__ == "__main__":
    app.run(debug=True)   # debug=True → 코드 수정 시 자동 재시작

# http://127.0.0.1:5000 에서 확인
```

---

## 3️⃣ 라우팅

```python
@app.route("/about")
def about():
    return "소개 페이지"

# URL 파라미터
@app.route("/users/<int:user_id>")
def get_user(user_id):
    return f"사용자 {user_id}"

# 여러 메서드
@app.route("/login", methods=["GET", "POST"])
def login():
    return "로그인"
```

---

## 4️⃣ REST API 구현

```python
books = [
    {"id": 1, "title": "파이썬 기초", "price": 25000},
    {"id": 2, "title": "파이썬 심화", "price": 30000},
]

# GET 전체 + 쿼리 파라미터
@app.route("/books")
def get_books():
    price_max = request.args.get("price_max", type=int)
    if price_max:
        result = [b for b in books if b["price"] <= price_max]
        return jsonify(result)
    return jsonify(books)

# GET 단일
@app.route("/books/<int:id>")
def get_book(id):
    book = next((b for b in books if b["id"] == id), None)
    if not book:
        return jsonify({"error": "책을 찾을 수 없어요"}), 404
    return jsonify(book)

# POST 생성
@app.route("/books", methods=["POST"])
def add_book():
    data = request.json
    new_book = {"id": len(books)+1, "title": data["title"], "price": data["price"]}
    books.append(new_book)
    return jsonify(new_book), 201

# DELETE 삭제
@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    global books
    books = [b for b in books if b["id"] != id]
    return jsonify({"message": f"{id}번 책 삭제 완료"})
```

---

## 5️⃣ 에러 핸들러

```python
# API 서버에서 에러를 JSON 으로 통일된 형식으로 반환

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "요청한 리소스를 찾을 수 없어요", "status": 404}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "서버 에러", "status": 500}), 500

# 직접 에러 발생
from flask import abort
abort(404)   # → errorhandler(404) 실행

# 커스텀 에러
class BookNotFound(Exception):
    pass

@app.errorhandler(BookNotFound)
def handle_book_not_found(error):
    return jsonify({"error": "책을 찾을 수 없어요"}), 404
```

---

## 6️⃣ 미들웨어 — before / after request

```python
import time
from flask import g

# 모든 요청 전에 실행
@app.before_request
def before():
    g.start_time = time.time()
    print(f"[요청] {request.method} {request.path}")

# 모든 요청 후에 실행 — response 반드시 반환!
@app.after_request
def after(response):
    elapsed = time.time() - g.start_time
    print(f"[응답] {response.status_code} | {elapsed:.4f}초")
    response.headers["X-Response-Time"] = f"{elapsed:.4f}s"
    return response   # ← 필수!

# 실행 흐름
# 클라이언트 요청
#   → before_request (로그, 인증 체크)
#   → 라우트 함수 (비즈니스 로직)
#   → after_request (로그, 헤더 추가)
# 클라이언트 응답
```

---

## 7️⃣ 블루프린트 — 라우트 분리

```python
# routes/book_routes.py
from flask import Blueprint, jsonify

book_bp = Blueprint("books", __name__, url_prefix="/books")

@book_bp.route("/")          # 실제 URL: /books/
def get_books():
    return jsonify([])

@book_bp.route("/<int:id>")  # 실제 URL: /books/1
def get_book(id):
    return jsonify({})

# app.py
from flask import Flask
from routes.book_routes import book_bp

app = Flask(__name__)
app.register_blueprint(book_bp)   # 블루프린트 등록

# 블루프린트 없이 → 모든 라우트가 app.py 에 몰림
# 블루프린트 있으면 → 기능별 파일 분리 → 유지보수 쉬움

# 자바로 비유하면
# @RestController BookController → book_routes.py
# SpringApplication (메인)       → app.py
```

---

## 8️⃣ Flask + 크롤링 연결

```python
from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def crawl_books():
    response = requests.get("https://books.toscrape.com")
    soup = BeautifulSoup(response.text, "html.parser")
    return [{
        "title": item.select_one("h3 a").get("title"),
        "price": item.select_one(".price_color").text.strip()
    } for item in soup.select(".product_pod")]

@app.route("/books")
def get_books():
    return jsonify(crawl_books())
```

---

## 9️⃣ API 테스트

```python
import requests

BASE = "http://127.0.0.1:5000"

requests.get(f"{BASE}/books").json()
requests.post(f"{BASE}/books", json={"title": "새 책", "price": 20000}).json()
requests.put(f"{BASE}/books/1", json={"title": "수정된 제목"}).json()
requests.delete(f"{BASE}/books/1").json()
```

---

## ✅ 오늘 주의사항

```python
# Selenium
# 1. driver.quit() 은 항상 finally 에서
try:
    driver.get(url)
finally:
    driver.quit()   # ✅ 에러나도 반드시 종료

# 2. WebDriverWait 이 time.sleep() 보다 효율적
wait.until(EC.presence_of_element_located(...))   # ✅

# REST API
# 3. 특정 리소스는 직접 조회
requests.get(f"{BASE_URL}/users/{user_id}")       # ✅
requests.get(f"{BASE_URL}/users")                 # ❌ 전체 불러와서 필터링

# Flask
# 4. 같은 URL 라우트 중복 금지 → 쿼리 파라미터는 같은 함수 안에서 처리
@app.route("/books")
def get_books():
    price_max = request.args.get("price_max", type=int)   # ✅
    if price_max:
        return jsonify([b for b in books if b["price"] <= price_max])
    return jsonify(books)

# 5. after_request 는 response 반드시 반환
@app.after_request
def after(response):
    return response   # ✅ 없으면 에러

# 6. errorhandler 에 jsonify 필수
@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "서버 에러"}), 500   # ✅
    return ({"error": "서버 에러"}), 500           # ❌ jsonify 없으면 에러

# 7. 전역 변수 수정 시 global 선언
@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    global books   # ✅ 필수
    books = [b for b in books if b["id"] != id]
```
