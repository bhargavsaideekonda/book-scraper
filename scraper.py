import requests
from bs4 import BeautifulSoup
r = requests.get("https://books.toscrape.com/",  timeout=10)
r.encoding = "utf-8"
soup = BeautifulSoup(r.text, "html.parser")
# BeautifulSoup sets up the board: it turns the page text into a tree of tags.
# Then soup moves like a queen: it jumps straight to any tag (soup.h1, find_all).
books = soup.find_all("article", class_="product_pod")
import csv
with open('books.csv', 'w', newline='', encoding="utf-8-sig") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['title', 'price', 'rating', 'stock'])
    for i in range(len(books)):
        book = books[i]
        title =book.h3.a["title"]
        price = book.find("p", class_="price_color")
        price = price.text
        rating = book.find("p", class_="star-rating")
        rate = rating["class"][1]
        stock = book.find("p", class_="instock availability")
        stock = stock.text.strip()
        print(f"{title} | {price} | {rate} | {stock}")
        writer.writerow([title, price, rate, stock])