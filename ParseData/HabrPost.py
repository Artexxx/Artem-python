# HabrPost.py -- парсит инфу о постах и открывает url интересных постов

import webbrowser
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://habr.com/ru/hub/python/all/page"


def get_info_about_post(soup) -> list:
    age = soup.find("span", {"class": "post__time"}).text.split(" ")[2]
    title = soup.find("a", {"class": "post__title_link"}).text
    href = soup.find("a", {"class": "post__title_link"})["href"]
    return [age, title, href]


def parse_page(soup):
    conteiner = soup.find("div", {"class": "posts_list"})
    posts = conteiner.find_all('article', {"class": "post"})
    for num, post in enumerate(posts):
        info = get_info_about_post(post)
        post_data[-1].append([num, info[-1]])
        print(num, *info[:-1])


post_data = []  # для нахождения url поста по номеру поста
for x in range(1, 3):
    print("START page", x, "_" * 100)
    post_data.append([])

    res = requests.get(BASE_URL + str(x))
    html = res.text
    soup = BeautifulSoup(html, "html.parser")
    parse_page(soup)
    print("END page", x, "_" * 100)

while True:
    print("Укажите номер страницы и интересного вам поста.")
    try:
        nums = list(map(int, str(input()).split(" ")))
        url = post_data[nums[0] - 1][nums[1]][-1]
        webbrowser.open(url)
    except:
        print("*** Error! Print only INT numbers!")
