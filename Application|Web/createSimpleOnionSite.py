"""
 Запускайте программу под root пользователем
 $ sudo python3 main.py

 Директория с файлами [ index.html ]:
     /var/www/onion

 Директория с файлами [ private_key, hostname ]:
    /var/lib/tor/onion/

"""
from os import system, listdir, mkdir, chdir, getcwd
from time import sleep

"""
# Раскомментировать, если пакет 'tor' не установлен
dist = ["apt-get install", "pacman -S"]
prog = ["tor"]
for i in dist:
    for j in prog:
        system("{dist} {prog}".format(dist=i, prog=j))
"""

# Директории со страницами сайта
www = [False, "/var/www/"]
onion = [False, "/var/www/onion/"]

# Директория с основными файлами сайта
main_files = "/var/lib/tor/onion/"

# Файлы связанные с сайтом
html_file = [False, "/var/www/onion/index.html"]
host_file = "/var/lib/tor/onion/hostname"
key_file = "/var/lib/tor/onion/private_key"

# Файл со всей информацией
readme = [False, "README.txt"]

# Конфигурационный файл тора и строки для настройки конфигурации файла torrc
torrc = [False, "/etc/tor/torrc"]
string1 = "HiddenServiceDir /var/lib/tor/onion"
string2 = "HiddenServicePort 80 127.0.0.1:80"

# Проверка существования /var/`www`/
if "www" in listdir("/var/"):
    www[0] = True
elif www[0] == False:
    mkdir(www[1])
    print(f"Directory '{www[1]}' created")

# проверить существование /var/www/onion
if "onion" in listdir(www[1]):
    onion[0] = True
#  создание /var/www/`onion`/
elif onion[0] == False:
    mkdir(onion[1])
    print(f"Directory '{onion[1]}' created")

# Проверка на наличие html файла  в /var/www/onion
if "index.html" in listdir(onion[1]):
    html_file[0] = True
# Создание html файла
elif html_file[0] == False:
    with open(html_file[1], "w") as html:
        html.write('''
<!DOCTYPE html>
<html>
	<head>
		<title>Hiden Zone</title>
		<meta charset="utf-8">
	</head>
	<body>
		<p>Hello World!</p>
	</body>
</html> ''')
        print(f"File '{html_file[1]}' created")

# Чтение конфигурационного файла /etc/tor/torrc
# на наличие строк настройки
with open(torrc[1], "r") as tor:
    for i in tor:
        if i == string1 or i == string2:
            torrc[0] = True
            break
# Если строк не было обнаружено: добавить
# строки в файл 'torrc'
if torrc[0] == False:
    with open(torrc[1], "a") as tor:
        tor.write(string1 + "\n" + string2)
        print(f"Strings appended in the '{torrc[1]}' file:")
        print(string1, string2, sep="\n")

# Запуск tor сервиса
system("systemctl start tor.service")
system("systemctl restart tor.service")
sleep(1)

# Чтение хостнэйма сайта
with open(host_file, "r") as host:
    hostname = host.read()
    print(f"\u001b[32m[+]\u001b[0mFile '{host_file}' read")

# Чтение приватного ключа сайта
with open(key_file, "r") as key:
    private_key = key.read()
    print(f"\u001b[32m[+]\u001b[0mFile '{key_file}' read")

# Проверка на наличие `README.txt`
if readme[1] in listdir(getcwd()):
    readme[0] = True

# Если не было обновлений или не было найдено файла README, то обновить или создать README
if www[0] == False or onion[0] == False or html_file[0] == False or readme[0] == False:
    with open(readme[1], "w") as info:
        info.write(f'''
Tor configuration: {torrc[1]}:
-	    {string1}
-	    {string2}\n
HTML file:      {html_file[1]}\n
Main files:     {main_files}
-   hostname [{host_file} ]: 
                {hostname} 
-	private_key [{key_file}]:
    {private_key}
Use this command for run tor service:
[for one time, after rebooting use this command again]
-	systemctl start tor.service
[for always time]
-	systemctl enable tor.service\n
Use this command for activate port 80:
[use in the directory:  {onion[1]}]
-	python3 -m http.server 80
''')
        if readme[0] == True:
            print(f"\u001b[32mFile '{readme[1]}' updated\u001b[0m")
        else:
            print(f"File '{readme[1]}' created")

print("\n\u001b[35mGo to \u001b[0m" + hostname)

# Переход в директорию html файла `/var/www/onion/`
chdir(onion[1])
system("python3 -m http.server 80")
