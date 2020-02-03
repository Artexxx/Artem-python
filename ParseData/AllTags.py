# AllTags.py - анализирует все тэги на странице.

import requests
from bs4 import BeautifulSoup


def get_list_tags_names(all_tags) -> list:
    return [tag.name for tag in all_tags]


url = "http://books.toscrape.com/"
res = requests.get(url)
html = res.text
soup = BeautifulSoup(html, "html.parser")

all_tags = soup.find_all(True)

tags_names = get_list_tags_names(all_tags)

stat_tags = sorted([[x, tags_names.count(x)] for x in set(tags_names)], key=lambda x: x[1], reverse=True)
print(stat_tags)
