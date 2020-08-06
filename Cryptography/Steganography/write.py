# добавляет в код файла текст
try:
    namefile=input("File name:")                #images.jpg
    with open(namefile,'ab') as file:
        text=input("Write text: ")
        file.write(text.encode("utf-8"))
except FileNotFoundError:
    print("[x] File:"+str(namefile+"is not defined"))
    raise SystemExit
else:
    print("[+] File:"+str(namefile)+" gotov")
