# Football_goal -- считает какое количество голов в среднем Leicester City забивала за матч в 2018-2019 года.

from bs4 import BeautifulSoup
import requests

url = "https://www.worldfootball.net/teams/leicester-city/2018/3/"

res = requests.get(url)

html = res.text

soup = BeautifulSoup(html, "html.parser")
table = soup.find("table", {"class": "standard_tabelle"})
lines = table.find_all('tr')

i = 0
count = 0
for line in lines:
    elements = line.find_all("td")
    if len(elements) == 8:
        i += 1
        count += int(elements[6].text.strip().split(":")[0])
print(count / i)
