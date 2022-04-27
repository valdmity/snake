import enum


class MapCell(enum.Enum):
    empty = 0
    wall = 1
    snake_head = 2
    snake_body = 3
    snake_pre_tail = 4
    snake_tail = 5
    food = 6

pairs = [[' ', MapCell.empty], ['*', MapCell.snake_body], ['@', MapCell.snake_head], ['⋄', MapCell.snake_pre_tail],
         ['•', MapCell.snake_tail], ['#', MapCell.wall], ['$', MapCell.food]]
mapcell_by_sym = dict(pairs)
sym_by_mapcell = dict(x[::-1] for x in pairs)