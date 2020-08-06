#добавляет один файл в другой на уровне байт

# read file 1 --------------------------------------------
try:
    nameFile=input("Name file 1:")
    with open (nameFile,'rb') as file1:
        read1=file1.read()
except:
    print("Error,file 1 not found")
    raise SystemExit

# read file 2 ----------------------------------------------
try:
    nameFile=input("Name file 2:")
    with open (nameFile,'rb') as file2:
        read2=file2.read()
except:
    print("Error,file 2 not found")
    raise SystemExit

# overwrite file2 / file2 = file1 + file2 /------------------
with open (nameFile,'wb') as file3:
    file3.write(read1)
    file3.write(read2)
    print("File "+nameFile+" overwriten :)")


