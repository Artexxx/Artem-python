#  ImgSpace.py - парсит фотки о космосе и сохраняет их.
import urllib

from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://wallpapershome.com"
SPACE = "/space/?page=4"

res = requests.get(BASE_URL + SPACE)
html = res.text

soup = BeautifulSoup(html, "html.parser")
conteiner = soup.find("div", {"class": "pics"})

images = conteiner.find_all("p")
urls_images = []
for image in images:
    id_image = image.a["href"].split("-")[-1].replace(".html", "")
    urls_images.append(f"https://wallpapershome.com/images/pages/pic_h/{id_image}.jpg")

for e, url in enumerate(urls_images):
    urllib.request.urlretrieve(url, f"IMG{e}.jpg")
