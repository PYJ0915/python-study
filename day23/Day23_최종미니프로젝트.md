# 📚 Day 23 파이썬 심화 — 최종 미니 프로젝트

---

## 프로젝트 개요

```
지금까지 배운 것들을 전부 연결해서
하나의 완성된 프로젝트 만들기

크롤링 → 데이터 분석 → 시각화 → API 서버
```

---

## 프로젝트 구조

```
mini_project/
├── 01_crawler.py    ← 크롤링 모듈
├── 02_analyzer.py   ← 데이터 분석 모듈
├── 03_app.py        ← Flask API 서버
├── 04_test.py       ← 전체 연결 테스트
├── books.csv        ← 수집한 데이터
└── chart.png        ← 시각화 결과
```

---

## 사용한 기술 스택

```
Selenium          → 동적 크롤링
BeautifulSoup     → HTML 파싱
pandas / numpy    → 데이터 분석
matplotlib        → 시각화
Flask             → REST API 서버
requests          → API 테스트
```

---

## 1단계 — crawler.py

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time

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
                "id":     i,
                "title":  item.select_one("h3 a").get("title"),
                "price":  item.select_one(".price_color").get_text().strip(),
                "rating": item.select_one("p")["class"][1]
            })
            i += 1   # i = i + 1 보다 파이써닉

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
df.to_csv("books.csv", index=False, encoding="utf-8-sig")
```

---

## 2단계 — analyzer.py

```python
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
books = pd.read_csv("books.csv", encoding="utf-8")

# 가격 — 문자열 → 숫자
books["price"] = books["price"].str.replace(r"[^0-9.]", "", regex=True).astype(float)

# 별점 — 영어 → 숫자
rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
books["rating"] = books["rating"].map(rating_map)

# 별점별 평균 가격
rating_avg_price = books.groupby("rating")["price"].mean()
print(rating_avg_price)

# 가격 분포 시각화
plt.hist(books["price"], bins=30, color="skyblue")
plt.title("책 가격 분포")
plt.savefig("chart.png")   # 파일로 저장
plt.show()

# 분석 결과
analyze = {
    "total_books":      len(books),
    "avg_price":        round(float(books["price"].mean()), 2),
    "max_price":        float(books["price"].max()),
    "min_price":        float(books["price"].min()),
    "rating_avg_price": rating_avg_price.to_dict()   # Series → dict 변환 필수
}

def get_books():
    return books.to_dict(orient="records")
```

---

## 3단계 — app.py

```python
from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# 서버 시작 시 데이터 로드
books = pd.read_csv("books.csv", encoding="utf-8")
books["price"] = books["price"].str.replace(r"[^0-9.]", "", regex=True).astype(float)
books["rating"] = books["rating"].map({"One":1,"Two":2,"Three":3,"Four":4,"Five":5})

# 에러 핸들러
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "책을 찾을 수 없어요"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "서버 에러"}), 500

# 전체 책 목록
@app.route("/books")
def get_books():
    return jsonify(books.to_dict(orient="records"))

# ⚠️ /books/top10 은 반드시 /books/<id> 보다 위에 선언
# Flask 는 위에서 아래로 라우트 매칭
# 순서 바뀌면 top10 이 id=top10 으로 인식될 수 있음
@app.route("/books/top10")
def get_top10():
    top10 = books.sort_values(
        by=["rating", "price"],
        ascending=[False, True]   # 별점 내림차순, 가격 오름차순
    ).head(10)
    return jsonify(top10.to_dict(orient="records"))

# 특정 책 조회
@app.route("/books/<int:id>")
def get_book(id):
    book = books[books["id"] == id]
    if book.empty:
        return jsonify({"error": "책을 찾을 수 없어요"}), 404
    return jsonify(book.to_dict(orient="records")[0])

# 분석 결과
@app.route("/analysis")
def analysis():
    analyze = {
        "total_books":      len(books),
        "avg_price":        round(float(books["price"].mean()), 2),
        "max_price":        float(books["price"].max()),
        "min_price":        float(books["price"].min()),
        "rating_avg_price": {
            str(k): round(float(v), 2)
            for k, v in books.groupby("rating")["price"].mean().items()
        }
    }
    return jsonify(analyze)

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 4단계 — test.py

```python
import requests

BASE = "http://127.0.0.1:5000"

# 전체 책 목록
print(requests.get(f"{BASE}/books").json())

# 특정 책 조회
print(requests.get(f"{BASE}/books/1").json())

# 없는 책 조회 — 에러 처리 확인
print(requests.get(f"{BASE}/books/9999").json())
# {"error": "책을 찾을 수 없어요"} 나오면 성공

# 별점 상위 10개
print(requests.get(f"{BASE}/books/top10").json())

# 분석 결과
print(requests.get(f"{BASE}/analysis").json())
```

---

## ✅ 오늘 주의사항

```python
# 1. i += 1 — 파이써닉한 카운터
i = i + 1   # ❌
i += 1       # ✅

# 2. Series → dict 변환 필수
rating_avg_price = books.groupby("rating")["price"].mean()
analyze = {"rating_avg_price": rating_avg_price}          # ❌ jsonify 에러
analyze = {"rating_avg_price": rating_avg_price.to_dict()} # ✅

# 3. 라우트 순서 — top10 을 <id> 보다 위에
@app.route("/books/top10")    # ✅ 먼저 선언
def get_top10(): ...

@app.route("/books/<int:id>") # ✅ 나중에 선언
def get_book(id): ...

# 4. numpy 타입 → float 변환
books["price"].mean()          # numpy.float64 → jsonify 에러 가능
float(books["price"].mean())   # ✅ float 로 변환

# 5. round() — 소수점 정리
round(float(books["price"].mean()), 2)   # ✅ 소수점 2자리

# 6. analysis 반환 문법
return jsonify(analyze={...})   # ❌ 문법 에러
return jsonify({...})           # ✅

# 7. driver.quit() 은 항상 finally 에서
try:
    driver.get(url)
finally:
    driver.quit()   # ✅ 에러나도 반드시 종료
```

---

## 전체 흐름 정리

```
01_crawler.py
    ↓ books.csv 저장
02_analyzer.py
    ↓ 데이터 정제 + 분석 + chart.png 저장
03_app.py
    ↓ Flask 서버 실행
04_test.py
    ↓ API 요청으로 전체 연결 확인
```
