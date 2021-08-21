import collections
import json
import os
import pathlib
import linecache
import shutil
import csv
import mmap
from xml.etree import ElementTree

example_xml="""
<breakfast menu>
    <food>
        <name>Belgian Waffles</name>
        <calories>650</calories>
    </food>
    <food>
        <name>Strawberry Belgian Waffles</name>
        <calories>900</calories>
    </food>
    <food>
        <name>Berry-Berry Belgian Waf fles</name>
        <calories>900</calories>
    </food>
    <food>
        <name>French Toast</name>
        <calories>бOO</calories>
    </food>
    <food>
        <name>Homestyle Breakfast</name>
        <calories>950</calories>
    </food>
</breakfast menu> 
"""
example_dict = {'name': 'ACME', 'shape': 100, 'price': 542.23, 'address': None, 'availability': True, }


# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
class file():
    file=open("somefile.txt", mode="ab", encoding='utf-8', errors='ignore')
    file.write("Hello word")
    # Можно перенаправлять поток вывод в файл
    print("Hello word", file=file)
    # Можно открывать сразу несколько файлов
    with open("somefile1.txt", 'rb') as f1, open("somefile2.txt", 'wb') as f2: pass

    # Значение символа
    # w  ─ открыть для записи, предыдущее содержимое файла стирается и перезаписывается
    # x  ─ создать новый файл для записи, если его нет в файловой системе
    # a  ─ открыть для добавления, запись ведется в конец
    # b  ─ открыть в бинарном режиме
    # r+ ─  открыть для чтения и записи
    # r  ─  открыть для чтения
    # rb ─  открыть для чтения на уровне байт
    # W+ ─ открыть для чтения и записи, содержимое файла стирается

    # Работа с ошибками кодировки (UnicodeEncodeError)
    #      Default text ─ français
    #            ignore ─ franais  # Отбрасывает данные
    #           replace ─ fran?ais # Заменяет вопросительным знаком (?)
    # xmlcharrefreplace ─ fran&#231;ais # Замена ссылкой на подходящий символ XML (без потери данных)
    #  backslashreplace ─ franWxe7ais   # Замена Escape-последовательностями repr(unicode) (без потери данных)

    file.readline(), """Читает файл построчно, выводит текст с переносом строки ─ \n """

    """Прочитать строку с определенным номером (например, четвертую строку файла, )
    ⚫ linecache нумерует строки, начиная c 1. Служебные символы убираются.    """
    linecache.getline('file.txt', 4),

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
class pathlib():
    """Класс pathlib.Path() представляет пути файловой системы, которые работают с системными вызовами и являются подклассом pathlib.PurePath."""
    f = pathlib.Path('example.txt')

    """ Чтение и запись файлов """
    f.write_bytes('Создан новый файл'.encode('utf-8'))
    # Пример чтения через f.open
    with f.open('r', encoding='utf-8') as file:
        print(file.read())
    # Пример чтения через f.read_text
    print(f.read_text('utf-8'))

    """ Создание каталогов """
    p = pathlib.Path('example_dir')
    p.mkdir() # Если создаваемый путь существует, то возбуждается исключение FileExistsError
    p.rmdir() # Если папка не пуста, то возбуждается исключение  OSError

    """Метод unlink используется для удаления файлов, символических ссылок и большинства других типов путей"""
    pathlib.Path('example.txt').unlink()

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
class mmap():
    """mmap используется тогда, когда надо отобразить в память бинарный файл в форме изменяемого массива байтов"""

    def memory_map(file_name, access=mmap.ACCESS_WRITE):
        size = os.path.getsize(file_name)
        fd = os.open(file_name, os.O_RDWR)
        return mmap.mmap(fd, size, access=access)


    with memory_map('example.txt') as m:
        print(m.read()); m.seek(0) # перейти в начало
        m[-3:] = b'ABC'
        print(m.read()); m.seek(0) # перейти в начало
    """
    │                 Before                   │                 After                    │
    ├──────────────────────────────────────────┼──────────────────────────────────────────┤
    │ b'Example file. This is the content: 123'│ b'Example file. This is the content: ABC'│
    """

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
# class os():
#     import os
#     os.path.isdir(r"C:\Users"), """Выхлоп /  True /"""
#     os.path.isfile(r"C:\Users"),"""Выхлоп /  False /"""
#     os.listdir(r"C:\Users"),"""Показывает все (даже скрытые) файлы которые есть в директории"""
#     os.path.exists("test.txt"),"""/ True or False /Показывает существует ли путь до файла или папки"""
#
#     for current_dir, dirs, files in os.walk("."):""" возвращает кортеж из 3 элементов                """
#          print(current_dir, dirs, files) ,     """    1 - строковое представление текущей директории """
#                                                """    2 - список из всех подпапок                    """
#                                                """    3 - список всех файлов                         """
#
#     os.getcwd(), """Выводит путь до текущей папки / C:/Users/admin/Desktop /"""
#     os.path.abspath("your_text"),"""То же самое, что os.getcwd() + '/your_text' -> C:/Users/admin/Desktop/your_text"""
#
#     os.system("C:\питон37"),"""Имитация терминала  /os.system("ping google.com")
#                                                   /os.system("type test.txt") - просмотр файла"""
#
#     os.path.getsize("test.txt"),"""Размер файла в байтах"""
#
#     os.path.join(r'C:\Users', 'admin'),"""(  C:/Users стало -> C:/Users/admin  )"""
#     os.chdir("direktoria"), """Может перемещать по директориям БЫЛО(  C:/Users/admin стало -> C:/Users/admin/directoria  ) """
#
#     os.path.splitext(r'C:\Users\admin\file.cp') """ / Разбивает путь на пару (root, ext), где ext начинается с точки /( C:/Users/admin/file', '.py')"""

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
class shutil():
    """Модуль shutil (сокр от "shell utilities") предоставляет функции, позволяющие копировать и перемещать файлы, а также удалять целые деревья каталогов"""

    """Функция copy() (cp src dst) ─ копирует файл src в файл или каталог dst, заменяя содержимое существующего файла или создавая его.
    Если dst является каталогом, то файл будет скопирован в dst с использованием базового имени файла из src."""
    shutil.copy("file.txt", "copy-file.txt")

    """Функция copytree() (cp --recursive src/ dst/) ─ копирует папку src в каталог dst.
    ⚫ Каталог dst не должен существовать: он создается. 
    ignore: игнорируются файлы и директории, которые соответствуют glob-style шаблонам."""
    shutil.copytree("path/", "copy_path/", ignore = shutil.ignore_patterns('*.py'))

    """Функция rmtree() ─ удаляет директорию path"""
    shutil.rmtree("path/")

    """Функция move() (mv src dst) ─ рекурсивно перемещает файл или каталог src в dst.
    После перемещения src удаляется (с помощью os.unlink для файлов и rmtree для каталогов)"""
    shutil.move("src", "dst")

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
class sys():
    import sys

    """ Считать все строки по одной из стандартного потока ввода"""
    for raw_line in sys.stdin:
        line = raw_line.strip()
    #_____ or _____ #
    with open(0) as f:
        lines = f.read().splitlines()

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
class csv():
    """csv модуль для чтения и записи данных в CSV-файл (Comma-Separated Values)"""

    """Чтение данных в именованный кортеж
    ⚫ Заголовки колонок должны быть валидными идентификаторами """
    with open("example.csv") as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        Row = collections.namedtuple('Row', headers)
        for r in f_csv: row = Row(*r); ...
    """
    │ TIME, AV_USD, REFRESH, AV_GBP│                                Before                                │
    ├──────────────────────────────┼──────────────────────────────────────────────────────────────────────┤
    │20:36:51, 672, 20:36:52, 1.23 │ Row(TIME='20:36:51', AV_USD='672', REFRESH='20:36:52', AV_GBP='1.23')│
    │20:37:04, 673, 20:37:05, 1.22 │ Row(TIME='20:37:04', AV_USD='673', REFRESH='20:37:05', AV_GBP='1.22')│
    │20:42:09, 671, 20:42:11, 1.21 │ Row(TIME='20:42:09', AV_USD='671', REFRESH='20:42:11', AV_GBP='1.21')│
    """

    """Чтение данных в последовательность словарей"""
    with open("example.csv") as f:
        f_csv = csv.DictReader(f)
        for row in f_csv: ...
    """
    │ TIME, AV_USD, REFRESH, AV_GBP│                                Before                                          │
    ├──────────────────────────────┼────────────────────────────────────────────────────────────────────────────────┤
    │20:36:51, 672, 20:36:52, 1.23 │ {'TIME': '20:36:51', 'AV_USD': '672', 'REFRESH': '20:36:52', 'AV_GBP': '1.23'} │
    │20:37:04, 673, 20:37:05, 1.22 │ {'TIME': '20:37:04', 'AV_USD': '673', 'REFRESH': '20:37:05', 'AV_GBP': '1.22'} │
    │20:42:09, 671, 20:42:11, 1.21 │ {'TIME': '20:42:09', 'AV_USD': '671', 'REFRESH': '20:42:11', 'AV_GBP': '1.21'} │
    """

    """Примеры записи данных"""
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)
    writer.writerows([["a"], ["b"]], quoting=csv.QUOTE_NONNUMERIC)
    # csv.QUOTE_ALL ─ все значения внутрь кавычек ''
    # csv.QUOTE_NONNUMERIC ─ все нечисловые значения внутрь кавычек ''

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
class json():
    """json модуль для чтения и записи данных в JSON-файл (JavaScript Object Notation)"""

    """Примеры записи и чтения данных"""
    with open("example.json", 'wx') as f:
        json.dump(example_dict, f)
    """
    │    After: Python dict    │      Before: string     │
    ├──────────────────────────┼─────────────────────────┤
    │    {'address': None,     │  "{'address': null,     │  
    │    'availability': True, │   'availability': true, │
    │    'name': 'ACME',       │   'name': 'ACME',       │
    │    'price': 542.23}      │   'price': 542.23}"     │
    """
    with open("example.json", 'r') as f:
        data = json.load(f)

    """Сериализация экземпляров классов
    Функция для аргумента default вызывается для объектов, которые иначе не могут быть сериализованы. Обычно возникает TypeError.
    Функция для аргумента object_hook вызывается для каждого словаря, декодированного из входящего потока данных, предоставляя возможность преобразования словарей в объекты другого тип.
    """
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    def serialize_instance(obj)->dict:
        d = {'__classname__': type(obj).__name__}
        d.update(vars(obj)); return d

    def unserialize_object(d:dict):
        classes = {'Point': Point}
        class_name = d.pop('__classname__', None)
        if class_name:
            cls = classes[class_name]
            obj = cls.__new__(cls) # Создание экземпляра без конструктора __init__
            for attr, value in d.items(): setattr(obj, attr, value)
            return obj
        return d
    
    p = Point(x=12, y=3)
    s=json.dumps(p, default=serialize_instance) #  Выхлоп /  '{"__classname__": "Point", "x": 12, "y": 3}' /
    p=json.loads(s, object_hook=unserialize_object) #  Выхлоп /  Point(12, 3) /

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
class xml():
    """xml модуль для чтения и записи данных в XML-файл (extensible Markup Language )"""

    """Парсинг простых XML-данных"""
    tree = ElementTree.parse("name_file.xml")
    root = tree.getroot() # Возвращает корень дерева
    for element in root.iterfind("scores"): # Поиск значения по всему дереву
        for child in element: print(child.tag, child.text)

    """Парсинг больших XML-данных
    Пример файла на 500K cтрок: https://data.cityofchicago.org/Service-Requests/311-Service-Requests-Pot-Holes-Reported-Historical/7as2-ds3y
    В основе итеративный парсинг и удаление узлов.
    Итератор ElementTree.iterparse: производит кортежи вида (event, element), где event одно из событий (start│end).
    Событие start создается, когда элемент создан, но еще не наполнен потомками.
    """"""Пример:
    >>>for event, element in ElementTree.iterparse('menu.xml', ('start', 'end')): print(event, element)
    start <Element 'breakfast_menu'>
    start <Element 'food'>
        start <Element 'name'>
        end <Element 'name'>                  
        start <Element 'calories'>
        end <Element 'calories'>
    end <Element 'food'>
    [...]
    end <Element 'breakfast_menu'>"""
    def parse_and_remove(file_name, path):
        doc = ElementTree.iterparse(file_name, ('start', 'end'))
        path_parts = path.split('/')
        next(doc) # Пропуск корня
        tag_stack = []
        elem_stack = []
        for event, element in doc:
            if event == 'start':
                tag_stack.append(element.tag); elem_stack.append(element)
            elif event == 'end':
                if tag_stack == path_parts:
                    yield element
                    # удаляется узел родителя
                    elem_stack[-2].remove(element)
                try:
                    tag_stack.pop(); elem_stack.pop()
                except IndexError: pass

    potholes_by_zip = collections.Counter()
    tree = ElementTree.parse("rows.xml")
    for pothole in tree.iterfind('row/row'):
        potholes_by_zip[pothole.findtext('zip')] += 1
    # _____ vs _____ #  Mem usage:  1200 MiB vs 75 MiB
    for pothole in fast_generator("rows.xml", 'row/row'):
        potholes_by_zip[pothole.findtext('zip')] += 1

    """Преобразование python-словарей в XML """
    def dict_to_xml(tag:str, dict_):
        root = ElementTree.Element(tag)
        for key, value in dict_.items():
            child = ElementTree.SubElement(root, key)
            child.text = str(value)
        return root
    e = dict_to_xml('stock', example_dict)
    # Так можно прикрепить атрибуты к элементу:
    e.set('_id', '1234') # <stock _id="1234"><name>ACME</name><shape>100</shape> [...] </stock>


# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
#                                                Анализ путей
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
class os.path():
    """
    Набор функций модуля os.path можно использовать для разбора строк, представляющих имена файлов, на составные элементы.
    Эти функции никак не связаны c реальными путями и оперируют исключительно строками.
    """
    os.path.isdir(r"C:\Users"),  """Выхлоп /  True /"""
    os.path.isfile(r"C:\Users"), """Выхлоп / False /"""
    os.listdir(r"C:\Users"), """Показывает все, даже скрытые файлы, которые есть в директории"""
    os.path.exists(r"C:\Users"), """Выхлоп / False / Показывает существует ли путь до файла или папки"""
    os.path.getsize("test.txt"), """Размер файла в байтах"""

    """Преобразует символ тильды (~) в имя домашнего каталога пользователя. """
    os.path.expanduser(r"~\Desktop"), # Выхлоп /  C:/Users/admin/Desktop /

    """Учитывая последовательность имен путей, возвращает самый длинный общий префикс-путь."""
    os.path.commonpath((r'C:\test\A', r'C:\test\B\C', r'C:\test\B\D'))
    # Выхлоп / C:/test /

    """Выводит путь до текущей папки """
    os.getcwd(), # Выхлоп / C:/Users/admin/Desktop /
    os.path.abspath("path"), # То же самое, что и os.getcwd() + '/path' -> C:/Users/admin/Desktop/path

    """ Разбивает путь на пару (root, ext), где ext начинается с точки /( C:/Users/admin/file', '.py')"""
    os.path.splitext(r'C:\Users\admin\file.cp')

    os.path.join(r'C:\Users', 'admin'), # Выхлоп / 'C:/Users/admin' /

    """Пройтись рекурсивно по директориям и найти файл
     os.walk ─ возвращает кортеж из 3 элементов:   
     1 ─ строковое представление текущей директории 2 ─ список из всех под-папок 3 ─ список всех файлов в текущей директории"""
    start, fname = '/', "index.html"
    for path, dirlist, filelist in os.walk(start):
        if fname in filelist:
            file_path = os.path.join(start, path, fname)
            print(os.path.abspath(file_path))

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
class pathlib():
    """
    Модуль pathlib предоставляет объектно-ориентированный API для работы c путями файловой системы.
    Он обеспечивает большие удобства по сравнению c модулем os.path, поскольку оперирует объектами на более высоком уровне абстракции.
    """
    import pathlib
    path = pathlib.PurePosixPath(r"C:\Users\admin\Desktop\file_name.rst")

    # path:  'C:\Users\admin\Desktop\file_name.rst'
    # name:  'file_name.rst'
    # suffix: '.rst'
    # stem:  'file_name'
    # parts: ('C:\Users\admin\Desktop', 'file_name.rst')
    # parent: PurePosixPath('C:\Users\admin\Desktop')
    # parent: PurePosixPath('C:\Users\admin\Desktop')
    # parents: <PurePosixPath.parents>

    """Вывести содержимое каталога без рекурсии"""
    dir_path = pathlib.Path('temp_dir')
    list(dir_path.iterdir())
    # Выхлоп / Path('temp_dir/image.jpg'), Path('temp_dir/text.txt') /

    """ Получить список лишь тех файлов, которые соответствуют заданному шаблону
    Рекурсивное сканирование c использованием метода rglob() вместо glob().
    """
    imgdir_path = pathlib.Path('cat_dog_images')
    list(imgdir_path.glob('*.jpg'))
    # Выхлоп / 'cat_dog_images/cat-01.jpg', 'cat_dog_images/cat-02.jpg' /

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
class fnmatch():
    """
    fnmatch используется для сравнения имен файлов c шаблонами модуля glob в соответствии c правилами, применяемыми в командных оболочках Unix (например, *.py,Dat[0-9]*.csv и т.д.).
    """
    from fnmatch import fnmatch
    fnmatch('data001.csv', '*.csv') # Выхлоп / True /

    files = ('data001.csv', '1.png', '2.png')
    fnmatch.filter(files, '*.png')
    # Выхлоп / [1.png, 2.png] /

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
class glob():
    """
    Правила создания шаблонов для модуля glob отличаются от тех, которые используются для работы c регулярными выражениями модуля re.
    Они соответствуют правилам расширения путей, действующими в командной оболочке Unix, и подразумевают использование нескольких специальных символов для реализации двух групповых метасимволов и диапазонов символов.
    """
    import glob

    """Символу “звездочка” (*) соответствует любое количество символов в сегменте"""
    glob.glob('E:/Фото 1/*.jpg') # Фильтрация только внутри папки ”Фото 1”
    # Выхлоп / ['E:/Фото 1/A.jpg', 'E:/Фото 1/B.jpg',  'E:/Фото 1/C.png',]
    glob.glob('E:/*/*') # Фильтрация только внутри под-папок папки ”E:/”
    # Выхлоп / ['E:/Фото 2/B.jpg', 'E:/Фото 1/A.jpg',  'E:/Фото 3/G.png',]
    glob.glob('E:/**/*')  # Фильтрация внутри папки и под-папок ”E:/”
    # Выхлоп / ['E:/1.jpg', 'E:/Фото 1/A.jpg',  'E:/Фото 3/G.png',

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

