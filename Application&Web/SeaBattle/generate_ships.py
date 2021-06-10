from random import shuffle, randint
from settings import BaseFieldSettings


def init_ship(len_ship, grid):
    random_orientation = ['vertical', 'horizontal'][randint(0, 1)]
    if random_orientation == 'vertical':
        start_x, start_y = randint(0, BaseFieldSettings.height_count_cells - len_ship - 1), randint(0, BaseFieldSettings.width_count_cells - 1)
    else:
        start_x, start_y = randint(0, BaseFieldSettings.height_count_cells - 1), randint(0, BaseFieldSettings.width_count_cells - len_ship - 1)

    for i in range(len_ship):
        if random_orientation == 'vertical':
            if grid[start_x + i][start_y] in [1, 'X', 'Y']:
                return init_ship(len_ship, grid)
        else:
            if grid[start_x][start_y + i] in [1, 'X', 'Y']:
                return init_ship(len_ship, grid)

    for i in range(len_ship):
        if random_orientation == 'vertical':
            if i == 0 and start_x != 0:
                grid[start_x - 1][start_y] = 'X'
                if start_y != 0:
                    grid[start_x - 1][start_y - 1] = 'X'
                if start_y != 9:
                    grid[start_x - 1][start_y + 1] = 'X'
            if i == len_ship - 1 and start_x + i != 9:
                grid[start_x + i + 1][start_y] = 'X'
                if start_y != 0:
                    grid[start_x + i + 1][start_y - 1] = 'X'
                if start_y != 9:
                    grid[start_x + i + 1][start_y + 1] = 'X'

            grid[start_x + i][start_y] = 1
            if start_y != 9:
                grid[start_x + i][start_y + 1] = 'X'
            if start_y != 0:
                grid[start_x + i][start_y - 1] = 'X'
        else:
            if i == 0 and start_y != 0:
                grid[start_x][start_y - 1] = 'Y'
                if start_x != 0:
                    grid[start_x - 1][start_y - 1] = 'Y'
                if start_x != 9:
                    grid[start_x + 1][start_y - 1] = 'Y'

            if i == len_ship - 1 and start_y + i != 9:
                grid[start_x][start_y + i + 1] = 'Y'
                if start_x != 0:
                    grid[start_x - 1][start_y + i + 1] = 'Y'
                if start_x != 9:
                    grid[start_x + 1][start_y + i + 1] = 'Y'

            grid[start_x][start_y + i] = 1
            if start_x != 9:
                grid[start_x + 1][start_y + i] = 'Y'
            if start_x != 0:
                grid[start_x - 1][start_y + i] = 'Y'
    return grid, [len_ship, random_orientation, f'{BaseFieldSettings.letters_array[start_x]}{start_y + 1}']


if __name__ == '__main__':
    ships_rules = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
    shuffle(ships_rules)
    test_grid = [[0 for _ in range(10)] for _ in range(10)]

    for ship_size in ships_rules:
        test_grid, ship_data = init_ship(ship_size, test_grid)
        print(ship_data)

    for r in test_grid: print(*r, sep=' ')
