# -------------------------------------------------------------------------------------------
class urllib_request():  # модуль который может скачивать из интернета,читать и парсить сайты
    import urllib.request

    urllib.request.urlretrieve(url, nameFile)
    """urlretrieve скачивает файл из интернета давая имя nameFile"""


# -------------------------------------------------------------------------------------------
class Beautiful_Soup():
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(contents, 'lxml');
    """Создается объект BeautifulSoup. Данные передаются конструктору. """
    # выводится только первый из них.
    print(soup.h2.string)
    print(soup.head)
    print(soup.li)

    # attrs -- возвращает список классов объекта
    elements = soup.select("div.mycontent")
    for elements in products:  # soup.find_all("div", {"class": "Porn"})
        print(product.attrs)  # ->{'class': ['class1', 'class2', 'class3']}

    image = product.find("img")['src']
    link = element.find("a", {"data-item-name": "detail-page-link"})["href"]

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
