# Flask - 파이썬으로 웹 서버를 만드는 경량 프레임워크

# 활용
# - REST API 서버 만들기
# - 웹 애플리케이션 만들기
# - 크롤링 데이터를 API 로 제공

# 1. 가장 간단한 Flask 서버
from flask import Flask

app = Flask(__name__)

@app.route("/")          # URL 경로 지정
def index():
    return "Hello Flask!"

if __name__ == "__main__":
    app.run(debug=True)   # debug=True → 코드 수정 시 자동 재시작


# 2. 라우팅 - Flask, FastAPI 등 웹 프레임워크에서 사용자가 요청한 URL(예: /about)을 매핑된 특정 파이썬 함수와 연결해주는 기술
app = Flask(__name__)

@app.route("/")
def index():
    return "홈페이지"

@app.route("/about")
def about():
    return "소개 페이지"

# URL 파라미터
@app.route("/users/<int:user_id>")
def get_user(user_id):
    return f"사용자 {user_id}"

# /users/1 → "사용자 1"
# /users/2 → "사용자 2"

# 여러 메서드
@app.route("/login", methods=["GET", "POST"])
def login():
    return "로그인"


# 3. JSON 응답 - REST API
from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Tom",  "email": "tom@gmail.com"},
    {"id": 2, "name": "Jane", "email": "jane@gmail.com"},
    {"id": 3, "name": "Mike", "email": "mike@gmail.com"},
]

# 전체 조회
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# 단일 조회
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "사용자 없음"}), 404
    return jsonify(user)


# 4. POST/PUT/DELETE
# POST — 생성
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json   # 요청 body 에서 JSON 받기
    new_user = {
        "id":    len(users) + 1,
        "name":  data["name"],
        "email": data["email"]
    }
    users.append(new_user)
    return jsonify(new_user), 201   # 201 Created

# PUT — 수정
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    for user in users:
        if user["id"] == user_id:
            user.update(data)
            return jsonify(user)
    return jsonify({"error": "사용자 없음"}), 404

# DELETE — 삭제
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": f"{user_id}번 사용자 삭제 완료"})


# 5. 쿼리 파라미터
# /users?name=Tom&limit=5
@app.route("/users", methods=["GET"])
def get_users():
    name  = request.args.get("name")   # 쿼리 파라미터
    limit = request.args.get("limit", type=int, default=10)

    result = users
    if name:
        result = [u for u in users if name.lower() in u["name"].lower()]

    return jsonify(result[:limit])


# 6. 블루프린트 - 라우트를 파일별로 분리하는 것

# user_routes.py (라우트 파일)
# routes/user_routes.py
from flask import Blueprint, jsonify, request

# 블루프린트 생성
# "users" → 블루프린트 이름
# url_prefix → 모든 라우트 앞에 /users 자동으로 붙음
user_bp = Blueprint("users", __name__, url_prefix="/users")

@user_bp.route("/")          # 실제 URL: /users/
def get_users():
    return jsonify([{"id": 1, "name": "Tom"}])

@user_bp.route("/<int:id>")  # 실제 URL: /users/1
def get_user(id):
    return jsonify({"id": id, "name": "Tom"})

@user_bp.route("/", methods=["POST"])  # 실제 URL: /users/
def create_user():
    data = request.json
    return jsonify(data), 201


# routes/book_routes.py (라우트 파일)
from flask import Blueprint, jsonify

book_bp = Blueprint("books", __name__, url_prefix="/books")

@book_bp.route("/")          # 실제 URL: /books/
def get_books():
    return jsonify([{"id": 1, "title": "파이썬"}])


# app.py (메인 파일에서 라우트 파일 임포트)
from flask import Flask
# from routes.user_routes import user_bp
# from routes.book_routes import book_bp

app = Flask(__name__)

# 블루프린트 등록
app.register_blueprint(user_bp)
app.register_blueprint(book_bp)

if __name__ == "__main__":
    app.run(debug=True)

# 결과
# /users/    → get_users()
# /users/1   → get_user(1)
# /books/    → get_books()

# 블루프린트 없이 → 모든 라우트가 app.py 에 몰림
# 블루프린트 있으면 → 기능별로 파일 분리 → 유지보수 쉬움


# 7. 에러 핸들러
# 에러 핸들러 없으면
# 404 에러 시 → HTML 에러 페이지 반환 (API 에는 안 어울림)

# 에러 핸들러 있으면
# 404 에러 시 → JSON 형식으로 통일된 에러 반환

# 기본 에러 핸들러
from flask import Flask, jsonify

app = Flask(__name__)

# 404 — 페이지 없음
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "요청한 리소스를 찾을 수 없어요",
        "status": 404
    }), 404

# 400 — 잘못된 요청
@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "error": "잘못된 요청이에요",
        "status": 400
    }), 400

# 500 — 서버 에러
@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "error": "서버 에러가 발생했어요",
        "status": 500
    }), 500

# 커스텀 에러 만들기
# 직접 에러 발생시키기
from flask import abort

# @app.route("/users/<int:id>")
# def get_user(id):
#     user = find_user(id)
#     if user is None:
#         abort(404)   # → @app.errorhandler(404) 실행
#     return jsonify(user)

# 커스텀 에러 클래스
class BookNotFound(Exception):
    pass

@app.errorhandler(BookNotFound)
def handle_book_not_found(error):
    return jsonify({"error": "책을 찾을 수 없어요"}), 404

# @app.route("/books/<int:id>")
# def get_book(id):
#     book = find_book(id)
#     if book is None:
#         raise BookNotFound()   # → @app.errorhandler(BookNotFound) 실행
#     return jsonify(book)

# 에러 핸들러 정리
# 에러 핸들러 = 에러 발생 시 실행되는 함수
#             일관된 JSON 형식으로 에러 반환 가능
#             API 서버에서 필수!


# 8. 미들웨어 (before / after request)
# 왜 필요한가?

# 모든 요청에 공통으로 처리해야 하는 것들

# 예시
# - 로그 남기기          → 모든 요청/응답 기록
# - 인증 체크            → 토큰이 있는지 확인
# - 응답 헤더 추가       → CORS 설정
# - 실행 시간 측정       → 성능 모니터링

# before_request / after_request
import time
from flask import Flask, request, jsonify, g

app = Flask(__name__)

# 모든 요청 전에 실행
@app.before_request
def before():
    g.start_time = time.time()   # g → 요청 내에서 공유하는 전역 객체
    print(f"[요청] {request.method} {request.path}")

    # 인증 체크 예시
    # token = request.headers.get("Authorization")
    # if not token:
    #     return jsonify({"error": "인증 필요"}), 401

# 모든 요청 후에 실행
@app.after_request
def after(response):
    elapsed = time.time() - g.start_time
    print(f"[응답] {response.status_code} | {elapsed:.4f}초")

    # 응답 헤더 추가
    response.headers["X-Response-Time"] = f"{elapsed:.4f}s"
    return response   # ← after_request 는 response 반드시 반환!

# 실행 흐름
# 클라이언트 요청
#     ↓
# @before_request 실행   ← 시간 기록, 인증 체크
#     ↓
# 라우트 함수 실행       ← 실제 비즈니스 로직
#     ↓
# @after_request 실행   ← 로그 출력, 헤더 추가
#     ↓
# 클라이언트 응답

# 전체 흐름 예시 
from flask import Flask, jsonify, request, g
import time

app = Flask(__name__)

books = [
    {"id": 1, "title": "파이썬 기초", "price": 25000},
    {"id": 2, "title": "파이썬 심화", "price": 30000},
]

@app.before_request
def before():
    g.start = time.time()
    print(f"→ {request.method} {request.path} 요청")

@app.after_request
def after(response):
    elapsed = time.time() - g.start
    print(f"← {response.status_code} ({elapsed:.4f}초)")
    return response

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "없는 페이지"}), 404

@app.route("/books")
def get_books():
    return jsonify(books)

@app.route("/books/<int:id>")
def get_book(id):
    book = next((b for b in books if b["id"] == id), None)
    if not book:
        return jsonify({"error": "책 없음"}), 404
    return jsonify(book)

if __name__ == "__main__":
    app.run(debug=True)

# GET /books 요청 시 출력
# → GET /books 요청
# ← 200 (0.0012초)

# GET /books/99 요청 시 출력
# → GET /books/99 요청
# ← 404 (0.0008초)

# Flask 심화 최종 정리 
# 블루프린트   → 라우트를 파일로 분리
#              기능별로 코드 정리 → 유지보수 쉬움

# 에러 핸들러 → 에러 발생 시 JSON 으로 통일된 응답
#              abort() 또는 raise 로 에러 발생

# 미들웨어    → 모든 요청 전/후에 공통 처리
#              로그, 인증, 성능 측정 등
#              after_request 는 response 반드시 반환!


# 9. Flask + 크롤링 연결
# 크롤링 데이터를 API 로 제공
from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def crawl_books():
    response = requests.get("https://books.toscrape.com")
    soup = BeautifulSoup(response.text, "html.parser")
    books = []
    for item in soup.select(".product_pod"):
        books.append({
            "title": item.select_one("h3 a").get("title"),
            "price": item.select_one(".price_color").text.strip()
        })
    return books

@app.route("/books")
def get_books():
    books = crawl_books()
    return jsonify(books)

@app.route("/books/<int:n>")
def get_book(n):
    books = crawl_books()
    if n > len(books):
        return jsonify({"error": "없는 책"}), 404
    return jsonify(books[n-1])

if __name__ == "__main__":
    app.run(debug=True)


# 10. API 테스트 - reuests로 확인
import requests

BASE = "http://127.0.0.1:5000"

# GET
print(requests.get(f"{BASE}/users").json())

# POST
print(requests.post(f"{BASE}/users",
    json={"name": "Anna", "email": "anna@gmail.com"}).json())

# PUT
print(requests.put(f"{BASE}/users/1",
    json={"name": "Tom Updated"}).json())

# DELETE
print(requests.delete(f"{BASE}/users/1").json())