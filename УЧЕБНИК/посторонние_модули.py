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
    conteiner = soup.select_one("ol.row")     # полезно для вобора всех элементов таблицы
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
class numpy():
    import numpy as np
    # заполнить все строки во всех таблицах       [[255. 0. 0.],[255. 0. 0.]]
    array[:] = 255, 0, 0
    df[:, [0, 1]] # взять  2 столбца

    """ Найти процент совпадений двух массивов"""
    x = np.array([1, 2, 1, 2, 1, 1])
    y = np.array([1, 2, 1, 1, 1, 1])
    (x == y).mean()

    """ создать массив изменённый по условию"""
    np.where(a > 0.5, True, False)
    array([True, True, False, False, False, False, True, True, False,])

    """ символы без повторений |работает с векторами|"""
    set_a = np.unique(a)

    """ создать матрицу элементы | на диагонали -1 | остальные 0.5|"""
    a = -1.5 * np.eye(4, 5, 0) + 0.5 * np.ones((4, 5))

    """превратить массив в одномерный"""
    a.flatten()
    np.concatenate(a, axis = 0)

    """ транспонирование (или смена порядка осей в случае, когда размерность массива больше двух)."""
    a.T or a.transpose(*axes)

    """ смена формы массива. Массив "распрямляется" и построчно заполняется в новую форму."""
    a.reshape(1,2,3)
    # [1] Количество "матриц"
    # [2] Количество строк в каждой матрице
    # [3] Количество столбцов в каждой матрице

    """ одномерный массив из 12 случайных чисел от 1 до 1000"""
    np.array(random.sample(range(1000), 12))
    rgen = np.random.RandomState(1)
    w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])

    """ посчитать среднее арифметическое  """
    a.mean(axis=0)     # вдоль столбцов
    a.mean(axis=1)     # вдоль строк
    a.mean(axis=None)  # вдоль всего массива

    np.loadtxt("data.csv", usecols=(0, 1, 4), skiprows=1, delimiter=",",
               dtype={'names': ('date', 'open', 'close'),
                      'formats': ('datetime64[D]', 'f4', 'f4')})
    # [usecols] — | список колонок, которые нужно использовать | все |
    # skiprows  — | количество рядов в начале, которые нужно пропустить | skiprows = 0 |
    #              < пропустил ряд заголовков >
    # delimiter — | разделитель столбцов в одной строке | любой пробел  |

    """ удалить 1 столбец в файле"""
    x = np.delete(data, 0, axis=1)

    """ вставить матрицу `а` перед матрицей `x`1 (похоже на |str +|)"""
    np.hstack((a, x1))

# -------------------------------------------------------------------------------------------
class pandas():
    import pandas as pd
    df = pd.read_csv('iris.data', header = None, )
    index_col = 0 # чтобы 0 столбец стал индексами | df = df.set_index('Test1')

    """ махинации с столбцами """
    df.apply(pd.to_numeric, errors='coerce')
    df.apply(np.sqrt) # np.diff - считает разность между ближайшими наблюдениями ( полезно с датами) [1, 2, 5] --> [1, 3]
    df.fillna(0)    # заменить пропущенные значения на 0
    df.fillna({'Test1':0.0}, inplace=True)
    df.isna().sum() # найти количество пропусков
    df.columns.str.replace('/', '') # удалить символ в названиях

    df.drop([0, 5])      # удалить строки
    df.drop_duplicates() # удалить повторяющиеся строки subset = ['Test1', 'Test2']
    df.unique(), df.nunique()
    df.groupby('legs').size()  # группирует и выводит количество
'=   df['CountryRegion'].value_counts()

    """ отфильтровать 'Name' по значению столбца 'Age' """
    df.loc[df.Age <= 18.0, ['Name']]
    df.Age == 18.00 # возращает булевый массив
    df.query("lunch == 'standard' | gender == @temp") # temp -- переменная
    df.filter(like='bbi', axis=0) # нечёткий поиск по строкам( индексам )

    """ узнать инфу о таблице"""
    df['lunch'].describe()
    # unique    2
    # top    standard
    # freq    645

    """ группировка """
    df.groupby(['gender', 'race/ethnicity'], as_index=False).aggregate({'math score': 'mean'})
    df.groupby('gender').aggregate({'math score': ['mean', 'max'], 'reading score': 'min'})
    #  math score  <mean | max>        | reading score <min>
    # female | 63.633205 | 194.095945 | 206.733938     as_index = False (заменяет строковые индексы на числа )

    """ получить по 5 отличниковв разного пола """
    df.sort_values(['gender', 'math score'], ascending=False).groupby('gender').head(5)

    df.hist(
        column=str|array,# постоить график для определённой колонки
        grid=bool        # показывать линии сетку
        x|yrot=int       # повернуть индексы ( числа под графиком)
        x|ylabelsize=int # изменить размер индексов
        bins=int         # изменить количество столбцов( баров )
        by=str           # скруппировать по колонке
    )
    """ Построить несколько графиков в одном месте"""
    df[["Test_1", "Test_2"]].plot.hist(alpha=0.4, bins = 10)
    df.plot.scatter(x, y, s=None, c=None,)

    """ Постройте простую линейную зависимость между двумя переменными"""
    import seaborn as sns
    ax = sns.lmplot(x="Test_1", y="Test_2", data=df, markers=["o", "x"]) # строит разбросанные точки и прямую регрессии
    col='Test3'# группирует данные и строит отдельные графики
    hue='Test3'# группирует данные и раскрашивает на одном графике
    fit_reg=False# убрать прямую
    ax.set_x|ylabels('ось х') # переименовать ось

    # построить просто график
    sns.scatterplot(df.iloc[:, 0], df.iloc[:, 1])
    # гистограмма и график плотности распределения
    sns.distplot(df['Test1'])
    # построить тепловую карту
    sns.heatmap(df, cmap = 'viridis')
    """ построить тепловую карту пустых мест в таблице"""
    sns.heatmap(df.isnull(), xticklabels=True, yticklabels=False, cmap='viridis')
    # показать сетку из разных графиков ( распределение каждой переменной и их зависимость друг от друга)
    sns.pairplot(df, hue='species') # большая корреляция <---> график похож на y = x

# -------------------------------------------------------------------------------------------

class sklearn():
    from sklearn import tree
    """ построить разноцветное дерево решений """
    clf = tree.DecisionTreeClassifier(criterion='entropy')
    tree.plot_tree(clf.fit(X, y) , class_names=['Positive', 'Negative'], filled=True)

# -------------------------------------------------------------------------------------------
class PIL():
    from PIL import Image, ImageFilter, ImageDraw
    img = Image.open('picture.png')
    img.save("ass.png")

    img.show()  # показывает картинку в мини проигрывателе
    img.size()  # (960, 800)
    img.format()  # 'PNG'

    img.thumbnail((200, 200))  # уменьшает размер фотки
    crop_img = img.crop((0, 0, 100, 100))  # обрезает фотку по координатам
    r_img = img.rotate(180)  # поворот

    blurred_img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

    img = Image.new("RGBA", (400, 200), "red")
    idraw = ImageDraw.Draw(img)
    idraw.rectangle((50, 50, 100, 100), fill="green")

# -------------------------------------------------------------------------------------------
class cv2():
    import cv2

    """ показать на экране картинку """
    img = cv2.imread('picture.png')
    cv2.imshow('title', img)
    cv2.waitKey(0)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgCanny = cv2.Canny(img, 150, 200) # найти края на изображение
    kernel = np.ones((5, 5), np.uint8)  # расширить вывод краей
    imgDialation = cv2.dilate(imgCanny, kernel, iterations=5)
    imgResize = cv2.resize(img, (100, 100))              # изменит размер
    mini = cv2.resize(img, dsize=(0, 0), fx=0.5, fy=0.5) # уменьшит размер в 2 раза

    imgCropped = img[0:700, 500:900]        # обрезать

    """ запуск онлайн камеры"""
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        cv2.imshow('Live', img)
        if cv2.waitKey(10) == 27: break  # press `ESC`
    cap.release()
    cv2.destroyAllWindows()

    """ создать пустую картинку (h = 480, w = 640)"""
    img = np.zeros((480, 640, 3))  # 480 таблиц по 640 строк и 3 столбцам
    img[:] = 0, 255, 70  # покрасить всё изображение
    cv2.line(img, (0, 0), (300, 300), (0, 0, 255), 10)        # нарисовать линию (закруглена)
    cv2.rectangle(img, (100, 100), (300, 300), (0, 0, 255))   # нарисовать квадрат
    cv2.circle(img, (100, 100), 100, (0, 0, 255), cv2.FILLED) # нарисовать круг
    # написать текст размером=2 и толщиной=3
    cv2.putText(img, "ass", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 3)

    """ склеить 2 фотки"""
    imgVert = np.vstack((img, img))
    imgHor = np.hstack((img, img))

    """" создать track bar"""
    def empty(): ...
    cv2.namedWindow("TrackBars")
    cv2.resizeWindow('TrackBars', 640, 200)
    cv2.createTrackbar('Hue Min', 'TrackBars', 0, 179, empty)
    h_min = cv2.getTrackbarPos('Hue Min', "TrackBars")

# -------------------------------------------------------------------------------------------
"""
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
        print(i, i.attrib)   # <Element a at 0x36cf0d0> {'href': 'https://docs.python.org/2.7/'}

# -------------------------------------------------------------------------------------------
import atexit

""" Выполнить код по завершению программы"""
def hello(name): print(name)
for name in ['Geeks', 'for', 'Geeek']:
    atexit.register(hello, name)
print("-"*50)

# -------------------------------------------------------------------------------------------
import fileinput
""" Открывает файлы переданные как аргументы
    python3 main.py dict.txt"""
with fileinput.input(files="mail.py") as f:
    for line in f:
        print(line)

# -------------------------------------------------------------------------------------------
import argparse
parser = argparse.ArgumentParser(description="Search some file")
parser.add_argument(dest='filenames', metavar='filename', nargs='*')
parser.add_argument('-p', '--pat', metavar='pattern', required=True, dest='patterns',
                    action='append', help="text pattern to search for")
parser.add_argument('-v', dest='verbose', action='store_true', help="verbose mode")
parser.add_argument('-o', dest='outfile', action='store', help="output file")
parser.add_argument('--speed', dest='speed', action='store', choices={'slow', 'fast'},
                    default="slow", help="search speed")
args = parser.parse_args()
print(args)
print(args.filenames)
print(args.patterns)
print(args.verbose)
print(args.outfile)
print(args.speed)

# -------------------------------------------------------------------------------------------

"""  считайте данные из файла и посчитайте их средние значения """
f = urlopen('https://stepic.org/media/attachments/lesson/16462/boston_houses.csv')
print(np.loadtxt(f, skiprows=1, delimiter=",").mean(axis = 0))

""" построить график рассеивания для 2х классов"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv('iris.data', header=None)
y = df.iloc[0: 150, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)
x = df.iloc[0:100, [0, 2]].values
plt.scatter(x[:50, 0], x[:50, 1],
            color='red', marker='o', label='щетинистый')
plt.scatter(x[50:100, 0], x[50:100, 1],
            color='blue', marker='x', label='разноцветный')
plt.xlabel('чашелистник [см]')
plt.ylabel('лепесток [см]')
plt.legend(loc = 'upper left')
plt.show()

df = np.loadtxt("fruct.csv", delimiter=",")
pears = df[:, 2] == 1  # таблица |true or false, ... ,|
apples = np.logical_not(pears)
plt.scatter(df[apples][:, 0], df[apples][:, 1], color="red")
plt.scatter(df[pears][:, 0], df[pears][:, 1], color="green")
plt.xlabel("yellowness")
plt.ylabel("symmetry")
plt.show()

