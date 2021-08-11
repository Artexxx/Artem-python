import collections
import os
import pathlib
import linecache
import shutil
import csv
import mmap


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
class file():

    file=open("somefile.txt", mode="ab", encoding='utf-8', errors='ignore')
    file.write("hello word")
    print("hello word", file=file)

    # Значение символа
    # w  — открыть для записи, предыдущее содержимое файла стирается и перезаписывается
    # x  — создать новый файл для записи, если его нет в файловой системе
    # a  — открыть для записи, запись ведется в коней
    # b  — открыть в бинарном режиме
    # r+ —  открыть для чтения и записи
    # r  —  открыть для чтения
    # rb —  открыть для чтения на уровне байт
    # W+ — открыть для чтения и записи, содержимое файла стирается

    # Работа с ошибками кодировки (UnicodeEncodeError)
    #      Default text — français
    #            ignore — franais  # Отбрасывает данные
    #           replace — fran?ais # Заменяет вопросительным знаком (?)
    # xmlcharrefreplace — fran&#231;ais # Заменяет ссылкой на символ XML (без потери данных)
    #  backslashreplace — franWxe7ais # Заменяет на значение repr(unicode) (без потери данных)

    file.readline(), """Читает файл построчно, выводит текст с переносом строки — \n """

    """Прочитать строку с определенным номером (например, четвертую строку файла, )
    [#] linecache нумерует строки, начиная c 1. Служебные символы убираются.
    """
    linecache.getline('file.txt', 4),

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
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

    """Метод unlink используется для удаления файлов, символических сс ылок и большинства других типов путей"""
    pathlib.Path('example.txt').unlink()

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
class mmap():
    """mmap используется тогда, когда надо отобразить в память бинарный файл в форме изменяемого массива байтов"""

    def memory_map(file_name, access=mmap.ACCESS_WRITE):
        size = os.path.getsize(file_name)
        fd = os.open(file_name, os.O_RDWR)
        return mmap.mmap(fd, size, access=access)


    with memory_map('example.txt') as m:
        print(m.read()); m.seek(0) # перейти в начало
        m[-5:-2] = b'ABC'
        print(m.read()); m.seek(0) # перейти в начало
    """
    |                 Before                   |                 After                    |
    |——————————————————————————————————————————|——————————————————————————————————————————|
    |b'Example file. This is the content (123)'|b'Example file. This is the content (ABC)'|
    """

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
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
#     os.path.abspath("your_text"),"""Тоже самое, что os.getcwd() + '/your_text' -> C:/Users/admin/Desktop/your_text"""
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

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
class shutil():
    """Модуль для копировния и перемещения файлов"""
    # Копируем src в dst. (cp src dst)
    shutil.copy("file.txt","copy-file.txt") ,
    # Перемещаем  src в dst. (mv src dst)
    shutil.move("src", "dst"),
    # Копируем дерево каталогов. (cp -R src dst)
    shutil.copytree("src", "dst", ignore = shutil.ignore_patterns('*.py'))
    """ignore_dangling_symlinks=True — игнорирует битый ссылки"""

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
class sys():
    import sys

    """ Считать все строки по одной из стандартного потока ввода"""
    for raw_line in sys.stdin:
        line = raw_line.strip()
    #_____ or _____ #
    with open(0) as f:
        lines = f.read().splitlines()

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
class csv():
    """csv модуль для чтения и записи данных в CSV-файл"""

    """Чтение данных в именованный кортеж
    [#] Заголовки колонок должны быть валидными идентификаторами """
    with open("example.csv") as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        Row = collections.namedtuple('Row', headers)
        for r in f_csv: row = Row(*r); ...
    """
    | TIME, AV_USD, REFRESH, AV_GBP|                                Before                                |
    |——————————————————————————————|——————————————————————————————————————————————————————————————————————|
    |20:36:51, 672, 20:36:52, 1.23 | Row(TIME='20:36:51', AV_USD='672', REFRESH='20:36:52', AV_GBP='1.23')|
    |20:37:04, 673, 20:37:05, 1.22 | Row(TIME='20:37:04', AV_USD='673', REFRESH='20:37:05', AV_GBP='1.22')|
    |20:42:09, 671, 20:42:11, 1.21 | Row(TIME='20:42:09', AV_USD='671', REFRESH='20:42:11', AV_GBP='1.21')|
    """

    """Чтение данных в последовательность словарей"""
    with open("example.csv") as f:
        f_csv = csv.DictReader(f)
        for row in f_csv: ...
    """
    | TIME, AV_USD, REFRESH, AV_GBP|                                Before                                          |
    |——————————————————————————————|————————————————————————————————————————————————————————————————————————————————|
    |20:36:51, 672, 20:36:52, 1.23 | {'TIME': '20:36:51', 'AV_USD': '672', 'REFRESH': '20:36:52', 'AV_GBP': '1.23'} |
    |20:37:04, 673, 20:37:05, 1.22 | {'TIME': '20:37:04', 'AV_USD': '673', 'REFRESH': '20:37:05', 'AV_GBP': '1.22'} |
    |20:42:09, 671, 20:42:11, 1.21 | {'TIME': '20:42:09', 'AV_USD': '671', 'REFRESH': '20:42:11', 'AV_GBP': '1.21'} |
    """

    """Примеры записи данных"""
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)
    writer.writerows([["a"], ["b"]], quoting=csv.QUOTE_NONNUMERIC)
    # csv.QUOTE_ALL — все значения внутрь кавычек ''
    # csv.QUOTE_NONNUMERIC — все нечисловые значения внутрь кавычек ''

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
class xml():
    """XML(расширяемый язык разметки) / сами обозначем теги / используется для того чтобы хранить данные 
    <tag>содержимое</tag>
    также можно указывать атрибуты в открывающемся тэге
    примечание: похоже на дерево, имеет корень """
    from xml.etree import ElementTree

    tree=ElementTree.parse("name_file.xml") # возвращает дерево
    root=tree.getroot() # возвращает корень дерева

    for child in root: # возвращает детей корня дерева
        print(child.tag, child.attrib)

    print(root[1][0].text) # можно выводить значения так

    for element in root.iter("scores"): # Поиск значения по всему дереву
        for child in element:
            print(child.tag, child.text)

    artem=root[0]
    modul_1=next(artem.iter("module1"))
    modul_1.text="90"  # изменил значение,!!! надо перезаписать файл
    certificate=artem[2]
    certificate.set("type","cool result")# добавил атрибуты

    descript=ElementTree.Element("description")# создаём тэг
    descript.text="Showed Good Skills"
    artem.append(descript) # добавляем тэг

    descript=artem.find("description")
    artem.remove(descript) # удаляет тэг

    root = ElementTree.Element('student')# создаёт корень
    name=ElementTree.SubElement(root,"name")# указываем родителя и имя тэга, создаёт тэг
    name.text="Artem"

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#                                                Анализ путей
# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
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
    os.path.expanduser(r"~\Desktop"), """Выхлоп /  C:/Users/admin/Desktop /"""

    """Учитывая последовательность имен путей, возвращает самый длинный общий префикс-путь."""
    os.path.commonpath((r'C:\test\A', r'C:\test\B\C', r'C:\test\B\D'))
    """Выхлоп / C:/test /"""

    """Выводит путь до текущей папки """
    os.getcwd(), """Выхлоп / C:/Users/admin/Desktop /"""
    os.path.abspath("path"), """Тоже самое, что os.getcwd() + '/path' -> C:/Users/admin/Desktop/path"""

    """ Разбивает путь на пару (root, ext), где ext начинается с точки /( C:/Users/admin/file', '.py')"""
    os.path.splitext(r'C:\Users\admin\file.cp')

    os.path.join(r'C:\Users', 'admin'), """(  C:/Users стало -> C:/Users/admin  )"""

    """Пройтись рекурсивно по директориям и найти файл
     os.walk — возвращает кортеж из 3 элементов:   
     1 — строковое представление текущей директории 2 — список из всех под-папок 3 — список всех файлов в текущей директории"""
    start, fname = '/', "index.html"
    for path, dirlist, filelist in os.walk(start):
        if fname in filelist:
            file_path = os.path.join(start, path, fname)
            print(os.path.abspath(file_path))

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
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

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
class fnmatch():
    """
    fnmatch используется для сравнения имен файлов c шаблонами модуля glob в соответствии c правилами, применяемыми в командных оболочках Unix (например, *.py,Dat[0-9]*.csv и т.д.).
    """
    from fnmatch import fnmatch
    fnmatch('data001.csv', '*.csv') # Выхлоп / True /

    files = ('data001.csv', '1.png', '2.png')
    fnmatch.filter(files, '*.png')
    # Выхлоп / [1.png, 2.png] /

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
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

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

