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

    # Следующий тег
    description = soup.find("div", {"class": "sub-header"}).find_next("p").text

    for tag in soup.find_all("li"):
        print("{0}: {1}".format(tag.name, tag.text))


# -------------------------------------------------------------------------------------------
class numpy():
    import numpy as np
    array[:] = 255, 0, 0 # заполнить все строки во всех таблицах   [[255. 0. 0.] ... [255. 0. 0.]]
    df[:, [0, 1]] # Возвращает 2 столбца
    img[:, :, 0] или img[..., 0] # Возвращает красный канал изображения

    """ Найти процент совпадений двух массивов"""
    x = np.array([1, 2, 1, 2, 1, 1])
    y = np.array([1, 2, 1, 1, 1, 1])
    (x == y).mean()

    """ Создать массив изменённый по условию"""
    np.where(x > 0.5, True, False)
    # Выхлоп / np.array[1, 2, 1, 2, 1, 1] -> array[False, True, False, True, False, False] /

    """ Символы без повторений"""
    set_a = np.unique(x)
    # Выхлоп /np.array[1, 2, 1, 2, 1, 1] -> array([1, 2]) /
    
    """Создать матрицу элементы | на диагонали -1 | остальные 0.5|"""
    x = -1.5 * np.eye(4, 5, 0) + 0.5 * np.ones((4, 5))

    """Превращает массив в одномерный"""
    x.flatten()
    x.ravel()
    np.concatenate(x, axis=0)
    # Выхлоп / np.array[[1, 2, 3],[4, 5, 6]] -> array[1, 2, 3, 4, 5, 6]/

    """Циклическое сместить элементы вдоль указанной оси"""
    np.roll(x, shift=2, axes=1)
    # Выхлоп / np.array[1, 2, 3, 4, 5, 6] -> array[5, 6, 1, 2, 3, 4]/

    """Превращает широкий массив в длинный """
    x[:, np.newaxis] или x.reshape(6, 1)
    # Выхлоп / array[[1],[2],[1],[2],[1],[1]] /

    """ Транспонирование (или смена порядка осей в случае, когда размерность массива больше двух)."""
    x.T или x.transpose(*axes)

    """ Смена формы массива. Массив "распрямляется" и построчно заполняется в новую форму."""
    x.reshape(1,2,3)
    # [1] Количество "матриц"
    # [2] Количество строк в каждой матрице
    # [3] Количество столбцов в каждой матрице

    """ Одномерный массив из 12 случайных чисел от 1 до 1000"""
    np.array(random.sample(range(1000), 12))
    rgen = np.random.RandomState(1)
    w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])

    """ Посчитать среднее арифметическое  """
    x.mean(axis=0)     # вдоль столбцов
    x.mean(axis=1)     # вдоль строк
    x.mean(axis=None)  # вдоль всего массива

    np.loadtxt("data.csv", usecols=(0, 1, 4), skiprows=1, delimiter=",",
               dtype={'names': ('date', 'open', 'close'),
                      'formats': ('datetime64[D]', 'f4', 'f4')})
    # [usecols] — | список колонок, которые нужно использовать | все |
    # skiprows  — | количество рядов в начале, которые нужно пропустить | skiprows = 0 |
    #              < пропустил ряд заголовков >
    # delimiter — | разделитель столбцов в одной строке | любой пробел  |

    """Удалить 1 столбец"""
    x = np.delete(data, 0, axis=1)

    """Обрезает (ограничивает) значения в массиве."""
    np.clip(x, a_min, a_max)
    # Выхлоп \array[3, 0, 2, 32, 0.5]\->/array[1, 0, 1, 1, 0.5 ]/

    """Вставить матрицу `x` перед матрицей `x`1 (похоже на |str +|)"""
    np.hstack((x, x1))
    np.vstack()       # соединяет матрицы по вертикали
    np.column_stack() # соеденяет матрицы по колонкам

    """Можно быстро выделить все три канала следующим образом:"""
    r, g, b = np.dsplit(img, 3)
    img = np.dstack((r,g,b)) # объединить назад

    """Векторизация Numpy с помощью функции numpy.vectorize то же самое, что и `map`"""
    cube = lambda x: x**3
    cube = np.vectorize(cube, otypes=[float])
    # Выхлоп / cube(np.arange(2,5)) -> array[8, 27, 64] /

    """Универсальная функция"""
    # nin, nout: Количество входных и выходных аргументов для этой функции.
    add = lambda x1, x2: x1 + x2
    add = np.frompyfunc(add, nin=2, nout=1)
    # Выхлоп / add([75, 10], [25, 40]) -> array[100, 50] /  add([75, 10], 25) -> array[100, 35]

# -------------------------------------------------------------------------------------------
class pandas():
    import pandas as pd
    df = pd.read_csv('iris.data', header = None, )
    index_col = 0 # чтобы 0 столбец стал индексами | df = df.set_index('Test1')
    parse_dates = ["date"] # привести столбцы к типу дата

    df.apply(pd.to_numeric, errors='coerce')
    df.apply(np.sqrt) # np.diff - считает разность между ближайшими наблюдениями ( полезно с датами) [1, 2, 5] --> [1, 3]
    df.pct_change()   # Процентное изменение между текущим и предыдущим элементом
    df.fillna(0)    # заменить пропущенные значения на 0
    df.fillna({'Test1':0.0}, inplace=True)
    df.isna().sum() # найти количество пропусков
    df.columns.str.replace('/', '') # удалить символ в названиях
    df["sales"].replace("[$,]", "", regex=True).astype("float") # удаление по регулярному выражению
    df['sales'].str.contains('Web|Mobile', regex=True, case=False) # возвращает логичский ряд, содержащий содержится-ли регулярное выражение в строке ряда

    df.drop([0, 5])      # удалить строки
    df.drop_duplicates() # удалить повторяющиеся строки subset = ['Test1', 'Test2']
    df.unique(), df.nunique()
    df.groupby('legs').size()  # группирует и выводит количество
    df['CountryRegion'].value_counts()
    _.get_group('XL')

    """Отфильтровать 'Name' по значению столбца 'Age' """
    df.loc[df.Age <= 18.0, ['Name']]
    df.Age == 18.00 # Возвращает булевый массив
    df.query("lunch == 'standard' | gender == @temp") # temp -- переменная
    df.filter(like='bbi', axis=0) # нечёткий поиск по строкам( индексам )

    """Вывести инфу о таблице"""
    df['lunch'].describe()
    # unique    2
    # top    standard
    # freq    645

    """Группировка """
    df.groupby(['gender', 'race/ethnicity'], as_index=False).aggregate({'math score': 'mean'})
    df.groupby('gender').aggregate({'math score': ['mean', 'max'], 'reading score': 'min'})
    #  math score  <mean | max>       | reading score <min>
    # female | 63.633205 | 194.095945 | 206.733938     as_index = False (заменяет строковые индексы на числа )

    """Получить по 5 отличниковв разного пола """
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

class tensorflow():
    import tensorflow as tf
    """Создание тензоров (tf.Tensor)"""
    a = np.array([1, 2, 3], dtype=np.int32)
    b = [4, 5, 6]
    t_a = tf.convert_to_tensor(a)
    t_b = tf.convert_to_tensor(b)
    # Выхлоп a:/ tf.Tensor([1 2 3], shape=(3,), dtype=int32) /
    # Выхлоп b:/ tf.Tensor([1 2 3], shape=(3,), dtype=int32) /
    t_ones = tf.ones((2, 3))
    t_ones.shape
    # рандомные числа
    tf.random.uniform(shape=(3, 5), seed=1, maxval=0.1, minval=-0.1)

    # Выхлоп размер:/ TensorShape([2, 3]) /
    """Обращение tf.Tensor в np"""
    t_ones.numpy()
    # Выхлоп / array([[1., 1., 1.) /
    """Махинации с матрицами"""
    tf.cast(t_a, tf.int64) # изменяет dtype тензора
    tf.transpose(t)        # транспонирование
    tf.reshape(t, shape=(5, 6)) # изменение размера
    tf.multiply(t1, t2).numpy() # умножение матриц
    tf.split(t, 3) # разделяет вектор на 3 части (только раные отрезки)
    C = tf.concat([a, a, a, a], axis=0) # склеивает несколько векторов (по горизонтали) или матриц (по вертикали)
    tf.stack([A, B], axis=1) # склеивает несколько матриц (по горизонтали)

    """ TensorFlow Dataset """
    a = [1.2, 3.4, 7.5, 4.1, 5.0, 1.0]
    ds = tf.data.Dataset.from_tensor_slices(a)
    for item in ds: print(item)
    # Выхлоп / tf.Tensor(1.2, shape=(), dtype=float32) ......
    # .......  tf.Tensor(1.0, shape=(), dtype=float32) /

    ds_batch = ds.batch(3) # нарезка Dataset на мини-пакеы
    for i, elem in enumerate(ds_batch, 1):
        print('batch {}:'.format(i), elem.numpy())
    # Выхлоп / batch 1: [1.2 3.4 7.5]
    #......... batch 2: [4.1 5.  1.] /

    """ Объединение двух тензоров в единый набор данных """
    X = tf.convert_to_tensor([[6, 3 ,15],[2, 3 , 5]])
    y = tf.convert_to_tensor([1.0, 0, 1.0, 0, 1.0, 1.0])

    ds_x = tf.data.Dataset.from_tensor_slices(X)
    ds_y = tf.data.Dataset.from_tensor_slices(y)
    ds_joint = tf.data.Dataset.zip((ds_x, ds_y))
    for example in ds_joint:
        print('  x: ', example[0].numpy(), '  y: ', example[1].numpy())
    # Выхлоп /  x:  [6 3 15]   y:  1.0
    #........   x:  [2 3 5 ]   y:  0.0
    # <~~~> 2 МЕТОД + lambda|shuffle
    ds_joint = tf.data.Dataset.from_tensor_slices((X, y))
    ds_trans = ds_joint.map(lambda x, y: (x * 2 - 1.0, y))
    ds_shuffle = ds_joint.shuffle(buffer_size=len(X))
    for example in ds_shuffle:
        print('  x: ', example[0].numpy(), '  y: ', example[1].numpy())
    # Выхлоп /   x:  [2 3 5 ]   y:  0.0 (перемешались пакеты)
    #........    x:  [6 3 15]   y:  1.0

    """ Чтение данных"""
    import pathlib
    imgdir_path = pathlib.Path('cat_dog_images')
    file_list = sorted([str(path) for path in imgdir_path.glob('*.jpg')])
    # Выхлоп / 'cat_dog_images/cat-01.jpg', 'cat_dog_images/cat-02.jpg' /
    import matplotlib.pyplot as plt
    import os
    fig = plt.figure(figsize=(10, 5))
    for i, file in enumerate(file_list):
        img_raw = tf.io.read_file(file)
        img = tf.image.decode_image(img_raw)
        print('Image shape: ', img.shape)
        ax = fig.add_subplot(2, 3, i + 1)
        ax.set_xticks([]); ax.set_yticks([])
        ax.imshow(img)
        ax.set_title(os.path.basename(file), size=15)
    plt.show()
    # Выхлоп / Image shape:  (900, 1200, 3)
    # .......  Image shape:  (900, 1200, 3) /

# -------------------------------------------------------------------------------------------
class tensorflow1():
    import tensorflow.compat.v1 as tf
    tf.disable_v2_behavior()

    """ Изменить размер фото """
    from keras_preprocessing.image import ImageDataGenerator
    IMG_SIZE = 100
    TEST_DIR = "fruits-360/Test"
    test_datagen = ImageDataGenerator(rescale=1. / 255)
    test_generator = test_datagen.flow_from_directory(TEST_DIR, target_size=(IMG_SIZE, IMG_SIZE))
    x, y = train_generator.next()
    for i in range(0, 3):
        image = x[i];plt.imshow(image); plt.show()

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

    imgCropped = img[0:700, 500:900] # обрезать

    """ Запуск онлайн камеры"""
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        cv2.imshow('Live', img)
        if cv2.waitKey(10) == 27: break  # press `ESC`
    cap.release()
    cv2.destroyAllWindows()

    """ Создать пустую картинку (h = 480, w = 640)"""
    img = np.zeros((480, 640, 3))  # 480 таблиц по 640 строк и 3 столбцам
    img[:] = 0, 255, 70  # покрасить всё изображение
    cv2.line(img, (0, 0), (300, 300), (0, 0, 255), 10)        # нарисовать линию (закруглена)
    cv2.rectangle(img, (100, 100), (300, 300), (0, 0, 255))   # нарисовать квадрат
    cv2.circle(img, (100, 100), 100, (0, 0, 255), cv2.FILLED) # нарисовать круг
    # написать текст размером=2 и толщиной=3
    cv2.putText(img, "ass", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 3)

    """ Склеить 2 фотки"""
    imgVert = np.vstack((img, img))
    imgHor = np.hstack((img, img))

    """" Создать track bar"""
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
parser.add_argument('-p', '--pat', metavar='pattern', required=True, dest='patterns', action='append', help="text pattern to search for")
parser.add_argument('-v', dest='verbose', action='store_true', help="verbose mode")
parser.add_argument('-o', dest='outfile', action='store', help="output file")
parser.add_argument('--speed', dest='speed', action='store', choices={'slow', 'fast'}, default="slow", help="search speed")
args = parser.parse_args()
print(args)
print(args.filenames)
print(args.patterns)
print(args.verbose)
print(args.outfile)
print(args.speed)

# -------------------------------------------------------------------------------------------
import sqlite3
import os

def create_SQL_table():
    """ Создаёт новую базу данных в каталоге `movieclassifier`"""
    if os.path.exists('reviews.sqlite'):
        os.remove('reviews.sqlite')
    conn = sqlite3.connect('reviews.sqlite')
    c = conn.cursor()
    c.execute('CREATE TABLE review_db (review TEXT, sentiment INTEGER, date TEXT)')
    example1 = 'I love this movie :)'
    c.execute("INSERT INTO review_db (review, sentiment, date) VALUES (?, ?, DATETIME('now'))", (example1, 1))
    example2 = 'I disliked this movie :('
    c.execute("INSERT INTO review_db (review, sentiment, date) VALUES (?, ?, DATETIME('now'))", (example2, 0))
    conn.commit()
    conn.close()


def sqlite_entry(path='reviews.sqlite', document, y):
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("INSERT INTO review_db (review, sentiment, date)" \
              " VALUES (?, ?, DATETIME('now'))", (document, y))
    conn.commit()
    conn.close()

def get_data(path='reviews.sqlite'):
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("SELECT * FROM review_db WHERE date BETWEEN '2020-05-20 10:10:10' AND DATETIME('now')")
    results = c.fetchall()
    conn.close()
    return results

""" Получение данных порциями (по 1000)"""
c.execute('SELECT * from review_db'), batch_size=1000
results = c.fetchmany(batch_size)

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

