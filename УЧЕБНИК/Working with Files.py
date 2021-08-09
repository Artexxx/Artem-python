# ----------------------------------------------------------------------------------------------------------------------
class file(): # Работа с файлами
    a=open("text.txt","w") , """Создаёт файл text.txt"""
    a.close()

    open("text.txt", "rb"), """Читает файл text.txt на уровне байт"""

    open("text.txt", "ab"), """Добавляет данные в файл"""
    file.write("hello word")

    # w (write) - открыть для записи, содержимое файла стирается
    # a (append) - открыть для аписи, запись ведется в коней
    # b (binary) - открыть в бинарном режиме
    # r+ -  открыть для чтения и записи
    # W+  - открыть для чтения и записи, содержимое файла стирается
    file.readline(), """Читает файл построчно, выводит текст с переносом строки — \n """

    """Прочитать строку с определенным номером (например, четвертую строку файла, )
    [#]  linecache нумерует строки, начиная c 1. Служебные символы убираются
    """
    import linecache
    linecache.getline('file.txt', 4),

    with open('test.txt', 'r') as file: """Читает файл text.txt и закрывает его"""
        print(file.read())

# ----------------------------------------------------------------------------------------------------------------------
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

# ----------------------------------------------------------------------------------------------------------------------
class shutil(): "Модуль для копировния и перемещения файлов"
    import shutil
    # Копируем src в dst. (cp src dst)
    shutil.copy("file.txt","copy-file.txt") ,
    # Перемещаем  src в dst. (mv src dst)
    shutil.move("src", "dst"),
    # Копируем дерево каталогов. (cp -R src dst)
    shutil.copytree("src", "dst", ignore = shutil.ignore_patterns('*.py'))
    """ignore_dangling_symlinks=True — игнорирует битый ссылки"""

# ----------------------------------------------------------------------------------------------------------------------
class sys():
    import sys

    """ Считать все строки по одной из стандартного потока ввода"""
    for raw_line in sys.stdin:
        line = raw_line.strip()
    #_____ or _____ #
    with open(0) as f:
        lines = f.read().splitlines()

# ----------------------------------------------------------------------------------------------------------------------
class csv():# Comma-Separated Values — (значения, разделённые запятыми)
    import csv
    csv.reader(file)# делает из текста файла [таблицы], разделитель-[,]
    csv.reader(file,delimiter="-")#  разделитель — [-]

    writer = csv.writer(file)
    writer.writerows([["a"],["b"]])# делает из [таблиц] текст  , разделитель-[,]
    writer.writerows([["a"], ["b"]], quoting=csv.QUOTE_NONNUMERIC)
    # csv.QUOTE_ALL - все значения внутрь кавычек ''
    # csv.QUOTE_NONNUMERIC - все нечисловые значения внутрь кавычек ''

# ----------------------------------------------------------------------------------------------------------------------
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

# ----------------------------------------------------------------------------------------------------------------------
#                                                      Анализ путей
# ----------------------------------------------------------------------------------------------------------------------
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

    os.path.splitext(r'C:\Users\admin\file.cp')
    """ Разбивает путь на пару (root, ext), где ext начинается с точки /( C:/Users/admin/file', '.py')"""

    os.path.join(r'C:\Users', 'admin'), """(  C:/Users стало -> C:/Users/admin  )"""



    for current_dir, dirs, files in os.walk("."): """ возвращает кортеж из 3 элементов                """
        print(current_dir, dirs, files), """    1 - строковое представление текущей директории """
                                         """    2 - список из всех под-папок                    """
                                         """    3 - список всех файлов                         """

# ----------------------------------------------------------------------------------------------------------------------
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

    """Содержимое каталога"""
    dir_path = pathlib.Path('temp_dir')
    list(dir_path.iterdir())
    # Выхлоп / Path('temp_dir/image.jpg'), Path('temp_dir/text.txt') /

    """ Получить список лишь тех файлов, которые соответствуют заданному шаблону
    Рекурсивное сканирование c использованием метода rglob() вместо glob().
    """
    imgdir_path = pathlib.Path('cat_dog_images')
    list(imgdir_path.glob('*.jpg'))
    # Выхлоп / 'cat_dog_images/cat-01.jpg', 'cat_dog_images/cat-02.jpg' /

# ----------------------------------------------------------------------------------------------------------------------
class fnmatch():
    """
    fnmatch используется для сравнения имен файлов c шаблонами модуля glob в соответствии c правилами, применяемыми в командных оболочках Unix (например, *.py,Dat[0-9]*.csv и т.д.).
    """
    from fnmatch import fnmatch
    fnmatch('data001.csv', '*.csv') # Выхлоп / True /
    fnmatch.filter(files, pattern)

# ----------------------------------------------------------------------------------------------------------------------
class glob():
    """
    Правила создания шаблонов для модуля glob отличаются от тех, которые используются для работы c регулярными выражениями модуля re.
    Они соответствуют правилам расширения путей, действующими в командной оболочке Unix, и подразумевают использование нескольких специальных символов для реализации двух групповых метасимволов и диапазонов символов.
    """
    import glob

    """Символу “звездочка” (*) соответствует любое количество символов в сегменте"""
    glob.glob('E:/Фото 1/*')
    # Выхлоп / ['E:/Фото 1/A.jpg', 'E:/Фото 1/C.jpg',  'E:/Фото 1/D.png',]
    glob.glob('E:/*/*')
    # Выхлоп / ['E:/Фото 2/B.jpg', 'E:/Фото 1/A.jpg',  'E:/Фото 3/G.png',]

# ----------------------------------------------------------------------------------------------------------------------
class cook():
    """ Пройтись по директориям и найти файл """
    def findFile(start, name):
        for r, d, files in os.walk(start):
            if name in files:f_p = os.path.join(start, r, name);print(os.path.abspath(f_p))
    findFile("/", 'index.html'),

