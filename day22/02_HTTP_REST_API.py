# 1. 배경 지식
# HTTP - 웹에서 데이터를 주고받는 규칙
# 클라이언트 → 요청(Request) → 서버
# 클라이언트 ← 응답(Response) ← 서버

# HTTP 메서드
# GET    → 데이터 조회
# POST   → 데이터 생성
# PUT    → 데이터 전체 수정
# PATCH  → 데이터 일부 수정
# DELETE → 데이터 삭제

# REST API - HTTP 를 활용해서 데이터를 주고받는 규칙

# 예시
# GET    /users        → 전체 사용자 조회
# GET    /users/1      → 1번 사용자 조회
# POST   /users        → 사용자 생성
# PUT    /users/1      → 1번 사용자 수정
# DELETE /users/1      → 1번 사용자 삭제

# 2. requests 기본
import requests

# GET 요청
response = requests.get("https://jsonplaceholder.typicode.com/users")

print(response.status_code)    # 200
print(response.json())         # JSON → 파이썬 딕셔너리 자동 변환

# POST 요청
data = {"title": "hello", "body": "world", "userId": 1}
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data   # json= 으로 전달
)
print(response.status_code)   # 201 Created
print(response.json())

# PUT 요청
response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json={"title": "수정된 제목"}
)

# DELETE 요청
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)   # 200


# 3. 헤더 / 파라미터
# 헤더 설정
url = "https://jsonplaceholder.typicode.com/users"
headers = {
    "Authorization": "Bearer 토큰값",
    "Content-Type": "application/json"
}
response = requests.get(url, headers=headers)

# 쿼리 파라미터
# URL: /posts?userId=1&_limit=5
params = {"userId": 1, "_limit": 5}
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
)
# requests 가 자동으로 URL 에 붙여줌


# 4. 응답 처리
response = requests.get(url)

response.status_code    # 상태 코드
response.json()         # JSON → dict 변환
response.text           # 문자열
response.headers        # 응답 헤더
response.url            # 최종 URL

# 상태 코드 확인
if response.status_code == 200:
    data = response.json()
else:
    print(f"에러: {response.status_code}")

# raise_for_status() — 에러면 예외 발생
try:
    response.raise_for_status()
    data = response.json()
except requests.exceptions.HTTPError as e:
    print(f"HTTP 에러: {e}")


# 5. 실전 예제 - 공공 API
import pandas as pd

# JSONPlaceholder — 테스트용 무료 API
BASE_URL = "https://jsonplaceholder.typicode.com"

# 전체 사용자 조회
response = requests.get(f"{BASE_URL}/users")
users = response.json()

# DataFrame 으로 변환
df = pd.DataFrame(users)
print(df[["id", "name", "email", "phone"]])

# 특정 사용자의 게시글 조회
user_id = 1
response = requests.get(f"{BASE_URL}/posts", params={"userId": user_id})
posts = response.json()
print(f"사용자 {user_id}의 게시글 수: {len(posts)}")


# 6. Session - 로그인 유지
# 일반 requests — 매 요청마다 독립적
# Session — 쿠키 / 헤더 유지

session = requests.Session()

# 로그인
session.post("https://example.com/login", data={
    "username": "user",
    "password": "pass"
})

# 로그인 상태로 요청
response = session.get("https://example.com/mypage")
session.close()

# with 문으로 자동 종료
# with requests.Session() as s:
#     s.post(url, data=login_data)
#     response = s.get(mypage_url)


# 7. 예외 처리
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()

except requests.exceptions.Timeout:
    print("타임아웃")
except requests.exceptions.ConnectionError:
    print("연결 에러")
except requests.exceptions.HTTPError as e:
    print(f"HTTP 에러: {e}")
except Exception as e:
    print(f"기타 에러: {e}")