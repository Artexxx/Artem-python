""" Пребор паролей для закодированного архива возможность --
    указать несколько словарей
    zip -P password arch.zip main.py
"""
import sys
from zipfile import ZipFile
from os import mkdir
from threading import Thread
from colorama import init, Fore; init(autoreset=True)

raw_banner = '''
    ░░███████╗░██╗░██████╗░░░██╗░░██╗░░█████╗░░░█████╗░░██╗░░██╗░
    ░░╚════██║░██║░██╔══██╗░░██║░░██║░██╔══██╗░██╔══██╗░██║░██╔╝░
    ░░░░███╔═╝░██║░██████╔╝░░███████║░███████║░██║░░╚═╝░█████═╝░░
    ░░██╔══╝░░░██║░██╔═══╝░░░██╔══██║░██╔══██║░██║░░██╗░██╔═██╗░░
    ░░███████╗░██║░██║░░░░░░░██║░░██║░██║░░██║░╚█████╔╝░██║░╚██╗░
    ░░╚══════╝░╚═╝░╚═╝░░░░░░░╚═╝░░╚═╝░╚═╝░░╚═╝░░╚════╝░░╚═╝░░╚═╝░
    '''
# color to banner
banner = ""
for i in raw_banner:
    if i not in "\n █░":
        banner += f"{Fore.BLUE}{i}\u001b[0m"
    elif i == "░":
        banner += f"{Fore.CYAN}{i}\u001b[0m"
    elif i == "█":
        banner += f"\u001b[41m{i}\u001b[0m"
    else:
        banner += i
print(banner)


def generator(string, archive):
    for word in string:
        passwd = word.rstrip("\n")
        archive.setpassword(passwd.encode())
        try:
            archive.extractall(directory)
        except:
            yield "[False]: " + passwd
        else:
            print("\u001b[32m[True]: \u001b[0m" + passwd)
            sys.exit(1)


def findPasword(dictionari):
    global archive
    with open(dictionari, errors='ignore') as dictionary:
        with ZipFile(archive) as archive:
            for password in generator(dictionary, archive):
                print(password)


directory = "ExtractArchive"
try:
    mkdir(directory)
except FileExistsError:
    pass

archive = input("Введите название архива который будет расшифрован")

N = input("Кольчество словарей")
THREAD = []
for i in range(int(N)):
    dict_name = input(f"Введите название {i + 1} словаря:")
    THREAD.append(Thread(target=findPasword, args=(dict_name,)))

# Запуск многопоточного перебора паролей
for thread in THREAD:
    thread.start()
