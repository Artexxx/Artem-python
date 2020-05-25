# -*- coding: utf-8 -*-
#  0 -> class regular # регулярки
#  1 -> class str():  #  работа с текстом и форматирование
#  2 -> class list():  #  работа со списками
#  3 -> class pyautogui():"""Библеотека автоматического питона"""
#  4 -> class try():  #  Как лучше всего использовать Try Except в Python
#  5 -> class file(): # работа с файлами
#  6 -> class os(): # модуль os
#  7 -> class shutil():"модуль для копировния и перемещения файлов"
#  8 -> class tkinter():" графический модуль tkinter"
#  9 -> class sys():
#  10 -> class recept():

# 1E6 = 100_000_000
# ----------------------------------------------------------------------------------------------------------------------
class format():  #  форматирование - подстановка значения в общий шаблон

    """Метод format подставляет те значения которые мы передали аргументами на то место где фигурные скобки"""
    template = "{m} oralcumshot {a}"       # шаблон
    template.format(a="Artem", m="Masha")  # можем указывать пустые скобки
    # Выхлоп / Artem oralcumshot Masha /

    x = 0.3141932# округляет до 3х знаков после запятой
    print("{:.3}".format(x))
    # Выхлоп / 0.314 /

    '{:,}'.format(1234)
    #  Выхлоп / 1.234/

    "{0:08}".format(128) # переводит в 8 систему счисления
    #  Выхлоп / 1 0000 0000/

# ----------------------------------------------------------------------------------------------------------------------
class regular_expression(): #регулярные выражения - поиск нужной инфы внутри текстового документа.
    # cначала с помощью рег. выражений описываем шаблон, а потом можем проверить подходитли данная строка под наш шаблон.
    r"Hello\nworld" # (raw) - сырая строка
    import re
    """ описание функций /берёт шаблон,строку / <re.Match object; span=(интервал), match="шаблон" >"""
    re.match()   # проверяет подходитли строка под данный шаблон      <span=(0, 3), match='abc'>
    re.search()  # находит первую подстроку подходящую под наш шаблон <span=(5, 8), match='abc'>
    [(m.start(0), m.end(0)) for m in re.finditer(pattern, s)] # список индексов вхождений шаблона в строку
    re.findall()  # находит все подстроки данной строки подходящей под данный щаблон ->['aac', 'abc', 'acc']
    re.sub(pattern, "ass", str,
           k)  # substitution заменить все вхождения подстрок подходящ под данный шаблон чем-то ->'ass,ass,ass'k раз

    #[] -- можно указать множество подходящих символов /[a-zA-Z]-все буквы англ алфавита/
    # , ^ $ * + ? {} [] \ () -- метасимволы
    #\d - [0-9] -- Цифры
    #\D - [^0-9] -- Не цифры
    #\s - [ \t\n\r\f\v] -- пробельные символы
    #\S - [^ \t\n\r\f\v]
    #\w - [a-zA-Z0-9] -- буквы+цифры
    #\W - [^a-zA-Z0-9]
    # . -- любой символ

    # * -- любое кол-во повторов включая 0 /"b*+" только положительное число b/
    # ? -- 0 или 1 кол-во повторов        /"b?"/
    # {k} -- указанное число повторов /{1,5} интервал/

    # + -- жадный поиск (самое длинное значение)
    # +? -- нежадный поиск(короткие значения)
    #
    # https://regex101.com/#python﻿-онлайн регулятор выражений
    #
    """
    pattern=r"\d+" # пока символ является числом склеивать :)
    r"[A-Z]{5}" делит сообщение по 5 букв 
    <a href="https://stepic.org/porn.html">1</a>   
    r'<a[^>]*?href="(.*?)"[^>]*?>' --  вытаскивает ссылку https://stepic.org/porn.html
    r'<a.*?href=".*?:\/\/((?:\w|-)+(?:\.(?:\w|-)+)+)' -- вытаскивает stepic.org       """
# ----------------------------------------------------------------------------------------------------------------------

class str():  #  работа с текстом

    """capitalize():
    Возвращает копию строки с заглавным символом только первого символа."""
    str = "это строковый пример....!!!"
    str.capitalize()
    #  Выхлоп/  Это строковый пример....!!!  /

    """Метод title()
    Возвращает копию строки , вкоторой первые символы всех слов идут с заглавной буквы."""
    str = "это пример строки....wow!!!"
    str.title()
    #  Выхлоп/  Это Пример Строки....Wow`M!!!  /
    import string
    string.capwords(str)
    #  Выхлоп/  Это Пример Строки....Wow`m!!!  /

    """Метод upper()
        Возвращает копию строки , вкоторой  символы всех слов идут с заглавной буквы."""
    str = "это пример строки....wow!!!"
    str.upper()
    # выхлоп/  ЭТО ПРИМЕР СТРОКИ....WOW!!!  /

    """Метод lower()
           Возвращает копию строки , вкоторой  символы всех слов идут с прописной буквы."""
    str = "ЭТО ПРИМЕР СТРОКИ....WOW!!!"
    str.upper()
    # выхлоп/  это пример строки....wow!!!/

    """Метод swapcase()
               Возвращает копию строки, в которой все символы, основанные на регистре, поменялись местами"""
    'Кот ОбОрмот!'.swapcase()  # кОТ оБоРМОТ!

    """Метод find() {В отличие от index не кидает ошибки}
          Возвращает индекс, первого вхождения одной строки в другую или -1"""
    "fora".find("a")
    # выхлоп/  3  /

    str.startswith("Hi")  # можем узнать начинается ли str с кортежа("Hi","hello") или другой строки   /TorF/
    str.endswith(".py")  # можем узнать заканчивается ли str кортежом(".py","png") или другой строкой /TorF/
    str.rstrip('m')  # убирает указанный символ в конце строки   str.rstrip() убирает все пробелы и /\n/ вконце строки
    str.lstrip('m')  # убирает указанный символ в начале строки mmmAss -> Ass
    str.strip('m')  # убирает указанный символ в конце и в начале строки

    """str.count(obj)  Метод count возвращает кол - во, сколько раз obj входит в str |смотри в списках| """
    str.count("a")
    # выхлоп/ 5  /

    """str.repace(a,b,k=None)  Метод replace: заменяет  a->b, k раз внутри str"""
    str.replace(",", ", ", 5)


    """ Метод re.sub ( pattern, repl, string, max=0)
    Эаменяет все вхождения ( pattern ) в ( string ) на ( repl,) """
    import re
    born = "05-03-1987 #  Дата рождения "
    #  Удалим комментарий из строки
    dob = re.sub(r'# .*$', "", born)
    print("Дата рождения:", dob)
    #  Выхлоп/ Дата рождения: 05-03-1987 /

    #  удаляет все заглавные
    f_dob = re.sub("([А-ЯЁ]+)", " ", born)
    #  Выхлоп/ ата рождения  /

    #  Удаляет все гласные буквы
    re.sub(r"[aeiouAEIOU]", '', str)

    #  Заменим дефисы на точки
    f_dob = re.sub(r'-', ".", born)
    #  Выхлоп/  #  05.03.1987 #  Дата рождения  /

    #  Поставить пробелы перед заглавными буквами
    f_dob = re.sub('([A-Z])', r" \1", born)

    """Мульти замена """
    "Swap vowels for numbers.".translate(str.maketrans('aeiou', '12345'))
    # Выхлоп/  `Sw1p v4w2ls f4r n5mb2rs.`
    "Swap abut.".translate({ord("a"):"b",  ord("b"): "a"})
    # Выхлоп/  `Swbp baut.`

    str.join(sequence)
    """Функция join() возвращает строку, в которой элементы были соединены с помощью str."""
    s = "-"
    seq = ("a", "b", "c")  # Это последовательность строк.
    print(s.join(seq))
    #  Выхлоп/  a-b-c  /

    """str.split(str=" ", num ), возвращает список всех слов в строке,
    используя str в качестве разделителя 
    разбивается на все пробелы, если не указано),
    при необходимости ограничить число разделений на num."""
    str = "this is my line..wow!!!"
    str.split()  #  Выхлоп/  ['this', 'is', 'my', 'line..wow!!!']  /
    str.split('i', 1)  #  Выхлоп/  ['th', 's is my line..wow!!!'] /
    str.split('w')     #  Выхлоп/ ['this is my line..', 'o', '!!!']  /

    """функция map принимает два аргумента:
     функцию и аргумент составного типа данных, например, список.
      map применяет к каждому элементу списка переданную функцию.
    Например, вы прочитали из файла список чисел, изначально все эти 
    числа имеют строковый тип данных, чтобы работать с ними - нужно превратить их в целое число: """
    old_list = ['1', '2', '3', '4', '5', '6', '7']
    new_list = list(map(int, old_list))
    #  Выхлоп/ [1, 2, 3, 4, 5, 6, 7] /

    eval(), """интерпретирует строку как код. 
          Если вы импортировали eval(input()) и os, человек может ввести input() os.system('rm -R *'),
          который удалит все ваши файлы в вашем домашнем каталоге"""
    eval("1+1")  # Выхлоп /2/

    [a + b + c for a, b, c in zip(one, two, three)]

# ----------------------------------------------------------------------------------------------------------------------
class list():  #  работа со списками
    obj = [], list = (), seq = [], index = []
    #  Описание методов
    a = [i for i in range(31)]
    #Выхлоп/ a=[0, 1, 2, 3, ... , 30]

    list.append(obj), """Добавляет объект obj в список (list)"""
    list1 = ['C++', 'Java', 'Python']
    list1.append('C# ')
    #  Выхлоп/ ['C++', 'Java', 'Python', 'C# ']  /

    list.insert(index, obj), """ - вставляет объект obj в список по смещению индекса"""
    list1 = ['физика', 'химия', 'математика']
    list1.insert(1, 'биология')
    #  Выхлоп/   ['физика', 'биология', 'химия', 'математика']  /

    list.extend(seq), """объединяет 2 списка / всё равно что + )"""
    list2 = ['физика', 'химия', 'математика']
    seq = [0, 1, 2, 3, 4]  #  создает список чисел от 0-4
    list1.extend(seq)
    #  Выхлоп/ ['физика', 'химия', 'математика', 0, 1, 2, 3, 4] /

    list.pop(obj), """– Удаляет и возвращает объект по индексу или последний из списка"""
    list1 = ['физика', 'биология', 'химия', 'математика']
    list1.pop(1)
    #  Выхлоп/ ['физика',  'химия', 'математика'] /

    list.remove(obj), """ – Удаляет объект obj из списка"""
    list1 = ['физика', 'биология', 'химия', 'математика']
    list1.remove('биология')

    list.reverse(), """ изменяет объекты списка на месте."""
    list1 = ['физика', 'биология', 'химия', 'математика']
    list1.reverse()
    #  Выхлоп/ ['математика', 'химия', 'биология', 'физика']/

    list.encode("utf-8") ,"""превращает строку в байты"""
    list.decode("utf-8") ,"""превращает байты B строку  """
    x=int("11001", base=2),"""переводит число меджу кодировками /x=25/"""

    list.count(obj), """Возвращает кол - во, сколько раз obj входит в список"""
    aList = ['0206', 'xyz', 'andreyex', 'abc',
'0206']
    aList.count('0206')

# ----------------------------------------------------------------------------------------------------------------------
class pyautogui():"""Библеотека автоматического питона"""

    pyautogui.moveTo(90, 300,duration = 1 ) ,""" moveTo(x,y,) /  перемещает курсор мыши в кординаты x,y  /,
                                                            / co скоростью duration  /"""

    pyautogui.click(420,100,duration=1) , """ click(x,y,), /  перемещает курсор мыши в кординаты x,y и кликает левой /
                                                        / co скоростью duration  /
                                                       /doubleClick()-2 click   / tripleClick()-3 click /"""

    pyautogui.rightClick(420,100,duration=1),  """ rightClick(x,y,) /  перемещает курсор мыши в кординаты x,y и кликает правой/,
                                                                 / co скоростью duration  /"""

    pyautogui.typewrite('Hellow word',interval=0.25) ,"""   typewrite(text) /  печатает текст  /
                                                                         / co скоростью interval  /"""

    pyautogui.press("enter") ,""" press("enter") /  нажимает 1 клавишу   /,
                                               /  pyautogui.hotkey("crtl","shift") комбиинирует 2 клавиши /"""

    pyautogui.keyDown("shift") # нажимает клавишу
    time.sleep(5)              # время задержки
    pyautogui.keyUp("shift")   # отпускат клавишу

# ----------------------------------------------------------------------------------------------------------------------
class try():  #  Как лучше всего использовать Try Except в Python
    try:
    except (TypeError,ValueError)  as e:     """ except ValueError: выводит ошибку если введён  не тот тип, TypeError"""
        print("Error! Print only INT numbers!")  ,
        print(e.args)
    except:
        continue  """перенаправляет ошибку"""

    """ Повторное возбуждение исключения"""
    try:
        ...
    except Exception  as e:
        print("У нас проблемы")
        raise

# ----------------------------------------------------------------------------------------------------------------------
class file(): # работа с файлами

    a=open("text.txt","w") , """создаёт файл text.txt"""
    a.close() # close

    open("text.txt", "rb"), """читает файл text.txt на уровне байт
                                / read1=file.read()/"""

    open("text.txt", "ab"),"""добавляет файл"""
    file.write("hello word"),"""добавляет в файл текст"""

    # w (write) - открыть для записи, содержимое файла стирается
    # a (append) - открыть для аписи, запись ведется в коней
    # b (binary) - открыть в бинарном режиме
    # r+ -  открыть для чтения и записи
    # W+  - открыть для чтения и записи, содержимое файла стирается
    file.readline(),       """читает файл построчно, но выводит текст с переносом строки / \n / """

    from linecache import getline
    getline('file.txt', 4),"""Прочитать строку с определенным номером 
                            (например, читаем четвертую строку файла, служебные символы убираются):"""

    with open('test.txt', 'r') as file,open('t.txt', 'r') as f: """читает файл text.txt и закрывает его"""
        print(file.read())

# ----------------------------------------------------------------------------------------------------------------------
class os(): # модуль os
    import os

    # описание методов

    os.path.isdir("C:\питон37"),"""Выхлоп /  True /"""
    os.path.isfile("C:\питон37"),"""Выхлоп /  False /"""
    os.listdir("C:\питон37"),"""Показывает все (даже скрытые) файлы которые есть в директории"""
    os.path.exists("name_file"),"""/ True or False /показывает существует или нет этот файл"""

    for current_dir, dirs, files in os.walk("."):""" возвращает кортеж из 3 элементов                """
         print(current_dir, dirs, files) ,     """    1 - строковое представление текущей директории   """
                                               """    2 - список из всех подпапок                      """
                                               """    3 - список всех файлов                            """

    os.path.expanduser("~") """получаем корневую директорию /home/artem/"""
    os.getcwd(), """выводит путь до текущей папки / C:\ю1\ /"""
    os.path.abspath("name_file"),"""выводит полный путь до текущей папки / C:\ю1\.name_file /"""

    os.system("C:\питон37"),"""иметация терминала  /os.system("ping google.com") -проврка интернета
                                                  /os.system("type файл") -просмотр файла"""

    os.path.getsize("файл"),"""размер файла в байтах"""

    os.path.join(dir, name),"""было (  C:\Users стало -> C:\Users\ю1\ name  )"""
    os.chdir("direktoria"),"""может меремещать по директориям БЫЛО(  C:\Users\ю1 стало -> C:\Users\ю1\ directoria  ) """

    os.path.splitext(dir)[1] ==  ,"""/.py/смотрит на расширение файла"""
    os.path.splitext(path)    ,  """ / разбивает путь на пару (root, ext), где ext начинается с точки/"""


# ----------------------------------------------------------------------------------------------------------------------
class shutil():"модуль для копировния и перемещения файлов"
    import shutil

    # Копируем src в dst. (cp src dst)
    shutil.copy("porn.json/text.txt","porn.json/result.txt") ,
    # Перемещаем  src в  dst. (mv src dst)
    shutil.move("src", "dst"),
    # Копируем дерево каталогов. (cp -R src dst)
    shutil.copytree("src", "dst", ignore = shutil.ignore_patterns('*.py'))
    """ignore_dangling_symlinks=True -- игнорирует бирый ссылки"""

# ----------------------------------------------------------------------------------------------------------------------
class tkinter():" графический модуль"
    import tkinter

    root=Tk()  ,#  создаёт окно
    root.mainloop(),#показывает окно

    root.title("Loker") ,# заголовочное название

    root.attributes("-fulscreen",True) ,# окно во весь экран

    entry = Entry(root,font=1)  ,# Поле ввода entry-text

    entry.place(width=150,height=50,x=600,y=400) ,#  кординаты и размеры поля ввода

    root.protocol("WM_DELETE_WINDOW",on_closing) ,# Не работает сочетание клавишь (альт-ф4) для закрытие программы

    root.bind('<Control-KeyPress-c>', callback)  # если нажато сочетание клавишь (ctrl-с) -> callback()

    Button(root, text="Я кнопка", width=10, heigh=4, bg="black", fg="blue")  #  / bg - цвет кнопки fg- цвет текста /

# ----------------------------------------------------------------------------------------------------------------------
class sys():
    import sys

    """ Считать все строки по одной из стандартного потока ввода"""
    for line in sys.stdin:
        line = line.strip()

    """ секундомер в терминале [динамически обновляется]"""
    for i in range(1, 4):
        a = f"\r{'.' * i}{i}"
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rtime out")

# ----------------------------------------------------------------------------------------------------------------------
class csv():# Comma-Separated Values — (значения, разделённые запятыми)
    import csv
    csv.reader(file)# делает из текста файла [таблицы], разделитель-[,]
    csv.reader(file,delimiter="-")#  разделитель--[-]

    writer = csv.writer(file)
    writer.writerows([["a"],["b"]])# делает из [таблиц] текст  , разделитель-[,]
    writer.writerows([["a"], ["b"]],quoting=csv.QUOTE_NONNUMERIC) #
    # csv.QUOTE_ALL - все значения внутрь кавычек ''
    # csv.QUOTE_NONNUMERIC - все нечисловые значения внутрь кавычек ''

# ----------------------------------------------------------------------------------------------------------------------
class xml():
    """XML(расширяемый язык разметки) / сами обозначем теги / используется для того чтобы хранить данные 
   <tag>содержимое</tag>
   также можно указывать атрибуты в открывающемся тэге 
   примечание: похоже на дерево, имеет корень """
   # плохо подходит для разбора html
    from xml.etree import ElementTree

    tree=ElementTree.parse("name_file.xml")# возвращает дерево
    root=tree.getroot() # возвращает корень дерева

    for child in root: # возвращает детей корня дерева
        print(child.tag, child.attrib)

    print(root[1][0].text) # можно выводить значения так

    for element in root.iter("scores"): # поиск значения по всему дереву
        for child in element:
            print(child.tag, child.text)

    artem=root[0]
    modul_1=next(artem.iter("module1"))
    modul_1.text="90"  # изменил значение,!!! надо перезаписать файл
    certificate=artem[2]
    certificate.set("type","cool rezultat")# добавил атрибуты

    descript=ElementTree.Element("description")# создаём тэг
    descript.text="Showed Good Skills"
    artem.append(descript) # добавляем тэг

    descript=artem.find("description")
    artem.remove(descript) # удаляет тэг

    root = ElementTree.Element('student')# создаёт корень
    name=ElementTree.SubElement(root,"name")# указываем родителя и имя тэга, создаёт тэг
    name.text="Artem"

# ----------------------------------------------------------------------------------------------------------------------
class cook():
    from collections import deque
    # создаёт arr максимальной длиной 3
    history = deque(maxlen=3)
    # [1, 2, 3] + [4] => [2, 3, 4]

    """ Сounter помогает найти количество повторений слова"""
    words = ['spam', 'egg', 'spam', 'counter', 'counter', 'counter']

    word_count = collections.Counter()
    for word in words:
        word_count[word] += 1
    # Выхлоп / word_count = Counter({'counter': 3, 'spam': 2, 'egg': 1})

    word_count = collections.Counter(words)
    print(word_count.most_common(2))
    # Выхлоп / {'counter': 3, 'spam': 2} /

    collections.Counter('abracadabra').most_common(3)
    # Выхлоп / [('a', 5), ('r', 2), ('b', 2)] /

    import heapq
    arr = [1, 2, 3, 123, 111, 234]
    print(heapq.nlargest(3, arr)) # [234, 123, 111]
    print(heapq.nsmallest(3, arr))# [1, 2, 3]

    heapq.heapify(arr) # сортировка
    print(arr[0], arr[-1])   # min и max значения
    heapq.heappush(arr, 2)   # добавление
    print(heapq.heappop(arr))# возращает min элемент, удаляет его

    heapq.heappush(queue, (priotiry, index, item))# добавление в очередь с приоритетом
    index += 1
    heapq.heappop(queue)[-1]# менее приоритетное

    """Найти max|min значение в словаре"""
    d = {"a": 30, "c": 1, }
    min(d, key=lambda k: d[k])
    max(zip(d.values(), d.keys())) #(30, 'a')

    """Отсортировать словарь по значениям"""
    d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
    sorted(d.items(), key=lambda item: item[1])
    # Выхлоп / [('one', 1), ('two', 2), ('three', 3)]/

    """Отсортировать список словарей по значению словаря  >see itemgetter<"""
    list_to_be_sorted = [{'name': 'Homer', 'age': 39}, {'name': 'Bart', 'age': 10}]
    sorted(list_to_be_sorted, key=lambda k: k['name'])#             по 1 ключу
    sorted(list_to_be_sorted, key=lambda k: (k['name'], k['age']))# по 2 ключам
    # Выхлоп / [{'name': 'Bart', 'age': 10}, {'name': 'Homer', 'age': 39}]/

    """Группировка по значению конкретного поля"""
    import collections
    data = [{'n': 'Artem', 'a': 39}, {'n': 'bard', 'a': 10},
            {'n': 'max', 'a': 39}, {'n': 'nata', 'a': 10}]
    group_by_age = collections.defaultdict(list)
    for row in data:
        group_by_age[row["a"]].append(row)
    #{39: [{'n': 'Artem', 'a': 39}, {'n': 'max', 'a': 39}],
    # 10: [{'n': 'bard', 'a': 10}, {'n': 'nata', 'a': 10}]}

    """Найти общие ключи|значения в словарях"""
    d1 = {"AAA": 30, "ZZZ": 30, }
    d2 = {"AAA": 31, "ZZZ": 30, }
    d1.keys() & d2.keys()  # {'AAA', 'ZZZ'} общие ключи
    d1.keys() - d2.keys()  # set() ключи 1 словаря без ключей 2
    d1.items() & d2.items()# {('ZZZ', 30)} общие пары

    """ Создание нового словаря из старого без ключей "ZZZ", "XXX" """
    new_d = {key: d[key] for key in d.keys() - {"ZZZ", "XXX"}}

    """ Вернуть все возможные перестановки массива """
    import itertools
    arr = [1, 2, 3]
    pr = [i for i in itertools.permutations(arr, 2)]

    """ Пройтись по диретрориям и найти файл """
    def findFile(start, name):
        for r, d, files in os.walk(start):
            if name in files:f_p = os.path.join(start, r, name);print(os.path.abspath(f_p))
    findFile("/", 'index.html'),

    """ Запустить debug"""
    import pdb
    i = 6
    pdb.set_trace() # Можно ввести `i` --> 6

# ----------------------------------------------------------------------------------------------------------------------










