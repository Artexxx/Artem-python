"""
Единственная строка входных данных содержит название экспоната
— строку, состоящую из не менее, чем одного, и не более, чем ста символов.
 Гарантируется, что строка состоит из строчных букв английского алфавита.
Выходные данные
Выведите единственное целое число —
 минимальное количество поворотов колеса, за которое Гриша сможет напечатать название экспоната.
 """
# chr() - Функция преобразующая число в символ по ASCII таблице
# ord() - Функция преобразующая символ в число по ASCII таблице

# sumvol # что ищем
# bykva  # откуда ищем

key = 0
kolvo = 0 # счётчик сдвигов
slovo = input('slovo').upper()


def find_min_key(bykva, sumvol):
    global key, kolvo
    if (ord(sumvol) - ord(bykva)) % 26 < (ord(bykva) - ord(sumvol)) % 26:

        key = (ord(sumvol) - ord(bykva)) % 26  # если число лежит в правой части .баробан в право крутим


    else:
        key = (ord(bykva) - ord(sumvol)) % 26  # если число лежит в левой части . баробан в лево крутим

    kolvo += key
    return (key)



and_sumvol = "A"
for bykv in slovo:
    print(find_min_key(bykva=bykv, sumvol=and_sumvol))
    and_sumvol = bykv
print('kolvo='+str(kolvo))
