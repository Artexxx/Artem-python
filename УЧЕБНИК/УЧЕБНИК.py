# -*- coding: utf-8 -*-
#  1 -> class str():  #  работа с текстом
#  2 -> class list():  #  работа со списками
#  3 -> class pyautogui():"""Библеотека автоматического питона"""
#  4 -> class try():  #  Как лучше всего использовать Try Except в Python
#  5 -> class file(): # работа с файлами
#  6 -> class os(): # модуль os
#  7 -> class shutil():"модуль для копировния и перемещения файлов"
#  8 -> class tkinter():" графический модуль"

#  -------------------------------------------------------------------------------------------

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
    #  Выхлоп/  Это Пример Строки....Wow!!!  /

    """Метод upper()
        Возвращает копию строки , вкоторой  символы всех слов идут с заглавной буквы."""
    str = "это пример строки....wow!!!"
    str.upper()
    # выхлоп/  ЭТО ПРИМЕР СТРОКИ....WOW!!!  /


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
    print(f_dob)
    #  Выхлоп/ ата рождения  /

    #  Заменим дефисы на точки
    f_dob = re.sub(r'-', ".", born)
    print(f_dob)
    #  Выхлоп/  #  05.03.1987 #  Дата рождения  /

    str.join(sequence)"""Функция join() возвращает строку, в которой элементы были соединены с помощью str."""
    s = "-"
    seq = ("a", "b", "c")  # Это последовательность строк.
    print(s.join(seq))
    #  Выхлоп/  a-b-c  /

    """str.split(str=" ", num ), возвращает список всех слов в строке,
    используя str в качестве разделителя 
    разбивается на все пробелы, если не указано),
    при необходимости ограничить число разделений на num."""
    str = "this is my line..wow!!!"
    str.split()  #  Выхлоп/  'this', 'is', 'my', 'line..wow!!!']  /
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

#  -------------------------------------------------------------------------------------------
class list():  #  работа со списками
    obj = [], list = (), seq = [], index = []
    #  Описание методов

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

    list.count(obj), """Возвращает кол - во, сколько раз obj входит в список"""
    aList = ['0206', 'xyz', 'andreyex', 'abc', '0206']
    aList.count('0206')

#  -------------------------------------------------------------------------------------------
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

#  -------------------------------------------------------------------------------------------
class try():  #  Как лучше всего использовать Try Except в Python

    except ValueError: """ except ValueError: выводит ошибку если введён  не тот тип"""
        print("Error! Print only INT numbers!")

    except:continue """перенаправляет ошибку"""



#  -------------------------------------------------------------------------------------------
class file(): # работа с файлами

    a=open("text.txt","w") , """создаёт файл text.txt"""
    a.close() # close

    open("text.txt", "rb"), """читает файл text.txt на уровне байт"""

    open("text.txt", "ab"),"""добавляет файл"""

    file.write("hello word"),"""добавляет в файл текст"""
#  -------------------------------------------------------------------------------------------
class os(): # модуль os
    import os

    # описание методов

    os.path.isdir("C:\питон37"),"""Выхлоп / True  /"""

    os.path.isfile("C:\питон37"),"""Выхлоп /  False /"""

    os.listdir("C:\питон37"),"""Показывает все (даже скрытые) файлы которые есть в директории"""

    os.system("C:\питон37"),"""иметация терминала  /os.system("ping google.com") -проврка интернета
                                                  /os.system("type файл") -просмотр файла"""

    os.path.getsize("файл"),"""размер файла в байтах"""

    os.path.join(dir, name),"""было (  C:\Users стало -> C:\Users\ю1\ name  )"""

    os.path.splitext(dir)[1] == ".py" ,"""смотрит на расширение файла"""


#  -------------------------------------------------------------------------------------------
class shutil():"модуль для копировния и перемещения файлов"
    import shutil

    shutil.copy("", "C:\ Users"), """  перемещает файл  """
    shutil.move("", "C:\ Users"), """  перемещает файл  """


#  -------------------------------------------------------------------------------------------
class tkinter():" графический модуль"
    import tkinter

    root=Tk()  ,#  создаёт окно

    root.title("Loker") ,# заголовочное название

    root.attributes("-fulscreen",True) ,# окно во весь экран

    entry = Entry(root,font=1)  ,# Поле ввода
    entry.place(width=150,height=50,x=600,y=400) ,#  кординаты и размеры поля ввода

    root.protocol("WM_DELETE_WINDOW",on_closing) ,# Не работает сочетание клавишь (альт-ф4) для закрытие программы

    Button(root, text="Я кнопка", width=10, heigh=4, bg="black", fg="blue")  #  / bg - цвет кнопки fg- цвет текста /

#  -------------------------------------------------------------------------------------------







