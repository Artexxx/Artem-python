# TableRiverTop -- берёт данные из таблицы и сохраняет
import csv

from bs4 import BeautifulSoup
import requests

url = "https://ru.wikipedia.org/wiki/Список_городов_России"

res = requests.get(url)

html = res.text

soup = BeautifulSoup(html, "html.parser")
conteiner = soup.find("div", {"class": "mw-parser-output"})

trs = conteiner.find_all('tr')
cities = [["Город", "Регион", "Федеральный округ", "Население", "Основание или певое упоминание", "Статус"]]


def inform_to_city(tds: "tag") -> list:
    inform = []
    for i in range(2, len(tds) - 1):
        inform.append(tds[i].text)
    # Пример - [Адыгейск, Адыгея, Южный, 12689, 1969, 1976]
    return inform


# cities = /div/table/tbody/tr/td
for tr in trs:
    tds = tr.find_all("td")
    if len(tds) == 8:
        inf_city = inform_to_city(tds)
        cities.append(inf_city)

with open("data.txt", "w", encoding="utf8") as f:
    writer = csv.writer(f)
    writer.writerows(cities)
