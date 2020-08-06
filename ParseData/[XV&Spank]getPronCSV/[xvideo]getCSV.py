from bs4 import BeautifulSoup
import multiprocessing as mp
import concurrent.futures
import requests
import pyprind
import time
import csv
import sys


class xvideos_scrapper:
    def __init__(self):
        self.Npages = None
        self.max_workers = 6

    def save_to_csv(self, terms, name='xvid'):
        """
        Сохраняет в файл созданные данные.
        terms (str) ключевые слова для поиска.
            Пример: 'teen schoolgirl 18yo'
        """
        fname = f'{name}.csv'
        search_terms = terms.replace(' ', '+')
        self.url = f'https://www.xvideos.com/?k={search_terms}'
        csv_data = self.get_all_data()

        with open(fname, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            headersf = ['title', 'total_time', 'vid_quality', 'view_ct', 'uploader_name', 'upvotes', 'downvotes',
                        'video_tags', 'comment_ct', 'url']
            writer.writerow(headersf)
            for c in csv_data:
                writer.writerow(c)

    def get_all_data(self):  # TODO
        """
        Объеденяет данные из множества потоков, для записи в файл.
        :return csv_data
        """
        all_urls = self.get_all_urls(self.Npages)
        pbar = pyprind.ProgBar(len(all_urls))
        print('\n\nНачало сбора данных, на 2500 видео ~ 10m')
        csv_data = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as ex:
            results = [ex.submit(self.create_data_list, l) for l in all_urls]
            for k in concurrent.futures.as_completed(results):
                csv_data.append(k.result())
                pbar.update()
        return csv_data

    def create_data_list(self, url):
        """
        Создаёт данные по конкретному видео.
        url - относительный адрес видео
            Пример: '/video53666101/first_footjoob_for_young_girl_'
        :return data (list, len=10)
        """
        self.soup = self._load_page(f'https://www.xvideos.com{url}')
        if not self.soup:
            return None
        data = []
        data.append(self.get_title())
        data.append(self.get_total_time())
        data.append(self.get_video_quality())
        data.append(self.get_view_count())
        data.append(self.get_uploader_name())
        data.append(self.get_upvotes())
        data.append(self.get_downvotes())
        data.append(self.get_video_tags())
        data.append(self.get_comment_ct())
        data.append(f'https://www.xvideos.com{url}')
        return data

    def get_all_urls(self, N_pages=None):
        '''
        Переходит по страницам и собирает относительные ссылки на видео.
        N_pages (int) регулирует количество страниц,
        - (default) пока страницы не повторятся (страницы закончились)
        Можно управлять фильтром:
            1. (default) & sort=uploaddate & durf=10-20min
            2. &sort=views&durf=10-20min
        :return: all hrefs
        '''
        # Формирование ссылок на страницы
        pageList = []
        filter = "&sort=uploaddate&durf=10-20min"
        page_mask = f'{self.url}{filter}&p='
        for i in range(N_pages or 10000):
            pageList.append(page_mask + str(i))
        sys.setrecursionlimit(1000000)
        pool = mp.Pool()
        print('Начало парсинга всех URL-адресов, на 100 стр ~ 10s');
        start_time = time.time()
        parse_jobs = [pool.apply_async(self.getVideoHref, args=(url, i))
                      for i, url in enumerate(pageList)]
        all_urls = []
        for i, job in enumerate(parse_jobs):
            page_result = job.get()
            if page_result:
                all_urls.extend(page_result)
            else:
                break
        print('Время парсинга: %.1f s' % (time.time() - start_time,))
        print('Пройдено страниц:', i)
        return all_urls

    def get_page_urls(self, soup):
        '''
        Предполагая, что страница была загружена,
            получает все относительные URL-адреса видео на этой странице,
        Пример: '/video53666101/first_footjoob_for_young_girl_'
            - для создания ссылки, надо просто добавить 'https://www.xvideos.com'
        '''
        all_urls = []
        res = soup.findAll('div', {'class': 'thumb'})
        for r in res:
            pot_hrefs = str(r.contents[0]['href'])
            if (pot_hrefs[:2] == '/v'):
                all_urls.append(pot_hrefs)
        return all_urls

    def getVideoHref(self, url, prev_page):
        """
        Связующая функция get_all_urls c get_page_urls
        :param prev_page: номер предыдущей страницы
        :return: page_urls & curr_page or None
        """
        soup = self._load_page(url)
        # идея заключается в том, что curry_page никогда не должен быть prev_page, если не происходит повторений.
        res = soup.findAll('a', {'class': 'active'})
        for r in res:
            if len(r['class']) != 1:
                continue
            curr_page = int(r.string)
            if (prev_page == curr_page):
                return None
        return self.get_page_urls(soup)

    def _load_page(self, url):
        """ :return BeautifulSoup"""
        page = requests.get(url)
        if (page.status_code == 200):
            return BeautifulSoup(page.text, features='lxml')
        else:
            print('\n' + url, page.status_code)

    def get_title(self):
        res = self.soup.findAll('h2', {'class': "page-title"})
        for r in res:
            return str(r.contents[0])

    def get_uploader_name(self):
        result = self.soup.findAll('span', {'class': 'name'})
        for r in result:
            return (str(r.string))

    def get_upvotes(self):
        result = self.soup.findAll('a', {'class': 'vote-action-good'})
        for r in result:
            result2 = r.findAll('span', {'class': 'rating-inbtn'})
            for r2 in result2:
                return (str(r2.string))

    def get_downvotes(self):
        result = self.soup.findAll('a', {'class': 'vote-action-bad'})
        for r in result:
            result2 = r.findAll('span', {'class': 'rating-inbtn'})
            for r2 in result2:
                return (str(r2.string))

    def get_comment_ct(self):
        result = self.soup.findAll('span', {'class': 'thread-node-children-count'})
        for r in result:
            return (int(r.string))

    def get_video_tags(self):
        all_tags = ''
        result = self.soup.findAll('div', {'class': 'video-tags-list'})
        for r in result:
            result2 = r.findAll('li')
            for r2 in result2:
                pot_tag = str(r2.contents[0].get('href'))
                if (pot_tag[:2] == '/t'):
                    all_tags += f'{str(r2.string)}|'
        return all_tags[:-1]

    def get_video_quality(self):
        res = self.soup.findAll('span', {'class': 'video-hd-mark'})
        if (len(res) == 0):
            return '0p'
        else:
            for r in res:
                return str(r.string)

    def get_view_count(self):
        res = self.soup.findAll('strong')
        for r in res:
            return str(r.string)

    def get_total_time(self):
        result = self.soup.findAll('span', {'class': 'duration'})
        for r in result:
            return str(r.string)


if __name__ == '__main__':
    x = xvideos_scrapper()
    tags = '18yo'
    x.url = f'https://www.xvideos.com/?k={tags}'
