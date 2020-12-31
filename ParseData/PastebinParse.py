# PastebinParse - находит заданные слова в файлах на сайте pastebin.com/archive
import requests
from bs4 import BeautifulSoup
import time
import os

BASE_URL = 'https://pastebin.com/'


def get_list_page():
    url = BASE_URL + 'archive'
    return requests.get(url).text


def get_pastes():
    page = get_list_page()
    soup = BeautifulSoup(page, "html.parser")
    return [
        {'name': a.text,
         'url': BASE_URL + a['href'],
         'id': a['href'].strip('/')}
        for a in soup.select('table.maintable tr a')]


def get_paste_text(id):
    # the raw text of the post
    url = f"{BASE_URL}raw/{id}"
    return requests.get(url).text


def contains_interesting_info(text):
    buzz_word = ['PyQt5.QtWidgets', 'BeautifulSoup', ' QApplication(sys.argv)',
                 'PyQt5.QtGui', 'mysql.connector', 'flask', 'Flask', 'porn']
    for word in buzz_word:
        if word in text:
            return True


def save_pastes(index, text, id=None):
    # file_name = id.replace('/','_')
    with open(os.path.join('Pastebin', f"{index}.txt"), 'w') as pasteFile:
        pasteFile.write(text)


def timer_text():
    seen_paste_ids = set()
    while True:
        pastes = get_pastes()
        for index, paste in enumerate(pastes):
            if paste['id'] not in seen_paste_ids:
                text = get_paste_text(paste['id'])
            if contains_interesting_info(text):
                # save_pastes(paste['id'], index, text)
                # qsave_pastes(index, text)
                print(paste['id'])
                print(text)
                print("_" * 100)
            else:
                print(f"[{index}]NotFind")

            seen_paste_ids.add(paste['id'])
            time.sleep(0.15)
        time.sleep(60)


os.makedirs('Pastebin', exist_ok=True)
timer_text()
