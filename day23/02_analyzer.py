import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# books.csv 불러오기
# 가격 / 별점 숫자로 변환
# 별점별 평균 가격
# 가격 분포 시각화
# 분석 결과 반환
books = pd.read_csv("books.csv", encoding="utf-8")
books["price"] = books["price"].str.replace(r"[^0-9.]", "", regex=True).astype(float)

rating_map = {
  "One" : 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5
}

books["rating"] = books["rating"].map(rating_map)

print(books.head(5))
rating_avg_price = books.groupby("rating")["price"].mean()
print(rating_avg_price)

plt.hist(books["price"], bins=30, color="skyblue")
plt.savefig("chart.png")
plt.show()

analyze = {
  "total_books" : len(books),
  "avg_price": books["price"].mean(),
  "max_price": books["price"].max(),
  "min_price": books["price"].min(),
  "rating_avg_price": rating_avg_price
}

def get_books():
    return books.to_dict(orient="records")

print(books)
print(get_books())
print(analyze)