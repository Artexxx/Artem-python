# Statistic.py -  количество посетителей с разными ОС за последние 3 месяца.

import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://www.liveinternet.ru/stat/ru/oses.html"
QUERY = "?date={}&period=month&per_page=20"
data = []
for x in range(1, 4):
    date = "2019-0{}-01".format(x)
    res = requests.get(BASE_URL + QUERY.format(date))
    html = res.text

    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", {"bgcolor": "#e8e8e8"})

    lines = table.find_all("tr")
    current = {date: []}
    for line in lines[1:-4]:
        name = line.find_all("td")[1].text.strip()
        count = line.find_all("td")[2].text.strip().replace(",", "")
        current[date].append([name, count])

    data.append(current)
with open("data.json", "w", encoding="utf8") as f:
    json.dump(data, f)
