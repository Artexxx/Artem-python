from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit
from distributed._concurrent_futures_thread import ThreadPoolExecutor
import socket

CLIENTS_DATA = {'Максим': {'IP': TODO, 'PORT': 6666},
                'Логунов': {'IP': TODO, 'PORT': 6666},
                'Я': {'IP': TODO, 'PORT': 7777}}

IP_LIST = {TODO: 'Максим',
           TODO: 'Я'}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.0.144', 7777))
server.listen()
print('[#] SERVER STARTED')


def infinite_server(window):
    while True:
        try:
            connection, addres = server.accept()
            data = connection.recv(1024).decode('utf-8')
            print('CLIENT', addres[0], data)
            print(IP_LIST[addres[0]], data)
            signal.create(data=[IP_LIST[addres[0]], data])
            connection.close()

        except Exception as e:
            print('[#] SERVER STOPPED', e.args)
            connection.close()


def parallel(window, signal):
    infinite_server(window)


def send_message_to(name='Я'):
    assert name in CLIENTS_DATA  # FIXME
    ip, port = CLIENTS_DATA[name].values()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    message = get_text_message_from_field(sendField)
    client.sendall(f'{message}'.encode('utf-8'))
    add_text_on_field(mainField, f'Это мое ообщение >>> {message}')
    client.close()


def get_text_message_from_field(field):
    message = field.toPlainText()
    field.setText('')
    return message


def add_text_on_field(field, text):
    field.setText(field.toPlainText() + text + '\n')


def siganal_function(data: list):
    print('[#] Получен сигнал с сервера со следующим сообщением:', data[1])
    add_text_on_field(mainField, f'[{data[0]}]: {data[1]}')


if __name__ == '__main__':
    root = QApplication([])
    base_window = QMainWindow()
    base_window.resize(850, 600)
    base_window.setStyleSheet("background-color:  #bb1E73")

    sendField = QTextEdit()
    sendField.setFixedSize(400, 100)
    sendField.move(base_window.width() // 2 - sendField.width() // 2 - 50,
                   base_window.height() - sendField.height() - 5)
    sendField.setStyleSheet("background-color:  #FF9E73")
    base_window.layout().addWidget(sendField)

    mainField = QTextEdit()
    mainField.setFixedSize(630, 200)
    mainField.move(base_window.width() // 2 - mainField.width() // 2 - 30, sendField.y() - mainField.height() - 20 - 5)
    mainField.setStyleSheet("background-color:  #fff6df")
    base_window.layout().addWidget(mainField)

    sendButton = QPushButton()
    sendButton.setFixedSize(100, 100)
    sendButton.move(sendField.x() + sendField.width() + 20, sendField.y())
    sendButton.setStyleSheet("background-color:  #f04747")
    base_window.layout().addWidget(sendButton)
    sendButton.clicked.connect(lambda: send_message_to(name='Максим'))

    signal = Signal()
    signal.connect(lambda data: siganal_function(data))

    base_window.show()

    executor = ThreadPoolExecutor(2)
    executor.submit(lambda: parallel(base_window, signal))
    root.exec()
