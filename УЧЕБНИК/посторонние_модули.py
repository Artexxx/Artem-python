# -------------------------------------------------------------------------------------------
class scrapy():  # модуль который может скачивать из интернета,читать и парсить сайты
    #        (в папке проекта)
    # scrapy runspider auto_ru.py --output=data.json -сохраняет заголовки с сайта в файл
    # scrapy runspider auto_ru.py --output=data.json -L WARNING
    import scrapy
    class BlogSpider(scrapy.Spider):
        name = 'blogspider'
        start_urls = ['https://blog.scrapinghub.com']

        def parse(self, response):
            for title in response.css('.post-header>h2'):
                yield {'title': title.css('a ::text').get()}

            for next_page in response.css('a.next-posts-link'):
                yield response.follow(next_page, self.parse)

    """ Дополнить ссылку картинки без `http`"""
    response.urljoin(img)

# -------------------------------------------------------------------------------------------
class urllib_request():  # модуль который может скачивать из интернета,читать и парсить сайты
    import urllib.request

    """urlretrieve скачивает файл из интернета давая имя nameFile"""
    urllib.request.urlretrieve(url, nameFile)

    urllib.request.urlopen("http://www.python.org")
# -------------------------------------------------------------------------------------------
class Beautiful_Soup():
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(contents, 'lxml');
    """Создается объект BeautifulSoup. Данные передаются конструктору. """
    # выводится только первый из них.
    print(soup.h2.string)
    print(soup.head)
    print(soup.li)
    print(soup.all_tags(True))  # все тэги на странице

    elements = soup.select("div.mycontent")
    conteiner = soup.select_one("ol.row")  # полезно для вобора всех элементов таблицы
    url = product.select_one("h3 a")["href"]  # =  h3.a

    # attrs -- возвращает список классов объекта
    for elements in products:  # soup.find_all("div", {"class": "Porn"})
        print(product.attrs)  # ->{'class': ['class1', 'class2', 'class3']}

    image = product.find("img")['src']
    link = element.find("a", {"data-item-name": "detail-page-link"})["href"]

    # следующий тег
    description = soup.find("div", {"class": "sub-header"}).find_next("p").text

    for tag in soup.find_all("li"):
        print("{0}: {1}".format(tag.name, tag.text))


# -------------------------------------------------------------------------------------------
"""
Вот команды, которые нам понадобятся в гите:
git clone ссылка путь_куда_клонировать
git pull (получает обновления с хаба)
git log (чекнуть чё было пока я отошёл)
git status (проверяет изменения на локалке)
git branch (просмотр всех веток)
git checkout feauture (переключение ветки)
git add . (фиксирование изменений)
git commit -m "task #11 change_file_HZ_NAHUYA" (сделать коммит)
git push -u origin feauture (отправить коммит в свою ветку на хабе)"""


# -------------------------------------------------------------------------------------------

class PyQt5_QtWidgets():  # графическая библеотека

    root = QApplication(sys.argv)
    """Параметр sys.argv это список аргументов командной строки.
                                       Скрипты Python можно запускать из командной строки. """


# -------------------------------------------------------------------------------------------

class lxml():  # библеотека lxml похожа на стандартную xml
    from lxml import etree
    import requests

    res = requests.get('https://docs.python.org/3/')
    parser = etree.HTMLParser()  # парсер html позволяет работать с плохосформированными данными
    root = etree.fromstring(res.text, parser)  # передаём данные html и парсер
    # root-корень дерева, дальше как и с библеотекой xml
    for i in root.iter("a"):  # поддеревья с тегом a
        print(i, i.attrib)  # <Element a at 0x36cf0d0> {'href': 'https://docs.python.org/2.7/'}

# -------------------------------------------------------------------------------------------
