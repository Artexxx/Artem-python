# GenerateTableHtml.py - ворует  html таблицу и создаёт другую в html

import requests
from bs4 import BeautifulSoup


def get_info_about_story(element) -> list:
    name = element.select("a")[0].text
    url = element.select("a")[0]['href']
    like = element.select("span.likes")[0].text
    return [url, name, like]


def add_in_html_table(story: list) -> str:
    url = story[0]
    name = story[1]
    like = story[2]
    return f'\t<li><a href="{url}"> {name} </a> <span>рейтинг: {like} <span> </li>\n'


BASE_URL = "https://azku.ru/russkie-narodnie-skazki/index.php"
res = requests.get(BASE_URL)
html = res.text
soup = BeautifulSoup(html, "html.parser")

elements = soup.select("div.mycontent")

stories = []
for element in elements:
    stories.append(get_info_about_story(element))

table_element = ""
for story in stories:
    table_element += add_in_html_table(story)

table = f'''<ul>
         {table_element}
        </ul>'''

with open("index.html", "w", encoding="utf8") as f:
    f.write(table)
