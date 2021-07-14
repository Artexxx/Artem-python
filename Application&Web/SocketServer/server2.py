# tcp сервер запускается на IP адресе 0.0.0.0 и TCP порту 2222
# обслуживает 10 клиентов одновременно
from threading import Thread
import socket

HOST = '0.0.0.0'
PORT = 2222


def server(conn, addr):
    while True:
        data = conn.recv(1024)
        if data.decode() == 'close':
            break
        conn.send(data)
    conn.close()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(10)
    for _ in range(10):
        conn, addr = s.accept()
        t = Thread(target=server, args=(conn, addr))
        t.start()
