# TextParser -- создаёт `data.txt` и сохраняет в него топ больших звёзд.

import requests
from bs4 import BeautifulSoup

url = "http://light-science.ru/kosmos/vselennaya/top-10-samyh-bolshih-zvezd-vo-vselennoj.html"
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 YaBrowser/19.12.3.332 (beta) Yowser/2.5 Safari/537.36"}

res = requests.get(url, headers=header)

html = res.text

soup = BeautifulSoup(html, 'lxml')

conteiner = soup.find("div", {"class": "td-post-content"})
elements = conteiner.find_all("p")

string = "Топ больших звёзд:\n"

for element in elements:
    if element.find("strong"):
        string += "\t" + element.find("strong").text + "\n"
with open("data.txt", "w", encoding='utf8') as file:
    file.write(string)


