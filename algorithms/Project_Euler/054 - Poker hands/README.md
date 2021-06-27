# [Покерные ставки](TODO)
## [Проблема](https://euler.jakumo.org/problems/view/54.html)



В карточной игре покер ставка состоит из пяти карт и оценивается от самой младшей до самой старшей в следующем порядке:

| Комбинация  | Значение                   |
| -------------:| ------------------------|
|Старшая карта  |Карта наибольшего достоинства.|
|Одна пара  |Две карты одного достоинства.|
|Две пары   |Две различные пары карт|
|Тройка     |Три карты одного достоинства.|
|Стрейт     |Все пять карт по порядку, любые масти.|
|Флаш       | Все пять карт одной масти.|
|Фул-хаус   |Три карты одного достоинства и одна пара карт.|
|Каре       |Четыре карты одного достоинства.|
|Стрейт-флаш|Любые пять карт одной масти по порядку.|
|Роял-флаш  | Десятка, валет, дама, король и туз одной масти.|

Достоинство карт оценивается по порядку:
<br>
2, 3, 4, 5, 6, 7, 8, 9, 10, валет, дама, король, туз.

Если у двух игроков получились ставки одного порядка, то выигрывает тот, у кого карты старше:
    к примеру, две восьмерки выигрывают две пятерки (см. пример 1 ниже).
<br>
Если же достоинства карт у игроков одинаковы, к примеру, у обоих игроков пара дам, 
    то сравнивают карту наивысшего достоинства (см. пример 4 ниже);
    если же и эти карты одинаковы, сравнивают следующие две и т.д.

Допустим, два игрока сыграли 5 ставок следующим образом:

|Ставка|1-й игрок| 	2-й игрок|	 	Победитель|
| ----- | ------  | ---------- | -----------|
|1 |5♥ 5♣ 6♠ 7♠ K♦<br>Пара пятерок|2♣ 3♠ 8♠ 8♦ T♦<br>Пара восьмерок|2-й игрок|
|2 |5♦ 8♣ 9♠ J♠ A♣<br>Старшая карта туз| 2♣ 5♣ 7♦ 8♠ Q♥<br>Старшая карта дама|1-й игрок|
|3 |2♦ 9♣ A♠ A♥ A♣<br>Три туза| 3♦ 6♦ 7♦ T♦ Q♦<br>Флаш, бубны|2-й игрок|
|4 |4♦ 6♣ 9♥ Q♥ Q♣<br>Пара дам<br>Старшая карта девятка|3♦ 6♦ 7♥ Q♦ Q♠<br>Пара дам <br> карта семерка|1-й игрок|
|5 |2♥ 2♦ 4♣ 4♦ 4♠<br>Фул-хаус<br>Три четверки|3♣ 3♦ 3♠ 9♠ 9♦<br>Фул-хаус <br> тройки|1-й игрок|

Файл poker.txt содержит одну тысячу различных ставок для игры двух игроков.
<br>В каждой строке файла приведены десять карт (отделенные одним пробелом): 
    первые пять - карты 1-го игрока,
    оставшиеся пять - карты 2-го игрока.
<br>
Можете считать, что все ставки верны (нет неверных символов или повторов карт), 
ставки каждого игрока не следуют в определенном порядке, и что при каждой ставке есть безусловный победитель.
<br>Сколько ставок выиграл 1-й игрок?

**Примечание**: карты в текстовом файле обозначены в соответствии с английскими наименованиями достоинств и мастей: T - десятка, J - валет, Q - дама, K - король, A - туз; S - пики, C - трефы, H - червы, D - бубны.
    

``` python
solution  () => 
```

## Частное решение (1)

```python

class Card:
    def __init__(self, card, suit):
        self.card = str(card)
        self.suit = str(suit)

    @property
    def rank(self) -> int:
        """
        Возвращает ранг карты
        (T = 10, J = 11, Q = 12, K = 13, A = 14)
        """
        ranks = '23456789TJQKA'
        return ranks.index(self.card) + 2

    def __gt__(self, other):
        return self.rank > other.rank

    def __repr__(self):
        beauty_suits = {'S': '♠', 'H': '♥', 'C': '♣', 'D': '♦'}
        return f'{self.card}{beauty_suits[self.suit]}'


class Hand:
    def __init__(self, *cards):
        self.cards = cards

    def calc_score(self):
        cards = self.cards
        if self.is_royal_flush(cards):
            return (10, False)

        if self.is_straight_flush(cards):
            return (9, False)

        if self.number_of_a_kind(cards) == 4:
            return (8, True)

        if self.is_full_house(cards):
            return (7, True)

        if self.is_flush(cards):
            return (6, False)

        if self.is_straight(cards):
            return (5, False)

        if self.number_of_a_kind(cards) == 3:
            return (4, True)

        if self.number_of_pairs(cards) == 2:
            return (3, True)

        if self.number_of_pairs(cards) == 1:
            return (2, True)

        return (0, False)

    @staticmethod
    def high_card(cards) -> int:
        """
        Возвращает карту с наибольшим рангом.

        Hand(5♠, 6♦, T♦, J♠, A♥) -> A♥
        """
        return max(cards)

    @staticmethod
    def high_rank_in_pairs(cards) -> int:
        """
        Возвращает наибольший ранг карты из пары.
        # нужно для сравнения пар

        Hand(5♠, 5♦, 7♥, 7♠, J♦) => 7
        """
        ranks = (c.rank for c in cards)
        C = Counter(ranks)
        max_rank = 0

        for rank, count in C.items():
            if count >= 2:
                max_rank = max(rank, max_rank)
        return max_rank

    @staticmethod
    def number_of_pairs(cards) -> int:
        """
        Возвращает количество различных пар.

        Hand(5♠, 5♦, 7♥, 7♠, J♦) => 2 (Две пары)
        """
        ranks = (c.rank for c in cards)
        pairs = 0
        C = Counter(ranks)
        for count in C.values():
            if count == 2:
                pairs += 1
        return pairs

    @staticmethod
    def number_of_a_kind(cards) -> int:
        """
        Возвращает - 3 если есть три карты одного достоинства,
                   - 4 если есть четыре карты одного достоинства
                  [#] None иначе

        Hand(5♠, 5♦, 5♥, 7♠, J♦) => 3 (Тройка)
        Hand(5♠, 5♦, 5♥, 5♠, J♦) => 4 (Каре)
        """
        ranks = (c.rank for c in cards)
        C = Counter(ranks)
        max_count = max(C.values())
        if max_count == 3:
            return 3
        elif max_count == 4:
            return 4

    @staticmethod
    def is_straight(cards, len_straight=5) -> bool:
        """
        Проверка на стрейт (все пять карт по порядку, любые масти)
        [#] Туз может считаться как самой старшей картой в комбинации, так и самой младшей.

        Hand(9♦, T♠, J♥, Q♦, K♠) -> True
        Hand(3♠, 4♦, 5♥, 6♠, A♦) -> True
        """
        ranks = set(c.rank for c in cards)
        if 14 in ranks:
            ranks.add(2)
        ranks = sorted(ranks)
        for i in range(len(ranks) - len_straight + 1):
            if ranks[i + len_straight - 1] - ranks[i] == len_straight - 1:
                return True
        return False

    @staticmethod
    def is_flush(cards) -> bool:
        """
        Проверка на флаш (все пять карт одной масти)

        Hand(T♠, 2♠, J♠, 5♠, A♠) -> True
        Hand(2♠, 5♦, J♥, T♠, Q♦) -> False
        """
        suits = (c.suit for c in cards)
        return len(set(suits)) == 1

    @staticmethod
    def is_full_house(cards) -> bool:
        """
        Проверка на фул-хаус (три карты одного достоинства и одна пара карт.)

        Hand(Q♠, Q♥, Q♦, 5♠, 5♠) -> True
        Hand(2♠, 5♦, J♥, T♠, Q♦) -> False
        """
        if Hand.number_of_a_kind(cards) == 3:
            if Hand.number_of_pairs(cards) == 2:
                return True
        return False

    @staticmethod
    def is_straight_flush(cards) -> bool:
        """
        Проверка на стрейт-флаш (любые пять карт одной масти по порядку.)

        Hand(4♠, 5♠, 6♠, 7♠, 8♠) -> True
        """
        if Hand.is_straight(cards) and Hand.is_flush(cards):
            return True
        return False

    @staticmethod
    def is_royal_flush(cards) -> bool:
        """
        Проверка на роял-флаш (Десятка, валет, дама, король и туз одной масти.)

        Hand(T♠, J♠, Q♠, K♠, A♠) -> True
        """
        ranks = set(c.card for c in cards)
        suits = set(c.suit for c in cards)

        if ranks == set('TJQKA') and len(suits) == 1:
            return True
        return False

    def __gt__(self, other):
        score_h1, flag_h1 = self.calc_score()
        score_h2, flag_h2 = other.calc_score()
        flag = flag_h1 and flag_h2  # флаг для проверки парных карт

        if score_h1 > score_h2:
            return True
        elif score_h1 == score_h2:
            if self.high_rank_in_pairs(self.cards) > self.high_rank_in_pairs(other.cards):
                return True
            # руки с повторяющимися картами
            elif flag:
                if self.high_rank_in_pairs(self.cards) > self.high_rank_in_pairs(other.cards):
                    return True
            # руки без повторов
            else:
                if self.high_card(self.cards) > self.high_card(other.cards):
                    return True
        else:
            return False

    def __repr__(self):
        return f'Hand{self.cards}'


def solution():
    with open('poker.txt', 'r') as f:
        count = 0
        for line in f.readlines():
            row = line.split()
            cards_player_1 = (Card(c[0], c[1]) for c in row[:5])
            cards_player_2 = (Card(c[0], c[1]) for c in row[5:])
            if Hand(*cards_player_1) > Hand(*cards_player_2):
                count += 1
        return count
```
```text
    Время  Замедление    Аргумент      Результат
---------  ------------  ----------  -----------
0.0615953  6.160%                            376 (Ответ)

```
