"""
Этот скрипт идет на wallhaven и находит случайные 1980x1080 NSFW аниме обои, применяет или просто загружает для вас.
https://wallhaven.cc/search?categories=010&purity=010&resolutions=1920x1080&sorting=random&order=desc&seed=457jK&page=2
    -- (это url-адрес по умолчанию, на который идет скрипт),
       настройте свои категории, скопировав url-адрес непосредственно в скрипт (строка 17)

"""
import requests
from bs4 import BeautifulSoup
import os
import argparse
import glob
import getpass
import webbrowser


def get_image(set_img):
    url = "https://wallhaven.cc/search?categories=010&purity=010&resolutions=1920x1080&sorting=random&order=desc"
    picture_page = soup_from_url(url).find("a", {"class": "preview"}).get("href")
    image_url = soup_from_url(picture_page).find("img", {"id": "wallpaper"}).get("src")
    img_data = requests.get(image_url).content
    image_path = get_path() + picture_page.split("/")[-1]

    with open(image_path, "wb") as handler:
        handler.write(img_data)
    print("Link to the image page : " + picture_page)
    if set_img:
        set_image(image_path)
    elif not set_img:
        webbrowser.open(picture_page)


def set_image(path):
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri " + path)


def set_last_image():
    path = get_path() + "*"
    list_of_files = glob.glob(path)
    latest_file = max(list_of_files, key=os.path.getctime)
    set_image(latest_file)


def get_path():
    path = "/home/" + getpass.getuser() + "/Pictures/anime-wallpapers/"
    return path


def soup_from_url(url):
    html = requests.get(url).content
    return BeautifulSoup(html, features="html.parser")


def main():
    parser = argparse.ArgumentParser(description="Easily get a random NSFW anime girl for your desktop UwU")
    parser.add_argument("-n", "--get_new", action="store_true",
                        help="get new wallpaper and apply as desktop background")
    parser.add_argument("-g", "--get", action="store_true",
                        help="get a hot anime girl, without applying as desktop background")
    parser.add_argument("-a", "--apply", action="store_true", help="use to apply last image you've downloaded")
    args = parser.parse_args()

    if args.get_new:
        get_image(True)
    elif args.get:
        get_image(False)
    elif args.apply:
        set_last_image()


if __name__ == "__main__":
    main()