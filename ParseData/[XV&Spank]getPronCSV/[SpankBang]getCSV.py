"""
~~~~~~~~~~ nuitka ~~~~~~~~~~~~~~
$ nuitka SpankbangScrapper.py
$ ./SpankbangScrapper.exe

~~~~~~~~~~ cython3 ~~~~~~~~~~~~~~
$ cython3 SpankbangScrapper.py --embed
$ gcc $(python3-config --includes) SpankbangScrapper.c -lpython3.6m -o SpankbangScrapper.exe
$ ./SpankbangScrapper.exe
"""
from bs4 import BeautifulSoup
import multiprocessing as mp
import concurrent.futures
import requests
import pyprind
import time
import csv
import sys


class SpankbangScrapper:

    def save_to_csv(self, terms, name='spankbang'):
        """
        Сохраняет в файл созданные данные.
        terms (str) ключевые слова для поиска.
            Пример: 'teen schoolgirl 18yo'
        """
        fname = f'{name}.csv'
        search_terms = terms.replace(' ', ',')
        self.url = f'https://spankbang.com/tag/{search_terms}/'

        csv_data = self.get_all_data()

        with open(fname, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            headersf = ['title', 'total_time', 'vid_quality', 'view_ct', 'uploader_name',
                        'rating', 'video_tags', 'comment_ct', 'url']
            writer.writerow(headersf)
            for column in csv_data:
                writer.writerow(column)

    def get_all_data(self):  # TODO
        """
        Объеденяет данные из множества потоков, для записи в файл.
        :return csv_data
        """
        all_urls = self._get_all_urls()
        pbar = pyprind.ProgBar(len(all_urls))
        print('\n\nНачало сбора данных, на 2500 видео ~ 10m')
        csv_data = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
            results = [ex.submit(self._create_data_list, url) for url in all_urls]
            for k in concurrent.futures.as_completed(results):
                csv_data.append(k.result())
                pbar.update()
        return csv_data

    def _get_all_data_low(self):  # TODO
        """
        Объеденяет данные из множества потоков, для записи в файл.
        :return csv_data
        """
        all_urls = self._get_all_urls()
        pool = mp.Pool()
        print('Начало сбора данных, на 3000 видео ~ 10m');start_time = time.time()
        parse_pages = [pool.apply_async(self._create_data_list, args=(url,)) for url in all_urls]
        csv_data = []
        for page in parse_pages:
            video_result = page.get()
            csv_data.append(video_result)
        print('Время парсинга: %.1f s' % (time.time() - start_time,))
        return csv_data

    def _create_data_list(self, url):
        """
        Создаёт данные по конкретному видео.
        url - относительный адрес видео
            Пример: '/3mdqk/video/dont+tell+dad+after'
        :return data
        """
        self.soup = self._load_page(f'https://www.spankbang.com{url}')
        data = []
        data.append(self.get_title())
        data.append(self.get_total_time())
        data.append(self.get_video_quality())
        data.append(self.get_view_count())
        data.append(self.get_uploader_name())
        data.append(self.get_rating())
        data.append(self.get_video_tags())
        data.append(self.get_comment_ct())
        data.append(f'https://www.spankbang.com{url}')
        return data

    def _get_all_urls(self, N_pages=None):
        '''
        Переходит по страницам и собирает ссылки на видео.
        N_pages (int) регулирует количество страниц,
            - (default) пока не закончатся
        Можно управлять фильтром:
            1. (default) ?order=new & period=all
            2. ?period=all & 720p=1 & max_length=30
            3. ?order=rated & period=all & max_length=30
        :return: all hrefs
        '''
        # Формирование ссылок на страницы
        pageList = []
        filter = "/?order=new&period=all"
        for i in range(N_pages or 100):
            pageList.append(self.url + str(i) + filter)

        sys.setrecursionlimit(1000000)
        pool = mp.Pool()
        print('Начало парсинга всех URL-адресов, на 50 стр ~ 10s');start_time = time.time()
        parse_jobs = [pool.apply_async(self.getVideoHref, args=(url,)) for url in pageList]
        all_urls = []
        for i, job in enumerate(parse_jobs):
            page_result = job.get()
            if page_result:
                all_urls.extend(page_result)
            else:
                break
        print('Время парсинга: %.1f s' % (time.time() - start_time,))
        print('Пройдено страниц:', i + 1)
        return all_urls

    def get_page_urls(self, soup):
        '''
        Предполагая, что страница была загружена,
          получает все относительные URL-адреса видео на этой странице,
          - если видео нет, возращает пустой массив.
        Пример: '/3mdqk/video/dont+tell+dad+after'
               - для создания ссылки, надо просто добавить 'https://spankbang.com/'
        '''
        all_urls = []
        res = soup.findAll('div', {'class': 'results'})
        for r in res:
            res2 = r.findAll('a', {'class': 'thumb'})
            for r2 in res2:
                all_urls.append(r2["href"])
        return all_urls

    def _load_page(self, url):
        """ :return BeautifulSoup"""
        page = requests.get(url)
        if (page.status_code == 200):
            return BeautifulSoup(page.text, features='lxml')
        else:
            print(url, page.status_code)

    def getVideoHref(self, url):
        return self.get_page_urls(self._load_page(url))

    def get_title(self):
        res = self.soup.findAll('h1')
        for r in res:
            return (str(r.contents[0]).strip())

    def get_video_quality(self):
        res = self.soup.findAll('div', {'class': 'play_cover'})
        for r in res:
            res2 = r.findAll('span', {'class': 'i-hd'})
            for r2 in res2:
                return (str(r2.string).strip())

    def get_view_count(self):
        res = self.soup.findAll('div', {'class': 'play_cover'})
        for r in res:
            res2 = r.findAll('span', {'class': 'i-plays'})
            for r2 in res2:
                return (str(r2.string).strip())

    def get_total_time(self):
        res = self.soup.findAll('div', {'class': 'play_cover'})
        for r in res:
            res2 = r.findAll('span', {'class': 'i-length'})
            for r2 in res2:
                return (str(r2.string).strip())

    def get_uploader_name(self):
        result = self.soup.findAll('li', {'class': 'us'})
        for r in result:
            result2 = r.findAll('a')
            for r2 in result2:
                uPos = str(r2['href']).find('t/')
                return (r2['href'][uPos + 2:])

    def get_rating(self):
        result = self.soup.findAll('span', {'class': 'rate'})
        for r in result:
            return (str(r.string))

    def get_comment_ct(self):
        result = self.soup.findAll('section', {'class': 'all_comments'})
        for r in result:
            result2 = r.findAll('h2')
            for r2 in result2:
                startInd = r2.string.find('(')
                endInd = r2.string.find(')')
                return (str(r2.string)[startInd + 1:endInd])

    def get_video_tags(self):
        all_tags = ''
        result = self.soup.findAll('div', {'class': 'ent'})
        for r in result:
            result2 = r.findAll('a')
            for r2 in result2:
                all_tags += f'{str(r2.string)}|'
        return all_tags[:-1]

if __name__ == '__main__':
    spank = SpankbangScrapper()
    # url = 'https://spankbang.com/tag/18yo/'
    tags = 'teen schoolgirl 18yo'
    spank.save_to_csv(tags)
