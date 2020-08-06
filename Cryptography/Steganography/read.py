"""#считает байты в файле и выводит код файла
try:
    namefile=input("File name:")
    with open(namefile,'rb') as r:
        byte = r.read(1)#  прочитался 1 байт
        k=0 #счётчик байтов
        while byte:
            byte = r.read(1)
            print(byte)
            k+=1
except FileNotFoundError:
    print("\n[x] File:"+str(namefile+"is not defined"))
    raise SystemExit
else:
    print( "\n[+] Number of bytes in "+str(namefile)+" :"+str(k))
   """

#считает байты в файле и выводит код декодированного файла
try:

    namefile = input("File name:")
    with open(namefile, 'rb') as r:
        byte = r.read(1)  # прочитался 1 байт
        k = 0
        while byte:
            try:  # try перенаправляет ошибку если не получается декодировать байт
                byte = r.read(1).decode("utf-8")
            except:
                continue
            print(byte, end='')
            k+=1                                           #images.jpg
except FileNotFoundError:
    print("\n[x] File:" + str(namefile + "is not defined"))
    raise SystemExit
else:
    print("\n[+] Number of bytes in " + str(namefile) + " :" + str(k))

