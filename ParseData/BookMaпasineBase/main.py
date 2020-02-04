# Сохраняем |данные| о книгах в определённом жанре в БД (Sqlite)
#           |>название, описание, цену ...<|

import requests
from bs4 import BeautifulSoup
import sqlite3


def get_info_about_product(soup) -> list:
    name = soup.select_one("h1").text
    price = soup.select_one("p.price_color").text[2:]
    description = soup.find("div", {"class": "sub-header"}).findNext("p").text
    info = str(soup.select_one("table.table.table-striped"))
    return [name, price, description, info]


URL = "http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html"
BASE_URL = "http://books.toscrape.com/catalogue"
res = requests.get(URL)

html = res.text

soup = BeautifulSoup(html, "html.parser")
conteiner = soup.select_one("ol.row")

products = conteiner.find_all("li")

urls_products = []
for product in products:
    url = product.select_one("h3 a")["href"]
    urls_products.append(BASE_URL + "/" + url.replace("../../../", ""))

books = []
for url in urls_products:
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, "html.parser")
    books.append(get_info_about_product(soup))

conn = sqlite3.connect("mydata.db")

cursor = conn.cursor()

cursor.executemany("INSERT INTO books VALUES (?,?,?,?)", books)
conn.commit()
conn.close()
