from SeaBattle import resources
from SeaBattle import settings
from SeaBattle import actions


class Player:
    """
    :param player_id: Уникальный в текущей игре
    :type: :class:`seabattle.game.GameSession`
    :param to_client_func: Функция, которая будет вызвана, когда игрок захочет отправить данные клиенту
    :param on_game_end: Функция, которая будет вызываться, когда игрок хочет закончить игру
    """
    _ships_was_placed = False  # флаг отмечающий, что игрок успешно разместил все корабли
    _my_turn = False  # flag showed that now is current player turn

    def __init__(self, player_id, game, to_client_func, on_game_end):
        self._game = game
        self.player_id = player_id
        self._to_client_func = to_client_func
        self._on_game_end = on_game_end
        self._ships = set([])

    def from_client(self, action: list): # TODO
        """
        Вызов: когда мы получаем сообщение от клиента
        :type action: `list`
        """
        if action[0] == resources.CLICK_ACTION:
            col, row = [int(i) for i in action[2:]]
            if not (0 <= col < settings.NUMBER_OF_CELLS or 0 <= row < settings.NUMBER_OF_CELLS):
                raise TypeError("Wrong cell position")
            if action[1] == resources.MY_BOARD:  # нажатия на мой корабль
                self.place_ship(col, row)
            elif action[1] == resources.OPPONENT_BOARD and self._my_turn:  # click on opponent board
                self.my_fire(col, row)
        else:
            raise TypeError("Wrong action")

    def place_ship(self, col, row): # TODO
        """
        Place current player ship in specific cell. When all
        ships has been placed notify game about this.
        :type col: `int`
        :type row: `int`
        """
        if not self._ships_was_placed and len(self._ships) < settings.MAX_NUMBER_OF_SHIPS:
            self._ships.add((col, row))
            self._to_client_func(actions.paint_cell(resources.MY_BOARD, resources.MY_SHIP, col, row))
            if settings.MAX_NUMBER_OF_SHIPS == len(self._ships):  # we'reready for begin
                self._ships_was_placed = True
                self._game.ready_for_begin(self)
            else:  # not all our ships has been placed
                result_text = (
                    resources.PLACE_SHIPS %
                    (settings.MAX_NUMBER_OF_SHIPS - len(self._ships))
                )
                self._to_client_func(actions.set_text(result_text))

    def my_fire(self, col, row):
        self._game.fire(self, col, row)

    def enemy_fire(self, col, row) -> bool: # TODO
        """
        Вызов: когда враг откроет по мне огонь.
        Проверяет, не попал ли в какой-нибудь корабль.
        Также уведомите игрока, если его корабль был сбит.
        :rtype: `bool` возвращает True, если мой корабль был сбит. В противном случае возвращается False.
        """
        if (col, row) in self._ships:  # enemy hit my ship
            color = resources.MY_DESTOYED_SHIP
            self._ships.remove((col, row,))
            hit = True
        else:  # enemy miss
            color = resources.MY_MISS
            hit = False
        self._to_client_func(actions.paint_cell(resources.MY_BOARD, color, col, row))
        return hit

    def my_miss(self, col, row):
        """
        """
        self._to_client_func(actions.paint_cell(resources.OPPONENT_BOARD, resources.MY_MISS, col, row))

    def my_hit(self, col, row):
        """
        """
        self._to_client_func(actions.paint_cell(resources.OPPONENT_BOARD, resources.MY_HIT, col, row))

    def your_turn(self):
        """
        """
        self._my_turn = True
        self._to_client_func(actions.set_text(resources.YOUR_TURN))

    def wait_other_player_turn(self):
        """
        """
        self._to_client_func(actions.set_text(resources.OTHER_PLAYER_TURN))
        self._my_turn = False

    def wait_other_player_ready(self):
        """
        """
        self._to_client_func(actions.set_text(resources.WAIT_OTHER))

    def has_ships(self):
        """
        """
        return bool(self._ships)

    def win(self):
        """
        """
        self._to_client_func(actions.set_text(resources.WIN))

    def lost(self):
        """
        """
        self._to_client_func(actions.set_text(resources.LOST))

    def error_other_player_leave(self):
        """
        """
        self._to_client_func(actions.set_text(resources.OTHER_PLAYER_LEAVE))

    def finish_game(self):
        """
        """
        self._game = None
        self._on_game_end()

    def disconnect(self):
        """
        """
        if self._game:
            self._game.player_disconnect(self)
            self._game = None

    def __hash__(self):
        return self.player_id

    def __eq__(self, other):
        return self.player_id == other.player_id

    def __ne__(self, other):
        return not self.__eq__(other)