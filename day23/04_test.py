import requests

BASE = "http://127.0.0.1:5000"

# 전체 책 목록 조회
print(requests.get(f"{BASE}/books").json())

# 특정 책 조회
print(requests.get(f"{BASE}/books/1").json())

# 없는 책 조회 — 에러 처리 확인
print(requests.get(f"{BASE}/books/9999").json())

# 별점 상위 10개
print(requests.get(f"{BASE}/books/top10").json())

# 분석 결과
print(requests.get(f"{BASE}/analysis").json())
