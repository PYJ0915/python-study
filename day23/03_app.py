# Flask API 서버 
# GET /books — 전체 책 목록
# GET /books/<id>  — 특정 책 조회
# GET /books/top10 — 별점 상위 10개
# GET /analysis — 분석 결과

from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

books = pd.read_csv("books.csv", encoding="utf-8")

books["price"] = books["price"].str.replace(r"[^0-9.]", "", regex=True).astype(float)

rating_map = {
  "One" : 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5
}

books["rating"] = books["rating"].map(rating_map)

@app.errorhandler(404)
def not_fount(error):
  return jsonify({"error": "책을 찾을 수 없어요"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "서버 에러", "status": 500}), 500

@app.route("/books")
def get_books():
   return jsonify(books.to_dict(orient="records"))

@app.route("/books/<int:id>")
def get_book(id):
    book = books[books["id"] == id]

    if book.empty:
        return jsonify({"error": "책을 찾을 수 없어요"}), 404

    return jsonify(book.to_dict(orient="records")[0])

@app.route("/books/top10")
def get_top10():
   top10 = books.sort_values(by="rating", ascending=False).head(10)
   return jsonify(top10.to_dict(orient="records"))

@app.route("/analysis")
def analysis():
   return jsonify(
      analyze = {
  "total_books" : len(books),
  "avg_price": books["price"].mean(),
  "max_price": books["price"].max(),
  "min_price": books["price"].min(),
  "rating_avg_price": books.groupby("rating")["price"].mean().to_dict()
}
   )

if __name__ == "__main__":
    app.run(debug=True)