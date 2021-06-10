from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel


class Game(object):
    letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
    ships_rules = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
    field_size = len(letters)


class BaseFieldSettings(object):
    # placement
    cell_size = 30
    width_count_cells = 10
    height_count_cells = 10
    # text settings
    font_size = 20
    x, y = 50, 50

    letters_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers_array = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                     '19', '20', '21', '22', '23', '24', '25', '26']

    ### GENERATED settings ###
    cell_size = int(cell_size - 1)
    gwidth = int((width_count_cells + 1) * (cell_size + 0.1))
    gheight = int((height_count_cells + 1) * (cell_size + 0.1))


class YourFieldSettings(object):
    title = "Your ships"


class EnemyFieldSettings(object):
    title = "Enemy field"


class HelpFieldSettings(object):
    title = 'Enemy field'
    game_rules = """
  Каждому участнику игры выдается поле 

  «Корабли»:

    шлюпка (1-палубный корабль) – 2 шт.,

    эсминец (2-х-палубный) – 2 шт.,

    крейсер (3-х-палубный) – 1 шт.

  Игроки по очереди «стреляют»,
    именуя клетки по цифре и букве, и,
    в случае попадания в корабль,
    получают вопрос, на который
    необходимо правильно ответить,
    чтобы «ранить» или «убить» судно.
    """


class YourFieldNameSettings(object):
    # placement and size
    size = (150, 220)
    x = BaseFieldSettings.x + BaseFieldSettings.gwidth // 2 - 50
    y = BaseFieldSettings.y - 130
    horizontal_offset = 3
    # styles and text
    text = 'Your ships'
    font = QFont("Lobster", 24, italic=True)
    css_text = "color: rgb(193, 154, 107); background-color: rgba(0,0,0,0%)"
    css_shadow = "color: rgb(28, 26, 26); background-color: rgba(0,0,0,0%)"


class EnemyFieldNameSettings(object):
    # placement and size
    size = (180, 260)
    x = BaseFieldSettings.gwidth + BaseFieldSettings.cell_size * 4.5 + BaseFieldSettings.gwidth // 2 - 50
    y = BaseFieldSettings.y - 150
    horizontal_offset = 3
    # styles and text
    text = 'Enemy field'
    font = QFont("Lobster", 23, italic=True)
    css_text = "color: rgb(193, 154, 107); background-color: rgba(0,0,0,0%)"
    css_shadow = "color: rgb(28, 26, 26); background-color: rgba(0,0,0,0%)"


class HelpFieldNameSettings(object):
    # placement and size
    size = (180, 150)
    x = BaseFieldSettings.gwidth + BaseFieldSettings.cell_size * 4.5 + BaseFieldSettings.gwidth // 2 - 80
    y = BaseFieldSettings.y - 90
    horizontal_offset = 3
    # styles and text
    text = 'Game rules'
    font = QFont("Lobster", 23, italic=True)
    css_text = "color: rgb(193, 154, 107); background-color: rgba(0,0,0,0%)"
    css_shadow = "color: rgb(28, 26, 26); background-color: rgba(0,0,0,0%)"


class Ships():
    ships_rules = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
