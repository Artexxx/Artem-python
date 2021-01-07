"""
Пролистывает https://www.reddit.com/r/Fairytail_hentai/

Использован конкретный субреддит, но этот код может быть использован и на любом другом субреддите аналогичным образом.
 - вход в систему не требуется.

Этот скрипт очищает динамически генерируемый веб-сайт в течение определенного периода времени (по умолчанию: 10 минут).
 - Чтобы изменить длительность, измените переменную end_time в секундах.
 - Чтобы изменить скорость прокрутки, измените переменную SCROLL_PAUSE_TIME в секундах.
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import sys

url = "https://www.reddit.com/r/Fairytail_hentai/"


class Post:
    def __init__(self):
        self.title = "NOT FOUND"
        self.user = "NOT FOUND"
        self.upvotes = "NOT FOUND"
        self.comments = 0
        self.imgsrc = "NOT FOUND"
        self.date = "NOT FOUND"



def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()


driver = webdriver.Chrome()
driver.get(url)
print("[#] sleep 1..."); time.sleep(5)
print("[#] You must be 18+ to view this community...")
yes_btn = driver.find_elements_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div[1]/div/div/div[2]/button')[0]
yes_btn.click()

SCROLL_PAUSE_TIME = 5
last_height = driver.execute_script("return document.body.scrollHeight")

print("[#] sleep 2..."); time.sleep(5)
print("[#] wake 2...")

end_time = int(time.time() + (10 * 60))
while (int(time.time()) <= end_time):
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        print("[#] Page end reached!")
        break
    last_height = new_height

print("[#] Final sleep...10 sec"); time.sleep(10)
print("Woke up...")
res = driver.execute_script("return document.documentElement.outerHTML")
print("-- over --")

soup = BeautifulSoup(res, 'lxml')
divs = soup.findAll("div", {"tabindex": "-1"})
post_list = []
counter = 0
for div in divs:
    post = Post()
    try:
        title = div.find("h3", {"class": "_eYtD2XCVieq6emjKBH3m"})
        post.title = title.text
    except: ...
    try:
        user_name = div.find("a", class_="_2tbHP6ZydRpjI44J3syuqC _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE")
        post.user = user_name.text
    except: ...
    try:
        upvotes = div.find("div", {"class": "_1rZYMD_4xY3gRcSS3p8ODO"})
        post.upvotes = upvotes.text
    except: ...
    try:
        date = div.find("a", {"class": "_3jOxDPIQ0KaOWpzvSQo-1s"})
        post.date = date.text
    except: ...
    try:
        comment = div.find("span", class_="FHCV02u6Cp2zYL0fhQPsO")
        comm = comment.text.split()[0]
        if (comm.lower() == 'comment'):
            post.comments = 0
        else:
            post.comments = comm
    except: ...
    try:
        img_src = div.find("img", {"class": ["_2_tDEnGMLxpM6uOa2kaDB3", "_2c1ElNxHftd8W_nZtcG9zf"]})
        post.imgsrc = img_src['src']
    except: ...

    post_list.append(post)
    counter += 1

print("[#] loop end")
print(len(post_list))
for post in post_list:
    print(f'title: {post.title}')
    print(f'user: {post.user}')
    print(f'upvotes: {post.upvotes}')
    print(f'comments: {post.comments}')
    print(f'src: {post.imgsrc}')
    print(f'date: {post.date}\n')

counter = 0
for post in post_list:
    if (post.imgsrc == 'NOT FOUND'):
        counter = counter + 1

print(f"[@] {counter} out of {len(post_list)} don't have img-src")

erza_list = []
for post in post_list:
    title = post.title.lower()
    if ('erza') in title:
        erza_list.append(post)

print("[@] len(erza list) = ", len(erza_list))
print("[#] done")

for post in erza_list:
    if (post.imgsrc != 'NOT FOUND'):
        print(post.title)
        print(post.imgsrc)
        print(f"{post.upvotes} upvotes")
        print(f"{post.comments} comments")
        print(post.date)
        print()

## create csv ##
data_rows = []
for post in post_list:
    title = post.title.encode('ascii', errors='ignore').decode('utf-8')
    data_rows.append([title, post.user, post.imgsrc, post.upvotes, post.comments, post.date])
data_rows.insert(0, ['title', 'posted_by', 'img_src', 'upvotes', 'comments', 'date'])
with open('subredditData.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data_rows)
print("[#] CSV done")
