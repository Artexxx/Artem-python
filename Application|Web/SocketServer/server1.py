# сервер запускается на IP адресе 0.0.0.0 и TCP порту 2222
# Получает сообщения длинной не более 1024 байт и отправляет обратно клиенту
# Закрывает соединение при получении сообщения с текстом close﻿

import socket

HOST = '0.0.0.0'
PORT = 2222

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(10)
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        if data.decode() == 'close': break
        conn.send(data)
