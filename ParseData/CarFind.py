# CarFind.py -- Ищет инфу о машинах и сохраняет в json

import json
import requests
from bs4 import BeautifulSoup


def get_info_to_car(element):
    name = element.find("div", {"class": "cldt-summary-title"}).text
    price = element.find("div", {"class": "cldt-summary-payment"}).text
    mileage = element.find("ul", {"data-item-name": "vehicle-details"}).find_all("li")[0].text
    year = element.find("ul", {"data-item-name": "vehicle-details"}).find_all("li")[1].text
    link = element.find("a", {"data-item-name": "detail-page-link"})["href"]
    return [name, price, mileage, year, link]


base_url = "https://www.autoscout24.com"

query = "/lst/renault?sort=price&desc=0&ustate=N%2CU&size=20&page={}&fregfrom=2015&atype=C&"

all_elements = []

for x in range(1, 21):
    res = requests.get(base_url + query.format(x))
    print(f"Status: page {x}")
    html = res.text

    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.find_all("div", {"class": "cl-list-element-gap"})
    for element in elements:
        all_elements.append(get_info_to_car(element))

with open("data.json", "w", encoding="utf8") as file:
    json.dump(all_elements, file)

print("RESULT:", len(all_elements))

with open("data.json", "r", encoding="utf8") as f:
    data = json.load(f)
    print(data[0:len(data)])
