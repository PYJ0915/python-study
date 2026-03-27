# 실습 문제
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import pandas as pd
import requests
from flask import Flask, jsonify, request, abort

# 문제 1 - books.toscrape.com 에서 Selenium 으로
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 1. 첫 페이지 책 제목 전부 출력
try:
    print("=== 첫 페이지 책 제목 출력 시작! ===")
    driver.get("https://books.toscrape.com")
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    for element in soup.select("h3 a") :
        print(element.get("title"))

finally:
    driver.quit()
    print("=== 첫 페이지 책 제목 출력 완료! ===")

# 2. 다음 페이지 버튼 클릭 후 2페이지 책 제목 출력
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    print("=== 두 번째 페이지 책 제목 출력 ===")
    driver.get("https://books.toscrape.com")
    time.sleep(2)

    try:
        next_btn = driver.find_element(By.CSS_SELECTOR, ".next a")
        next_btn.click()
        time.sleep(2)
    except:
        print("마지막 페이지")

    soup = BeautifulSoup(driver.page_source, "html.parser")

    for element in soup.select("h3 a") :
        print(element.get("title"))

finally:
    driver.quit()  
    print("=== 두 번째 페이지 책 제목 출력 완료! ===")


# 3. 1~3페이지 제목 + 가격 DataFrame 저장
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
all_data = []

try:
    print("=== 1~3페이지 제목 + 가격 DataFrame 저장 시작! ===")
    driver.get("https://books.toscrape.com")
    time.sleep(2)

    for page in range(3):
        soup = BeautifulSoup(driver.page_source, "html.parser")

        for item in soup.select(".product_pod"):
            all_data.append({
                "title":  item.select_one("h3 a").get("title"),
                "price":  item.select_one(".price_color").text.strip()
            })

        print(f"{page+1}페이지 완료!")

        try:
            next_btn = driver.find_element(By.CSS_SELECTOR, ".next a")
            next_btn.click()
            time.sleep(2)
        except:
            print("마지막 페이지")
            break

finally:
    driver.quit()
    print("=== 1~3페이지 제목 + 가격 DataFrame 저장 완료! ===")

df = pd.DataFrame(all_data)
print(df.head())


# 문제 2 - jsonplaceholder.typicode.com 에서
BASE_URL = "https://jsonplaceholder.typicode.com"

# 1. 전체 사용자 이름 + 이메일 출력
response = requests.get(f"{BASE_URL}/users")
users = response.json()

df = pd.DataFrame(users)
print(df[["name", "email"]])

# 2. userId=1 의 게시글 제목 전부 출력
user_id = 1
response = requests.get(f"{BASE_URL}/posts", params={"userId":user_id})
posts = response.json()
df = pd.DataFrame(posts)
print(df)
print(df["title"].values)

# 3. 전체 게시글 중 userId 별 게시글 수 출력
response = requests.get(f"{BASE_URL}/posts")
posts = response.json()
df = pd.DataFrame(posts)
print(df.groupby("userId").count()["id"])

# 4. 새 게시글 POST 요청 후 응답 출력
data = {"title": "hello", "body": "world", "userId": 1}
response = requests.post(
    f"{BASE_URL}/posts",
    json=data
)

print(response.status_code)
print(response.json())


# 문제 3 - 아래 함수 구현
# 아래 함수를 구현해봐요
def get_user_info(user_id: int) -> dict:
    # user_id 로 사용자 정보 + 게시글 수 반환
    # {"name": "...", "email": "...", "post_count": 10}
    try:
      response = requests.get(f"{BASE_URL}/users")
      info = response.json()
      df = pd.DataFrame(info)
      user = df[df["id"] == user_id]
      resp = requests.get(f"{BASE_URL}/posts", params={"userId": user_id})
      posts = resp.json()
      return {"name" : user["name"].iloc[0], "email": user["email"].iloc[0], "post_count" : len(posts)}
    except Exception as e:
       print(f"에러: {e}")

print(get_user_info(1))

# 문제 4 - 아래 조건으로 API 서버 만들기
app = Flask(__name__)

books = [
    {"id": 1, "title": "파이썬 기초", "price": 25000},
    {"id": 2, "title": "파이썬 심화", "price": 30000},
    {"id": 3, "title": "데이터 분석", "price": 35000},
]

# GET    /books         → 전체 책 목록
# GET    /books/<id>    → 특정 책 조회
# POST   /books         → 책 추가
# DELETE /books/<id>    → 책 삭제
# GET /books?price_max=30000
# → 가격이 30000 이하인 책만 반환
# 없는 책 조회 시 → {"error": "책을 찾을 수 없어요"}, 404
# 서버 에러 시   → {"error": "서버 에러"}, 500

@app.errorhandler(500)
def server_error(error):
    return({
        "error": "서버 에러",
        "status": 500
    }), 500

@app.route("/books")
def get_books():
    return jsonify(books)

@app.route("/books/<int:id>")
def get_book(id):
    book = next((b for b in books if b["id"] == id), None)
    if not book:
        return jsonify({"error": "책을 찾을 수 없어요"}), 404
    return jsonify(book)

@app.route("/books", methods=["POST"])
def add_book():
    data = request.json
    new_book = {
        "id": len(books) + 1,
        "title": data["title"],
        "price": data["price"]
    }
    books.append(new_book)
    return jsonify(new_book), 201

@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    global books
    books = [b for b in books if b["id"] != id]
    return jsonify({"message": f"{id}번 사용자 삭제 완료"})
    

@app.route("/books")
def get_book_below_price():
    price = request.args.get("price_max")
    books = next((b for b in books if b["price"] <= price))
    if not books:
        return jsonify({"error": "3만원 이하의 책을 찾을 수 없어요"}), 404
    return jsonify(books)
    


# 풀이 개선점
#문제 2-3 — 더 간결하게
# 지금 코드
print(df.groupby("userId").count()["id"])

# 더 간결하게
print(df.groupby("userId").size())   # ✅ size() 가 더 자연스러움


# 문제 4 - 더 깔끔한 풀이
from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {"id": 1, "title": "파이썬 기초", "price": 25000},
    {"id": 2, "title": "파이썬 심화", "price": 30000},
    {"id": 3, "title": "데이터 분석", "price": 35000},
]

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "책을 찾을 수 없어요"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "서버 에러", "status": 500}), 500

@app.route("/books")
def get_books():
    price_max = request.args.get("price_max", type=int)
    if price_max:
        result = [b for b in books if b["price"] <= price_max]
        return jsonify(result)
    return jsonify(books)

@app.route("/books/<int:id>")
def get_book(id):
    book = next((b for b in books if b["id"] == id), None)
    if not book:
        return jsonify({"error": "책을 찾을 수 없어요"}), 404
    return jsonify(book)

@app.route("/books", methods=["POST"])
def add_book():
    data = request.json
    new_book = {
        "id":    len(books) + 1,
        "title": data["title"],
        "price": data["price"]
    }
    books.append(new_book)
    return jsonify(new_book), 201

@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    global books
    books = [b for b in books if b["id"] != id]
    return jsonify({"message": f"{id}번 책 삭제 완료"})

if __name__ == "__main__":
    app.run(debug=True)

