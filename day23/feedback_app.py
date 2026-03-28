from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

books = pd.read_csv("books.csv", encoding="utf-8")
books["price"] = books["price"].str.replace(r"[^0-9.]", "", regex=True).astype(float)
books["rating"] = books["rating"].map({"One":1,"Two":2,"Three":3,"Four":4,"Five":5})

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "책을 찾을 수 없어요"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "서버 에러"}), 500

@app.route("/books")
def get_books():
    return jsonify(books.to_dict(orient="records"))

@app.route("/books/top10")        # ← 반드시 위에
def get_top10():
    top10 = books.sort_values(
        by=["rating", "price"],
        ascending=[False, True]   # 별점 내림차순, 가격 오름차순
    ).head(10)
    return jsonify(top10.to_dict(orient="records"))

@app.route("/books/<int:id>")     # ← 반드시 아래
def get_book(id):
    book = books[books["id"] == id]
    if book.empty:
        return jsonify({"error": "책을 찾을 수 없어요"}), 404
    return jsonify(book.to_dict(orient="records")[0])

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