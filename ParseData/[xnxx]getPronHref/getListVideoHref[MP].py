""" Многопоточный парсер ссылок на видео с помощью BS4+Multiprocessing"""
import time
import re
import math
import multiprocessing as mp
import requests
from bs4 import BeautifulSoup
import sys


def get_html(url):
    try:
        res = requests.get(url)
        res.encoding = 'utf-8'
        html = res.text
    except:
        pass
    return html


def getVideoHref(html):
    soup = BeautifulSoup(html, 'lxml')
    href = soup.find_all(href=re.compile("video-"))
    return href


def getListVideoHref(searchkey='lolly'):
    search_url = 'https://www.xnxx.com/search/' + searchkey + '/'
    res = requests.post(search_url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'lxml')
    # Подсчет страниц
    try:
        video_count = soup.select_one("span.free-plate").text
        pageNum = math.ceil(int(re.sub("\D", "", video_count)) // 37) + 5
        pageList = [search_url + str(i) for i in range(pageNum)]
    except:
        pageNum = 10000

    # Решение RecursionError
    sys.setrecursionlimit(1000000)
    print('Начало парсинга, на 50 стр ~ 6s');start_time = time.time()

    pool = mp.Pool()
    crawl_jobs = [pool.apply_async(get_html, args=(url,)) for url in pageList]
    htmls = [j.get() for j in crawl_jobs]
    parse_jobs = [pool.apply_async(getVideoHref, args=(html,)) for html in htmls]
    results = [j.get() for j in parse_jobs]
    href_list = ['https://www.xnxx.com' + results[x][i].get('href')
                 for x in range(len(results))
                 for i in range(len(results[x]))]

    print('Время парсинга: %.1f s' % (time.time() - start_time,))
    links = list(dict.fromkeys(href_list))  # Удаление дубликатов
    return links


if __name__ == '__main__':
    from pprint import pprint

    list_video_href = getListVideoHref()
    pprint(list_video_href)
