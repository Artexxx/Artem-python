from distributed._concurrent_futures_thread import ThreadPoolExecutor

from PyQt5.QtCore import QTimer, Qt, QRect, QObject
from PyQt5.QtGui import QPainter, QColor, QFont, QPixmap, QPen, QTransform
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QGraphicsItem, QTextEdit, QPushButton, \
    QGraphicsDropShadowEffect

from qtpy import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal
import socket

from settings import BaseFieldSettings, HelpFieldSettings
from settings import YourFieldSettings, EnemyFieldSettings
from settings import EnemyFieldNameSettings, HelpFieldNameSettings, YourFieldNameSettings
from settings import Ships

from random import shuffle
from generate_ships import init_ship
import re



class MouseBaseController():
    window = None

    def set_mouse_tracking_on(self, window):
        self.window = window
        self.enemy_field = self.window.enemy_field
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        # hide EnemyBaseFieldSettings.stand
        if self.enemy_field.MouseInFieldFlag:
            self.enemy_field.MouseInFieldFlag = False
            self.enemy_field.fire_stand.setParent(None)


class Signal(QObject):
    pyqtSignal = pyqtSignal(object)

    def create(self, data):
        self.pyqtSignal.emit(data)

    def connect(self, function):
        self.pyqtSignal.connect(function)


class BaseServer():
    _is_game_coordinates_pattern = re.compile("\\('[A-Z][A-Z]?', '[0-9][0-9]?'\\)")

    def __init__(self, server_ip, server_port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server = self.server
        server.bind((server_ip, server_port))
        server.listen()
        print('[#] SERVER STARTED')

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~| Server data |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        self.CLIENTS_DATA = {'Максим': {'IP': '127.0.0.0', 'PORT': server_port},
                             'Настя': {'IP': '127.0.0.0', 'PORT': server_port},
                             'Я': {'IP': server_ip, 'PORT': server_port}}

        self.IP_LIST = {'127.0.0.0': 'Максим', server_ip: 'Я'}

    def parallel_infinite_server(self):
        while True:
            try:
                connection, addres = self.server.accept()
                data = connection.recv(1024).decode('utf-8')
                if self.IP_LIST[addres[0]] != "Я":
                    signal.create(data=["TestName", data])
                connection.close()

            except Exception as error:
                print('[#] SERVER STOPPED', error)
                connection.close()

    def receiving_message_on_server(self, data: list):
        """[Signal function] """
        user, message = data
        print('[#] Получен сигнал с сервера со следующим сообщением:', message)
        is_game_coordinates = re.fullmatch(self._is_game_coordinates_pattern, message)
        if is_game_coordinates:
            print('Получены игровые координаты', message)
        else:
            base_window.base_messenger.add_message_on_mainField(message, user)


class MessangerMainField(QTextEdit, MouseBaseController):
    pass


class BaseMessenger():
    def __init__(self):
        self.sendField = QTextEdit()
        self.mainField = MessangerMainField()
        self.mainField.set_mouse_tracking_on(base_window)
        self.sendButton = QPushButton()

    def get_text_message_from_sendField(self):
        message = self.sendField.toPlainText()
        self.sendField.setText('')  # clear input-field
        return message

    def add_message_on_mainField(self, message: str, user: str):
        if user == 'Я':
            custom_message = f'Это моё сообщение >>> {message}'
        else:
            custom_message = f'[{user}]: {message}'
        self.mainField.setText(self.mainField.toPlainText() + custom_message + '\n')

    def send_message(self, message):
        server_object = base_server
        ip, port = server_object.CLIENTS_DATA["Я"].values()
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, port))
        client.sendall(f'{message}'.encode('utf-8'))
        self.add_message_on_mainField(message, user="Я")
        client.close()

    def send_message_from_sendField(self):
        text = self.get_text_message_from_sendField().strip()
        if text: self.send_message(text)


class BaseWindow(QMainWindow, MouseBaseController):
    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

        ### Init fields ###
        self.your_field = YourField()
        self.enemy_field = EnemyField()
        self.help_field = HelpField()

    def initUI(self):
        self.resize(850, 630)
        self.setStyleSheet("background-color:  #FF9E73")
        self.setMouseTracking(True)

    def draw_field(self, field, draw_title=True):
        if draw_title:
            field.draw_title(base_window)
        base_window.layout().addWidget(field)


class BaseField(QWidget, BaseFieldSettings):
    """
    Загружается из настроек:
    """
    cell_size: int  # размер одной клетки поля
    width_count_cells: int   # количество клеток по горизонтали
    height_count_cells: int  # количество клеток по вертикали
    letters_array: list  # [A-Z] - список букв, для игровых координат
    numbers_array: list  # [1-26] - список чисел, для игровых координат
    gwidth: int  # сгенерированная, относительно количества и размера клеток, ширина поля
    gheight: int  # сгенерированная, относительно количества и размера клеток, высота поля

    def paintEvent(self, event):
        painter = QPainter(self)
        font = painter.font()
        font.setPixelSize(20)
        painter.setFont(font)
        w = self.gwidth
        h = self.gheight

        # horizontal lines
        y = self.cell_size
        while y <= h:
            painter.drawLine(self.cell_size, y, w - 3, y)
            y += self.cell_size

        # vertical lines
        x = self.cell_size
        while x <= w:
            painter.drawLine(x, self.cell_size, x, h - 3)
            x += self.cell_size

        # letters
        y = 0
        count = 0
        while y <= h:
            y += self.cell_size
            if count >= 1:
                letter = self.letters_array[count - 1]
                painter.drawText(9, y - 4, ' ' + letter if letter in 'IJL' else letter)
            count += 1

        # numbers
        x = 0
        count = 0
        while x <= w:
            x += self.cell_size
            if count >= 0:
                number = self.numbers_array[count]
                # К числу прибавляем пробел, потому-что 10 занимает две цифры, а 9 - одну
                painter.drawText(x + 4, 22, ' ' + number if count < 9 else number)
            count += 1


class YourField(BaseField, YourFieldSettings):
    """
    Рисует поле игрока в левой части экрана.
    [#] На этом поле будут распологаться видимые корабли

    Загружается из настроек:
    """
    title: str

    def __init__(self):
        QWidget.__init__(self)
        self.resize(BaseField.gwidth, BaseField.gheight)
        self.move(50, 50)

    def paintEvent(self, event):
        super().paintEvent(event)

    def draw_title(self, base_window):
        label = QtWidgets.QLabel(self.title)
        label.setFont(QFont("Fira Mono Bold", 24))
        label.adjustSize()
        label.move(self.x()+label.width()//2+30, self.y()-label.height())
        base_window.layout().addWidget(label)


class EnemyField(BaseField, EnemyFieldSettings):
    """
    Рисует поле врага в правой части экрана.
    [#] На этом поле будут распологаться невидимые корабли, которые игрок бутет атаковать

    Загружается из настроек:
    """
    title: str

    def __init__(self):
        QWidget.__init__(self)
        self.initUI()

        # ~~~~~~~ settings FireStand ~~~~~~~ #
        self.fire_stand = FireStand(self)
        self.setMouseTracking(True)
        self.MouseInFieldFlag = False

    def initUI(self):
        self.resize(BaseField.gwidth, BaseField.gheight)
        self.move(int(BaseField.gwidth + BaseField.cell_size * 4.5), 50)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(50)
        self.setGraphicsEffect(shadow)

    def draw_title(self, base_window):
        label = QtWidgets.QLabel(self.title)
        label.setFont(QFont("Fira Mono Bold", 24))
        label.adjustSize()
        label.move(self.x()+label.width()//2+16, self.y()-label.height())
        base_window.layout().addWidget(label)

    def paintEvent(self, event):
        super().paintEvent(event)

    def mouseMoveEvent(self, event):
        scaled_x = event.x()
        scaled_y = event.y()
        NowMouseInFieldFlag = self._check_coordinate_in_field(scaled_x, scaled_y)
        if NowMouseInFieldFlag:
            self.customMouseMoveEvent(scaled_x, scaled_y)
            if not self.MouseInFieldFlag:
                self.MouseInFieldFlag = True
                base_window.layout().addWidget(self.fire_stand)
        elif self.MouseInFieldFlag:
            self.MouseInFieldFlag = False
            self.fire_stand.setParent(None)

    def customMouseMoveEvent(self, hover_x, hover_y):
        new_stand_x = int((hover_x // self.cell_size) * self.cell_size)
        new_stand_y = int((hover_y // self.cell_size) * self.cell_size)
        if self.fire_stand.x() != new_stand_x or self.fire_stand.y() != new_stand_y:
            self.fire_stand.move_stand_in_field(new_stand_x, new_stand_y)

    def _parse_numbers_to_str_guess(self, x, y):
        """
        Вспомогательная функция, переводит координаты нажатия на поле в игровые координаты
        return: str
            Координаты нажатия в буквенном виде
        """
        # (-1) - т.к первая строка и колонка поля заняты игровыми координатами
        return (self.settings.letters_array[int(y // self.settings.cell_size) - 1],
                self.settings.numbers_array[int(x // self.settings.cell_size) - 1])

    def send_click_guess(self, press_coordinates):
        server_object = base_server
        ip, port = server_object.CLIENTS_DATA["Я"].values()
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, port))
        client.sendall(f'{press_coordinates}'.encode('utf-8'))
        client.close()


    def _check_coordinate_in_field(self, x, y) -> bool:
        if x < 0 or y < 0:
            return False
        # первая строка и колонка поля заняты игровыми координатами
        return x > int(self.cell_size) and y > int(self.cell_size) and x < int(self.width) and y < int(self.height)


class HelpField(QLabel, HelpFieldSettings):
    """
    Поле с правилами игры в правой части экрана.

    Загружается из настроек:
    """
    game_rules: str  # текст с правилами игры
    title: str

    def __init__(self):
        QWidget.__init__(self)
        self.initUI()

    def initUI(self):
        self.resize(325, 325)
        self.move(464, 62)
        self.setStyleSheet("""
            QWidget {
                background-color: rgb(56, 56, 53);
                color: rgb(234, 216, 150);
                font-size: 15px;
                box-shadow: 2px -2px 10px 0.85px rgb(56, 56, 53);
                border: 5px;
                border-style: inset;
                border-color: rgb(193, 154, 107) rgb(142, 113, 78) rgb(142, 113, 78) rgb(193, 154, 107);
                }
            """)
        self.setText(self.game_rules)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(50)
        self.setGraphicsEffect(shadow)

    def draw_title(self, base_window):
        label = QtWidgets.QLabel(self.title)
        label.setFont(QFont("Fira Mono Bold", 24))
        label.adjustSize()
        label.move(self.x()+label.width()//2, self.y()-label.height() - 6)
        base_window.layout().addWidget(label)


def draw_field_name(base_window, settings=YourFieldNameSettings):

    # """ Заголовок для поля - крупный текст с эффектом тени """
    # # placement and size #
    # size = (150, 220)
    # x = 165
    # y = -80
    # horizontal_offset = 3
    # # styles and text #
    # text = 'Your ships'
    # font = QFont("Lobster", 24, italic=True)
    # css_text = "color: rgb(193, 154, 107); background-color: rgba(0,0,0,0%)"
    # css_shadow = "color: rgb(28, 26, 26); background-color: rgba(0,0,0,0%)"
    #
    #
    # title = QtWidgets.QLabel(base_window)
    # title.resize(*settings.size)
    # title.setFont(settings.font)
    # title.setText(settings.text)
    # title.move(settings.x, settings.y)
    # title.setStyleSheet(settings.css_text)
    # title.adjustSize()
    # base_window.layout().addWidget(title)

    #
    # shadow = QtWidgets.QLabel(base_window)
    # shadow.resize(*settings.size)
    # shadow.setFont(settings.font)
    # shadow.setText(settings.text)
    # shadow.move(settings.x - settings.horizontal_offset, settings.y)
    # shadow.setStyleSheet(settings.css_shadow)
    # # shadow.adjustSize()

    resultsLabel = QLabel(settings.text)
    resultsLabel.setFont(QFont("Fira Mono Bold", 24))
    resultsLabel.adjustSize()
    resultsLabel.move(100, 100)
    base_window.layout().addWidget(resultsLabel)


def draw_messenger(base_window):
    base_messenger = base_window.base_messenger
    ## draw а field where the player writes messages ##
    sendField = base_messenger.sendField
    sendField.setFixedSize(430, 50)
    sendField.move(base_window.width() // 2 - sendField.width() // 2 - 40,
                   base_window.height() - sendField.height() - 15)
    sendField.setStyleSheet("background-color:  #FF9E73")
    base_window.layout().addWidget(sendField)
    ## draw а chat field that displays players messages ##
    mainField = base_messenger.mainField
    mainField.setFixedSize(620, 150)
    mainField.move(base_window.width() // 2 - mainField.width() // 2 + 17, sendField.y() - mainField.height() - 10)
    mainField.setStyleSheet("background-color:  #fff6df")
    base_window.layout().addWidget(mainField)
    ## draw а button that sends a message to the chat when clicked ##
    sendButton = base_messenger.sendButton
    sendButton.setFixedSize(100, 50)
    sendButton.move(sendField.x() + sendField.width() + 20, sendField.y())
    sendButton.setStyleSheet("background-color:  #f04747")
    base_window.layout().addWidget(sendButton)
    sendButton.clicked.connect(lambda: base_messenger.send_message_from_sendField())


def start_game_animation(base_window):
    # TODO
    # def move_enemy_field_within():
    #     guide_label = base_window.guide_label
    #     if guide_label.x() < BaseFieldSettings.width + BaseFieldSettings.cell_size * 4.5:
    #         field.move(BaseFieldSettings.width + BaseFieldSettings.cell_size * 4.5 + BaseFieldSettings.width // 2 - 80, BaseFieldSettings.map_field['y'] - 100)

    def move_guide_without():
        guide_label = base_window.help_field
        guide_label.move(guide_label.x() + 10, guide_label.y())
        guide_label_title = base_window.guide_title1
        guide_label_title.move(guide_label_title.x() + 10, guide_label_title.y())
        guide_label_title = base_window.guide_title2
        guide_label_title.move(guide_label_title.x() + 10, guide_label_title.y())
        if guide_label.x() > base_window.width():
            base_window.timer.stop()
            base_window.draw_field(base_window.en)

    base_window.timer = QTimer()
    timer = base_window.timer
    timer.setInterval(16)
    timer.timeout.connect(lambda: move_guide_without())
    timer.start()


def _parse_guess(location: str):
    """
    Вспомогательная функция, переводит игровые координаты поля в числовые
    locations (str)
        Координаты корабля в буквенном виде
        Пример: ['C3', 'E3', 'D3']
    return: List[x y]
        Координаты корабля в численном виде
    >>>  _parse_guess('A1')
    0, 0
    >>>  _parse_guess('C1')
    0, 60
    """
    return (BaseFieldSettings.numbers_array.index(location[1:]) * BaseFieldSettings.cell_size,
            BaseFieldSettings.letters_array.index(location[0]) * BaseFieldSettings.cell_size)


class FireStand(QWidget):
    def __init__(self, Field):
        QWidget.__init__(self)
        self.field_object = Field
        self.setFixedSize(self.field_object.cell_size + 1, self.field_object.cell_size + 1)

        # ~~~~~~~~~~~~~~ Default color settings ~~~~~~~~~~~~~~~ #
        self._green_color_fill = QColor()  # заливка
        self._green_color_fill.setNamedColor('#BCFFB4')
        self._green_color_outline = QColor()  # рамка
        self._green_color_outline.setNamedColor('#00AF17')

    def paintEvent(self, base_window):
        painter = QPainter(self)
        fill_color = self._green_color_fill
        outline_color = self._green_color_outline
        painter.setBrush(fill_color)
        pen = QPen(outline_color, 4)
        painter.setPen(pen)
        painter.drawRect(0, 0, self.field_object.cell_size, self.field_object.cell_size)

    def mousePressEvent(self, event):
        press_x = int(self.x() - self.field_object.x() + 3)
        press_y = int(self.y() - self.field_object.y() + 3)
        press_coordinates = self.field_object._parse_numbers_to_str_guess(press_x, press_y)
        self.field_object.send_click_guess(press_coordinates)

    def mouseMoveEvent(self, event):
        ...

    def move_stand_in_field(self, x, y):
        if x < self.field_object.width() - self.width() and y < self.field_object.height() - self.height():
            self.move(self.field_object.x() + x, self.field_object.y() + y)



class Ships():
    def __init__(self):
        self.ships_rules = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
        self.all_ships = set()

    def add_ships_on_window(self):
        main_field = [[0 for _ in range(10)] for _ in range(10)]
        shuffle(self.ships_rules)
        for ships_size in self.ships_rules:
            main_field, (number_of_palubs, orientation, start_coordinate) = init_ship(ships_size, main_field)
            ship = Ship(number_of_palubs, orientation, start_coordinate)
            base_window.layout().addWidget(ship)
            self.all_ships.add(ship)
        assert len(self.all_ships) == len(self.ships_rules)

    def check_ship_intersect(self, otherShip, myShip) -> bool:
        rect_other_ship = QRect(otherShip.x(), otherShip.y(), otherShip.width(), otherShip.height())
        rect_my_ship = QRect(myShip.x()-BaseFieldSettings.cell_size+1, myShip.y()-BaseFieldSettings.cell_size+1, myShip.width()+BaseFieldSettings.cell_size+1, myShip.height()+BaseFieldSettings.cell_size+1)

        rect_intersected_ships = rect_my_ship.intersected(rect_other_ship)
        return rect_intersected_ships.width() != 0 and rect_intersected_ships != 0

    def check_all_intersect(self, myShip, withoutShips: set) -> bool:
        '''Проверяет пересечение всех корблей из self.all_ships без withoutShips c короблём myShip'''
        ships_without_myship = self.all_ships - {*withoutShips, myShip}
        for ship in ships_without_myship:
            if self.check_ship_intersect(ship, myShip):
                return True
        return False


class ShipStand(QWidget):
    def __init__(self, Ship):
        QWidget.__init__(self)
        self.ship_object = Ship
        if Ship.orientation == 'horizontal':
            self.setFixedSize(Ship.number_of_palubs * BaseFieldSettings.cell_size + 1, BaseFieldSettings.cell_size + 1)
        else:
            self.setFixedSize(BaseFieldSettings.cell_size + 1, Ship.number_of_palubs * BaseFieldSettings.cell_size + 1)
        self.move(self.ship_object.x(), self.ship_object.y())

        # ~~~~~~~~~~~~~~ Default color settings ~~~~~~~~~~~~~~~ #
        self._green_color_fill = QColor()  # заливка
        self._green_color_fill.setNamedColor('#BCFFB4')
        self._green_color_outline = QColor()  # рамка
        self._green_color_outline.setNamedColor('#00AF17')
        self._red_color_fill = QColor()  # заливка
        self._red_color_fill.setNamedColor('#FA8072')
        self._red_color_outline = QColor()  # рамка
        self._red_color_outline.setNamedColor('#DC143C')
        self.RenderColorFlag = 'GREEN'

        # ~~~~~~~~~~~~~~ TEMP ~~~~~~~~~~~~~~~ #
        self.last_valid_position = (self.ship_object.x(), self.ship_object.y())

    def paintEvent(self, base_window):
        painter = QPainter(self)
        x = 0
        y = 0
        if self.RenderColorFlag == 'GREEN':
            fill_color = self._green_color_fill
            outline_color = self._green_color_outline
        elif self.RenderColorFlag == 'RED':
            fill_color = self._red_color_fill
            outline_color = self._red_color_outline
        else:
            assert self.RenderColorFlag in ['GREEN', 'RED']

        painter.setBrush(fill_color)
        pen = QPen(outline_color, 4)
        painter.setPen(pen)
        if self.ship_object.orientation == 'horizontal':
            for _ in range(self.ship_object.number_of_palubs):
                painter.drawRect(x, y, BaseFieldSettings.cell_size, BaseFieldSettings.cell_size)
                x += BaseFieldSettings.cell_size
        else:
            for _ in range(self.ship_object.number_of_palubs):
                painter.drawRect(x, y, BaseFieldSettings.cell_size, BaseFieldSettings.cell_size)
                y += BaseFieldSettings.cell_size

    def move_stand_in_field(self):
        _field_x = BaseFieldSettings.x + BaseFieldSettings.cell_size + 1
        _field_y = BaseFieldSettings.y + BaseFieldSettings.cell_size + 1
        start_x, start_y = self.ship_object.x(), self.ship_object.y()
        if self.ship_object.orientation == 'horizontal':
            width_ship = self.ship_object.number_of_palubs * BaseFieldSettings.cell_size + 1
            height_ship = BaseFieldSettings.cell_size + 1
        else:
            width_ship = BaseFieldSettings.cell_size + 1
            height_ship = self.ship_object.number_of_palubs * BaseFieldSettings.cell_size + 1
        is_left = start_x < _field_x
        is_higher = start_y < _field_y
        is_right = start_x > _field_x + BaseFieldSettings.gwidth - (width_ship + BaseFieldSettings.cell_size)
        is_lower = start_y > _field_y + BaseFieldSettings.gheight - (height_ship + BaseFieldSettings.cell_size)
        if is_left and not (is_lower or is_higher):
            _all = False
            self.move(_field_x, _field_y + ((start_y-_field_y + BaseFieldSettings.cell_size//2)//BaseFieldSettings.cell_size) * BaseFieldSettings.cell_size)

        if is_higher and not (is_right or is_left):
            self.move(_field_x + ((start_x-_field_x+BaseFieldSettings.cell_size//2)//BaseFieldSettings.cell_size) * BaseFieldSettings.cell_size, _field_y)

        if is_right and not (is_lower or is_higher):
            self.move(_field_x + BaseFieldSettings.cell_size * 9 - (width_ship - BaseFieldSettings.cell_size), _field_y + ((start_y-_field_y + BaseFieldSettings.cell_size//2)//BaseFieldSettings.cell_size) * BaseFieldSettings.cell_size)

        if is_lower and not (is_right or is_left):
            self.move(_field_x + ((start_x-_field_x+BaseFieldSettings.cell_size//2)//BaseFieldSettings.cell_size) * BaseFieldSettings.cell_size, _field_y +BaseFieldSettings.cell_size * 9 - (height_ship - BaseFieldSettings.cell_size))

        if all((not is_higher, not is_right, not is_left, not is_lower)):
            self.move(_field_x + ((start_x-_field_x+BaseFieldSettings.cell_size//2)//BaseFieldSettings.cell_size) * BaseFieldSettings.cell_size, _field_y + ((start_y-_field_y + BaseFieldSettings.cell_size//2)//BaseFieldSettings.cell_size) * BaseFieldSettings.cell_size)

        if not Ships.check_all_intersect(self, withoutShips={self.ship_object}):
            self.RenderColorFlag = 'GREEN'
            self.last_valid_position = (self.x(), self.y())
        else:
            self.RenderColorFlag = 'RED'
        self.repaint()

    def move_in_last_valid_position(self):
        x, y = self.last_valid_position
        self.move(x, y)
        if self.RenderColorFlag == 'RED':
            self.RenderColorFlag = 'GREEN'
        self.repaint()

    def before_rotation(self):
        ''' Удаляет стэнд корабля с окна '''
        self.setParent(None)

    def after_rotation(self):
        '''Добавляет стэнд корабля на окно
        [*] корабль должен рисоваться сверху'''
        base_window.layout().addWidget(self)
        self.ship_object._paint_first_ship()

        if self.ship_object.orientation == 'horizontal':
            self.setFixedSize(self.ship_object.number_of_palubs * BaseFieldSettings.cell_size + 1, BaseFieldSettings.cell_size + 1)
        else:
            self.setFixedSize(BaseFieldSettings.cell_size + 1, self.ship_object.number_of_palubs * BaseFieldSettings.cell_size + 1)
        self.move(self.ship_object.x(), self.ship_object.y())


class Ship(QWidget):
    """
    locations (list)
        Координаты корабля
        Пример: ['C3', 'E3', 'D3']
    duration (str)
        Направление корабля {'vertical', 'horizontal'}
        Пример: 'vertical'
    start_coordinate (str)
        Начальная координата корабля (там где его нос)
        Пример: 'D3'
    """
    number_of_palubs = None
    orientation = None
    RotationFlag = False
    angle = 0

    def __init__(self, number_of_palubs, orientation, start_coordinate):
        QWidget.__init__(self)
        self.number_of_palubs = number_of_palubs
        self.orientation = orientation
        if self.orientation == 'horizontal':
            self.setFixedSize(self.number_of_palubs * BaseFieldSettings.cell_size + 1, BaseFieldSettings.cell_size + 1)
        else:
            self.setFixedSize(BaseFieldSettings.cell_size + 1, self.number_of_palubs * BaseFieldSettings.cell_size + 1)
        self.sunk = False

        _field_x = BaseFieldSettings.x + BaseFieldSettings.cell_size + 1
        _field_y = BaseFieldSettings.y + BaseFieldSettings.cell_size + 1
        start_x, start_y = _parse_guess(start_coordinate)
        self.move(_field_x + start_x, _field_y + start_y)
        self.stand = ShipStand(self)
        base_window.layout().addWidget(self.stand)

    def _paint_first_ship(self):
        '''Рисует корабль над другими'''
        self.stand.raise_()
        self.raise_()

    def paintEvent(self, base_window):
        painter = QPainter(self)
        if self.RotationFlag:
            x, y = -15, -15
            painter.translate(30, 30)
            painter.rotate(-self.angle)
        else:
            x, y = 0, 0
        custom_color_fill = QColor()  # заливка
        custom_color_fill.setNamedColor('#2b2216')
        painter.setBrush(custom_color_fill)
        custom_color_outline = QColor()  # рамка
        custom_color_outline.setNamedColor('#c19a6b')
        pen = QPen(custom_color_outline, 4)
        painter.setPen(pen)
        if self.orientation == 'horizontal':
            for _ in range(self.number_of_palubs):
                painter.drawRect(x, y, BaseFieldSettings.cell_size, BaseFieldSettings.cell_size)
                x += BaseFieldSettings.cell_size
        else:
            for _ in range(self.number_of_palubs):
                painter.drawRect(x, y, BaseFieldSettings.cell_size, BaseFieldSettings.cell_size)
                y += BaseFieldSettings.cell_size

    def mouseDoubleClickEvent(self, event):  ## TODO: custom rotation with QTimer
        self.stand.before_rotation()

        def _rotate_animation(self):
            last_orientation = self.orientation
            if last_orientation == 'horizontal':
                self.angle -= 5
            else:
                self.angle += 5
            self.repaint()
            if abs(self.angle) >= 90:
                self.timer_rotation.stop()
                # self.angle = 0
                if last_orientation == 'horizontal':
                    self.move(self.x() + 15, self.y() + 15)
                else:
                    self.move(self.x() + 15, self.y() + 15)

                self.RotationFlag = False
                size_after_rotation = self.size_before_rotation[::-1]
                self.setFixedSize(*size_after_rotation)
                self.orientation = 'vertical' if last_orientation == 'horizontal' else 'horizontal'
                self.stand.after_rotation()

        if not self._rotate_permission():
            print("No permission for rotate ship")
            return 1

        self.size_before_rotation = (self.width(), self.height())
        self.setFixedSize(int(max(self.size_before_rotation) * 1.2), int(max(self.size_before_rotation) * 1.2))
        self.move(self.x()-15, self.y()-15)
        self.RotationFlag = True

        ##~~~~~~~~Animation~~~~~~~~##
        self.timer_rotation = QTimer()
        timer = self.timer_rotation
        timer.setInterval(30)
        timer.timeout.connect(lambda: _rotate_animation(self))
        timer.start()


    def mouseDoubleClickEvent_outdated(self, event):  # FIXME: outdated function
        self.orientation = 'horizontal' if self.orientation == 'vertical' else 'vertical'
        if self.orientation == 'horizontal':
            self.setFixedSize(self.number_of_palubs * BaseFieldSettings.cell_size + 1, BaseFieldSettings.cell_size + 1)
            self.stand.setFixedSize(self.number_of_palubs * BaseFieldSettings.cell_size + 1, BaseFieldSettings.cell_size + 1)
        else:
            self.setFixedSize(BaseFieldSettings.cell_size + 1, self.number_of_palubs * BaseFieldSettings.cell_size + 1)
            self.stand.setFixedSize(BaseFieldSettings.cell_size + 1, self.number_of_palubs * BaseFieldSettings.cell_size + 1)

    def _rotate_permission(self) -> bool:
        return self.number_of_palubs != 1

    def mousePressEvent(self, event):
        self._paint_first_ship()
        self.press_x = event.x()
        self.press_y = event.y()
        base_window.layout().addWidget(self)

    def mouseReleaseEvent(self, event):
        approximately_equal = lambda a, b: abs(a - b) < 13

        def _valid_position_animation(self, delta_x, delta_y, end_pos):
            self.move(self.x() + delta_x, self.y() + delta_y)
            x_e, y_e = end_pos
            x_n, y_n = self.x(), self.y()
            if approximately_equal(x_e, x_n) and approximately_equal(y_e, y_n):
                self.timer_move.stop()
                self.move(x_e, y_e)

        if not self.RotationFlag:
            self.stand.move_in_last_valid_position()
            self.timer_move = QTimer()
            timer = self.timer_move
            timer.setInterval(30)
            end_pos = self.stand.last_valid_position
            start_pos = (self.x(), self.y())
            delta_x, delta_y = int((end_pos[0] - start_pos[0]) / 10 * ((-1) ** (int(end_pos[0] > start_pos[0]) + 2) * ((-1) ** (int(end_pos[0] < start_pos[0]) + 1)))), \
                               int((end_pos[1] - start_pos[1]) / 10 * ((-1) ** (int(end_pos[1] > start_pos[1]) - 3)) * ((-1) ** (int(end_pos[1] < start_pos[1]) + 2)))
            timer.timeout.connect(lambda: _valid_position_animation(self, delta_x, delta_y, end_pos))
            timer.start()


    def mouseMoveEvent(self, event):
        if not self._move_permission():
            print("No permission for movement ship")
            return 1
        x = self.x() + event.x() - self.press_x
        y = self.y() + event.y() - self.press_y
        self.move(x, y)
        self.stand.move_stand_in_field()

    def _move_permission(self) -> bool:
        return self.RotationFlag != True


if __name__ == '__main__':
    root = QApplication([])
    base_window = BaseWindow()
    base_window.draw_field(base_window.your_field, draw_title=True)
    base_window.draw_field(base_window.help_field, draw_title=True)

    # start_game_animation(base_window)

    base_window.set_mouse_tracking_on(base_window)
    #
    Ships = Ships()
    Ships.add_ships_on_window()
    base_window.show()
    #
    # base_server = BaseServer(TODO, 7777)
    # base_window.base_messenger = BaseMessenger()
    # draw_messenger(base_window)
    # signal = Signal()
    # signal.connect(lambda data: base_server.receiving_message_on_server(data))
    # executor = ThreadPoolExecutor(2)
    # executor.submit(lambda: base_server.parallel_infinite_server())
    root.exec()