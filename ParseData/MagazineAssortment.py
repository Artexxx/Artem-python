# MagazineAssortment - парсит данные о Велосипедах с интернет магазина и сохраняет

import csv

import requests
from bs4 import BeautifulSoup


def get_info_product(product) -> list:
    image = product.find("img")['src']
    name = product.find("div", {"class": "product-name"}).text
    code = product.find("div", {"class": "product-model"}).text
    description = product.find("div", {"class": "product-description"}).text
    price = product.find("p", {"class": "price"}).text.strip().replace("р.", "")
    return [name, code, description, price]


url = "http://sportunit.ru/velosipedy?limit=100"
res = requests.get(url)

html = res.text
response = requests.get(url)

soup = BeautifulSoup(html, "html.parser")
multy_class = ['product-layout', 'product-grid', 'col-lg-4', 'col-md-4', 'col-sm-6', 'col-xs-12']
products = soup.find_all("div", {"class": "col-xs-12"})

all_product = []

for product in products:
    if product.attrs['class'] == multy_class:
        all_product.append(get_info_product(product))

names = ["Наименование", "Артикль", "Описание", "Цена"]

with open("data.csv", "w", encoding="utf8") as f:
    writer = csv.writer(f)
    writer.writerow(names)
    writer.writerows(all_product)
