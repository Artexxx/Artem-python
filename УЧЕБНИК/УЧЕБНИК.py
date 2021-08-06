# -*- coding: utf-8 -*-
#  0 -> class regular
#  1 -> class str()
#  2 -> class list():
#  3 -> class set&dict():
#  4 -> class pyautogui():
#  5 -> class try():
#  6 -> class file():
#  7 -> class os():
#  8 -> class shutil():
#  9 -> class tkinter():
#  10 -> class sys():
#  11 -> class recept():

"""Есть по крайней мере два способа создать кортеж из одного элемента."""
t = tuple([1])
t = (1,)
t = 1, # можно и без скобок
# Выхлоп /  type(x) -> tuple /

# ----------------------------------------------------------------------------------------------------------------------
class extraHacks(): # Экстра-фишки 3.7+
    1E6 = 100_000_000 # сокращенная зипись числа
    bit = 2; bit <<= 9 # сдвиг на 9 битов влево (10 ~> 10_000_000_000)
    bit = 32; bit >>= 2 # сдвиг на 2 бита вправо (удаление справа 2 битов) (32 ~> 16 ~> 8)
    bit |= 0b10 # операция ИЛИ -  если справа есть пустые биты (0), то они заменяются (1) (1_000 ~> 1_010)
    bit >> bit.bit_length()-2 & 0b11

    from dataclasses import dataclass
    @dataclass # (frozen=True) запрет на изменение полей
    class Edge: # создаёт автоматически метод  __init__(), который создайт экземпляры
        u: int  # >>> print(Edge('NodeA', 'NodeB'))
        v: int  # NodeA -> NodeB
        def __str__(self): return f"{self.u} -> {self.v}"

    old = {**dict1, **dict1} # раньше объединение двух словарей в один новый словарь
    new = dict1 | dict2 # сейчас то же самое можно сделать так (python 3.9)

    import pdb; pdb.set_trace() # раньше отладка делалась так
    breakpoint() # сейчас то же самое можно сделать так (python 3.7)

    # Присваивающее выражение: Новый оператор `:=` позволяет присваивать значения переменным внутри выражений (python 3.8)
    if (n := len(list_)) > 10:
        print(f"List is too long ({n} elements, expected <= 10)")

    # Поддержка f-строками `=` для самодокументирующих выражений и отладки (python 3.8)
    print(f'List is too long  {n=}')
    # Выхлоп / "List is too long n=10"

    # Positional-only аргументы (python 3.8)
    # Тае можно указать, какие параметры функций можно передавать через синтаксис именованных аргументов, а какие нет.

    def f(a, b, /, c, d, *, e, f): print("Positional-only parameters", a, b, c, d, e, f)
    f(10, 20, 30, d=40, e=50, f=60)     # OK
    f(10, b=20, c=30, d=40, e=50, f=60) # ошибка, `b` не может быть именованным аргументом
    f(10, 20, 30, 40, 50, f=60)         # ошибка, `e` обязан быть именованным аргументом

# ----------------------------------------------------------------------------------------------------------------------
class format():  #  форматирование - подстановка значения в общий шаблон
    """Метод string.safe_substitute() {Вместо вызова исключения перехватывает его и оставляет в тексте само выражение переменной.}"""
    template = string.Template("a = $b + $c")
    template.safe_substitute({'b': 123, 'C': 21})
    # Выхлоп / a = 123 + $c /

    """Метод format подставляет те значения которые мы передали аргументами на то место где фигурные скобки"""
    template = "{m} and {a}" # создание шаблона
    template.format(a="cat", m="dog")  # можем передавать пустые переменные
    # Выхлоп / cat and dog /

    "{:.3}".format(0.3141932) # округляет до 3х знаков после запятой
    # Выхлоп / 0.314 /
    '{:,}'.format(1234)
    #  Выхлоп / 1,234/
    "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
    #  Выхлоп / int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010/

# ----------------------------------------------------------------------------------------------------------------------
class textwrap():  # использоватся требуется красиво оформленный вывод
    import textwrap
    """Метод dedent удаляет общий пробельный префикс из всех строк и приводит к лучшему результату"""
    dedented_text = textwrap.dedent(raw_text)

    """Метод fill изменяет ширину области вывода, добавляет префикс"""
    print(textwrap.fill(dedented_text, initial_indent='', subsequent_indent=' ' * 4, width=50)) # Создаём висячие отступы

    """Метод indent управляет префиксом, его получат те строки, для которых should_indent вернет истинное значение."""
    should_indent = lambda line: len(line.strip()) % 2 == 0
    wrapped = textwrap.fill(dedented_text, width=50)
    final = textwrap.indent(wrapped, 'EVEN', predicate=should_indent)

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
    re.sub(pattern, "ass", str, k)  # substitution заменить все вхождения подстрок подходящих под данный шаблон чем-то ->'ass,ass,ass'k раз

    """ Метод re.sub ( pattern, repl, string, max=0)
    Эаменяет все вхождения ( pattern ) в ( string ) на ( repl,)"""
    born = "05-03-1987 #  Дата рождения "
    #  Удалим комментарий из строки
    dob = re.sub(r'# .*$', "", born)
    print("Дата рождения:", dob)
    #  Выхлоп/ Дата рождения: 05-03-1987 /

    #  удаляет все заглавные
    re.sub("([А-ЯЁ]+)", " ", born)
    #  Выхлоп/ ата рождения  /

    #  Удаляет все гласные буквы
    re.sub(r"[aeiouAEIOU]", '', str)

    #  Заменим дефисы на точки
    re.sub(r'-', ".", born)
    #  Выхлоп/  #  05.03.1987 #  Дата рождения  /

    #  Поставить пробелы перед заглавными буквами
    re.sub('([A-Z])', r" \1", born)


     []   # (класс символов) Находить любые символы заключенные в квадратных скобках /[a-zA-Z]-все буквы англ алфавита/
    [^ ]  # (отрицание класа символов). Находить, любые символы не заключенные в квадратных скобках
    (xyz) # (группа символов) Находить только символы xyz в указанном порядке

    | # (чередование) Находить либо буквы до, либо буквы после символа
    ^ # находить совпадения только в том случае, если шаблон будет в конце строки  / ^(H|h)ello /
    $ # находить совпадения только в том случае, если шаблон будет в конце строки / goodbye(\.)$ /
    * # любое кол-во повторов включая 0 /"b+" только положительное число b/
    ? # 0 или 1 кол-во повторов        /"b?"/
    {k} # указанное число повторов /{1,5} интервал/
    ab *  # a, за которым следует ноль или более b
    ab +  # a, за которым следует одна или более b
    ab?   # a, за которым следует ноль или одна b

     . # любой отдельной символ, кроме разрыва строки
    \d # [0-9] -- Цифры
    \D # [^0-9] -- Не цифры
    \s # [ \t\n\r\f\v] -- пробельные символы
    \S # [^ \t\n\r\f\v]
    \w # [a-zA-Z0-9] -- буквы+цифры
    \W # [^a-zA-Z0-9]

    # +  - (жадный поиск) самое длинное значение
    # +? - (нежадный поиск) короткие значения

    (?=...) """Положительное опережающее условие (Lookahead)
    [?] [?] Находит все совпадения, за которыми следует определенный шаблон"""
    # (T|t)he(?=\sfat) => The fat cat sat on the mat.
    #  Выхлоп/ The / перед fat

    (?!...) """Отрицательное  опережающее условие
    [?] Находит все совпадения, за которыми НЕ следует определенный шаблон"""
    # (T|t)he(?!\sfat) => The fat cat sat on the mat.
    #  Выхлоп/ the / перед mat

    (?<=...) """Положительное ретроспективное условие (Lookbehind)
    [?] Находит все совпадения, которым предшествует определенный шаблон"""
    # (?<=(T|t)he\s)(fat|mat) >= The fat cat sat on the mat.
    #  Выхлоп/ fat mat / после The и the

    (?<!...) """Отрицательное  ретроспективное условие
    [?] Находит все совпадения, которым НЕ предшествует определенный шаблон"""
    # (?<!(T|t)he\s)(cat) >= The fat cat sat on the mat.
    #  Выхлоп/ fat mat / после The и the

    i # (insensitive) Поиск без учета регистра
    g #	Глобальный поиск: поиск шаблона во всем входном тексте
    m # Мультистроковый поиск: Якоря применяются к каждой строке.

    #     The =V=> The fat cat sat on the mat =  Выхлоп/  The /
    # /The/gi =S=> The fat cat sat on the mat =  Выхлоп/ The the /

    # /.at(.)?$/   =V=> The fat\n cat sat\n on the mat =  Выхлоп/  mat /
    # /.at(.)?$/gm =S=> The fat\n cat sat\n on the mat =  Выхлоп/ fat sat mat /

    address = re.compile("""
        # Имя состоит из букв и может включать символы точки "."
        # в сокращенных вариантах обращения и инициалах
        ((?P<name>
            ([\w.,]+\s+)*[\w.,]+)
            \s*
            # Адреса электронной почты заключаются в угловые скобки
            # < >, но только если найдено имя, поэтому открывающая
            # угловая скобка включена в эту группу
            <
        )? # Полное имя является необязательным элементом
        # Собственно электронный адрес: username@domain.tld
        (?P<email>
            [\w\d.+-]+ # Имя пользователя
            @
            ([\w\d.]+\.)+ # Префикс имени домена
            (com|org|edu) # Ограничение списка доменов верхнего уровня
        )
        >? # Необязательная закрывающая угловая скобка
    """, re.VERBOSE)
    address.search(' First M. Last <first.last@example.com>')
    # Выхлоп / Name : First M. Last
    #          Email: first.last@example.com /

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
    str_ = "это строковый пример....!!!"
    str_.capitalize()
    #  Выхлоп/  Это строковый пример....!!!  /

    """Метод title()
    Возвращает копию строки , вкоторой первые символы всех слов идут с заглавной буквы."""
    str_ = "это пример строки....wow!!!"
    str_.title()
    #  Выхлоп/  Это Пример Строки....Wow`M!!!  /
    import string
    string.capwords(str_)
    #  Выхлоп/  Это Пример Строки....Wow`m!!!  /

    """Метод title()
        Дополняет указанную строку нулями слева до указанной минимальной длины."""
    str(12).zfill(7)
    #  Выхлоп/  '001'  /

    """Метод swapcase()
    Возвращает копию строки, в которой все символы, основанные на регистре, поменялись местами"""
    'Кот ОбОрмот!'.swapcase()  # кОТ оБоРМОТ!

    """Метод find() {В отличие от index() не кидает ошибки}
    Возвращает индекс, первого вхождения одной строки в другую или -1"""
    "fora".find("a")
    # Выхлоп/  3  /

    str_.startswith("Hi")  # можем узнать начинается ли str с кортежа("Hi","hello") или другой строки   /TorF/
    str_.endswith(".py")  # можем узнать заканчивается ли str кортежом(".py","png") или другой строкой /TorF/
    str_.rstrip('m')  # убирает указанный символ в конце строки   str.rstrip() убирает все пробелы и /\n/ вконце строки
    str_.lstrip('m')  # убирает указанный символ в начале строки mmmAss -> Ass
    str_.strip('m')  # убирает указанный символ в конце и в начале строки

    """str.repace(a,b,k=None)  Метод replace: заменяет  a->b, k раз внутри str"""
    str_.replace(",", ", ", 5)

    #  Мульти замена
    "Swap vowels for numbers.".translate(str.maketrans('aeiou', '12345'))
    # Выхлоп/  `Sw1p v4w2ls f4r n5mb2rs.`
    "Swap abut.".translate({ord("a"): "b", ord("b"): "a"})
    # Выхлоп/  `Swbp baut.`

    """str.split(str=" ", num), возвращает список всех слов в строке, используя str в качестве разделителя 
           разбивается на все пробелы, если не указано), при необходимости ограничить число разделений на num."""
    str_ = "this is my line..wow!!!"
    str_.split()  #  Выхлоп/  ['this', 'is', 'my', 'line..wow!!!']  /
    str_.split('i', 1)  #  Выхлоп/  ['th', 's is my line..wow!!!'] /
    str_.split('w')     #  Выхлоп/ ['this is my line..', 'o', '!!!']  /

    """eval() интерпретирует строку как код. 
          Если вы импортировали eval(input()) и os, человек может ввести os.system('rm -R *'),
          который удалит все ваши файлы в вашем домашнем каталоге"""
    eval("1+1")  # Выхлоп /2/


# ----------------------------------------------------------------------------------------------------------------------
class list():
    obj = [], list = (), seq = [], index = []
    a = [i for i in range(31)]
    # Выхлоп/ a = [0, 1, 2, 3, ... , 30]

    list.insert(index, obj), """ Вставляет объект obj в список по смещению индекса"""
    list_ = ['физика', 'химия', 'математика']
    list_.insert(1, 'биология')
    #  Выхлоп/   ['физика', 'биология', 'химия', 'математика']  /

    list.extend(seq), """ Объединяет 2 списка / всё равно что + )"""
    list_ = ['физика', 'химия', 'математика']
    list_.extend([0, 1, 2, 3, 4])
    #  Выхлоп/ ['физика', 'химия', 'математика', 0, 1, 2, 3, 4] /

    list.pop(obj), """ Удаляет и возвращает объект по индексу или последний из списка"""
    list_ = ['физика', 'биология', 'химия', 'математика']
    list_.pop(1)
    #  Выхлоп/ ['физика',  'химия', 'математика'] /

    list.remove(obj), """ Удаляет объект obj из списка"""
    list_ = ['физика', 'биология', 'химия', 'математика']
    list_.remove('биология')

    list.reverse(), """ Изменяет объекты списка на месте."""
    list_ = ['физика', 'биология', 'химия', 'математика']
    list_.reverse()
    #  Выхлоп/ ['математика', 'химия', 'биология', 'физика']/

# ----------------------------------------------------------------------------------------------------------------------
class set_dict():
    """ Порядок ключей в словарях теперь гарантированно совпадает с порядком их вставки, это добавлено в спецификацию. (python 3.7)"""

    """ Объединение двух словарей в один новый словарь """
    d1 = {"AAA": 30, "ZZZ": 30, }
    d2 = {"AAA": 31, "ZZZ": 30, }
    # (!) при пересечение ключей берётся значение из последнего словаря
    dict_ = {**d1, **d2} #=> {'AAA': 31, 'ZZZ': 30}

    """Найти общие ключи|значения в словарях"""
    d1.keys() & d2.keys()  #=>  {'AAA', 'ZZZ'} общие ключи
    d1.keys() - d2.keys()  #=>  set() ключи 1 словаря без ключей 2
    d1.items() & d2.items()  #=>  {('ZZZ', 30)} общие пары

    """ update() обновляет/дополняет словарь <смотри collections.ChainMap>,
     перезаписывая существующие ключи новыми значениями. Если ключ в словаре отсутствует, то он добавляется."""
    d1.update({"ZZZ": 31}) # {'AAA': 30, 'ZZZ': 0}
    d1.update([('BBB', 30), ('CCC', 30)]) # {'AAA': 30, 'ZZZ': 0, 'BBB': 30, 'CCC': 30}

    """ Создание нового словаря из старого без ключей "ZZZ", "XXX" """
    dict_ = {key: dict_[key] for key in dict_.keys() - {"ZZZ", "XXX"}}

    """ Найти max|min значение в словаре"""
    dict_ = {"key1": 30, "key2": 20, "key3": 10, }
    min(dict_, key=lambda key: dict_[key]) #=> 'key3'
    max(zip(dict_.values(), dict_.keys())) #=> (30, 'key1')

    """ Отсортировать словарь по значениям """
    sorted(dict_.items(), key=lambda item: item[1])
    # Выхлоп / [('key3', 10), ('key2', 20), ('key1', 30)]/

    """Отсортировать список словарей по значению словаря  >смотри itemgetter<"""
    list_to_be_sorted = [{'name': 'Homer', 'age': 39}, {'name': 'Bart', 'age': 10}]
    sorted(list_to_be_sorted, key=lambda k: k['name'])#             по 1 ключу
    sorted(list_to_be_sorted, key=lambda k: (k['name'], k['age']))# по 2 ключам
    # Выхлоп / [{'name': 'Bart', 'age': 10}, {'name': 'Homer', 'age': 39}]/

    import collections
    """defaultdict() - подкласс словаря
    Попытка доступа к отсутствующему ключу его создаёт и инициализирует,
     используя принятую по умолчанию фабрику, то есть в данном примере list()"""
    dd = collections.defaultdict(list)
    dd['colors'] += ['red', 'green', 'blue']
    # Выхлоп / defaultdict(list, {'colors': ['red', 'green', 'blue']})/


# ----------------------------------------------------------------------------------------------------------------------
class pyautogui():
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
class TryExcept():
    try:  ...
    except (TypeError,ValueError)  as e:  """ except ValueError: выводит ошибку если введён  не тот тип, TypeError"""
        print("Error! Print only INT numbers!")  ,
        print(e.args)
    except: continue  # Перенаправляет (игнорирует) ошибку
    finally: ... # Выполнится всегда
    else: ... # Выполнится если ошибки не произошло


    """ Повторное возбуждение исключения"""
    try: ...
    except Exception  as e:
        print("У нас проблемы")
        raise

# ----------------------------------------------------------------------------------------------------------------------
class file(): # Работа с файлами

    a=open("text.txt","w") , """создаёт файл text.txt"""
    a.close()

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
class os():
    import os
    os.path.isdir(r"C:\Users"), """Выхлоп /  True /"""
    os.path.isfile(r"C:\Users"),"""Выхлоп /  False /"""
    os.listdir(r"C:\Users"),"""Показывает все (даже скрытые) файлы которые есть в директории"""
    os.path.exists("test.txt"),"""/ True or False /Показывает уществует ли путь до файла или папки"""

    for current_dir, dirs, files in os.walk("."):""" возвращает кортеж из 3 элементов                """
         print(current_dir, dirs, files) ,     """    1 - строковое представление текущей директории """
                                               """    2 - список из всех подпапок                    """
                                               """    3 - список всех файлов                         """

    os.path.expanduser("~") """Возвращает корневую директорию C:/Users/admin"""
    os.getcwd(), """Выводит путь до текущей папки / C:/Users/admin/Desktop /"""
    os.path.abspath("your_text"),"""Тоже самое, что os.getcwd() + '/your_text' -> C:/Users/admin/Desktop/your_text"""

    os.system("C:\питон37"),"""Имитация терминала  /os.system("ping google.com")
                                                  /os.system("type test.txt") - просмотр файла"""

    os.path.getsize("test.txt"),"""Размер файла в байтах"""

    os.path.join(r'C:\Users', 'admin'),"""(  C:/Users стало -> C:/Users/admin  )"""
    os.chdir("direktoria"), """Может перемещать по директориям БЫЛО(  C:/Users/admin стало -> C:/Users/admin/directoria  ) """

    os.path.splitext(r'C:\Users\admin\file.cp') """ / Разбивает путь на пару (root, ext), где ext начинается с точки /( C:/Users/admin/file', '.py')"""

# ----------------------------------------------------------------------------------------------------------------------
class shutil(): "Модуль для копировния и перемещения файлов"
    import shutil

    # Копируем src в dst. (cp src dst)
    shutil.copy("porn.json/text.txt","porn.json/result.txt") ,
    # Перемещаем  src в  dst. (mv src dst)
    shutil.move("src", "dst"),
    # Копируем дерево каталогов. (cp -R src dst)
    shutil.copytree("src", "dst", ignore = shutil.ignore_patterns('*.py'))
    """ignore_dangling_symlinks=True -- игнорирует бирый ссылки"""

# ----------------------------------------------------------------------------------------------------------------------
class tkinter():  "Графический модуль"
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

    """ Секундомер в терминале [динамически обновляется]"""
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
    from xml.etree import ElementTree

    tree=ElementTree.parse("name_file.xml") # возвращает дерево
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

    """ Использование ChainMap + argparse. <смотри dict.update()> ChainMap() группирует несколько словарей"""
    from collections import ChainMap
    defaults = {'ip': 'localhost', 'port': 7777}
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ip')
    parser.add_argument('-p', '--port')

    args = parser.parse_args() # Возвращает Namespace(ip=None, port=None)
    new_dict = {key: value for key, value in vars(args).items() if value} # vars() возвращает словарь пространства имен объекта
    # Поиск ключей в ChainMap() происходит последовательно, слева на право, во всех добавленных словарях, пока не будет найден соответствующий ключ
    settings = ChainMap(new_dict, defaults)

    from itertools import accumulate
    list(accumulate(['i', 'have','no','space']))
    # Выхлоп / ['i', 'ihave', 'ihaveno', 'ihavenospace'] /

    """ Сounter помогает найти количество повторений"""
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
    print(heapq.heappop(arr))# Возвращает min элемент, удаляет его

    heapq.heappush(queue, (priotiry, index, item))# добавление в очередь с приоритетом
    index += 1
    heapq.heappop(queue)[-1]# менее приоритетное

    """Группировка по значению конкретного поля"""
    import collections
    data = [{'n': 'Artem', 'a': 39}, {'n': 'bard', 'a': 10},
            {'n': 'homer', 'a': 39}, {'n': 'nata', 'a': 10}]
    group_by_age = collections.defaultdict(list)
    for row in data:
        group_by_age[row["a"]].append(row)
    # {39: [{'n': 'Artem', 'a': 39}, {'n': 'homer', 'a': 39}],
    #  10: [{'n': 'bard',  'a': 10},  {'n': 'nata',  'a': 10}]}

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
