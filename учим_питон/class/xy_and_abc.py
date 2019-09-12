from math import sqrt

try:
    a = int(input("write a->"))
    b = int(input("write b->"))
    c = int(input("write c->"))
except ValueError:  # except ValueError: выводит ошибку если введён  не тот тип
    print("Error! Print only INT numbers!")

# дискриминант
D = b ** 2 - 4 * a * c

# 1 version
if D > 0:
    x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print("x1= " + str(x1) + " \n x2= " + str(x2))

# 2 version
if D == 0:
    x = -b / (2 * a)
    print(str(x))

# 3 version
if D < 0:
    print("Not x!")
