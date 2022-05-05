from objects.snake import *
from objects.vector import *
from objects.map_parser import *
import time

# noinspection PyTypeChecker
sym_by_direction = dict([[vector_zero, '*'],
                         [vector_left, '←'],
                         [vector_right, '→'],
                         [vector_up, '↓'],
                         [vector_down, '↑']])
level1 = ['                                   ',
          '                              $    ',
          '           $      $      #         ',
          '               $         ##        ',
          '                           ###     ',
          '                    $$$            ',
          '        #           $$$$$$$$$      ',
          '##     ###               #####     ',
          '        #                  #       ',
          '                              #    ']


class GameEngine:
    def __init__(self):
        self.map = parse_map(level1)
        self.map_size = [len(self.map[0]), len(self.map)]
        self.update_map([[Vector(3, 3), MapCell.food]])
        self.snake = Snake(self, Vector(1, 1))
        self.view = None

    def update(self):
        self.snake.move()

    def update_map(self, updates):
        for upd in updates:
            x, y = upd[0].x, upd[0].y
            self.map[y][x] = upd[1]

    def draw(self, dir_flag):
        output = [[' '] * self.map_size[0] for _ in range(self.map_size[1])]
        for y in range(self.map_size[1]):
            for x in range(self.map_size[0]):
                output[y][x] = sym_by_mapcell[self.map[y][x]]
        for s in self.snake.get_segmets():
            if dir_flag:
                output[s.pos.y][s.pos.x] = sym_by_direction[s.dir]
            else:
                output[s.pos.y][s.pos.x] = sym_by_mapcell[s.segment_type]
        fin_output = ""
        for line in output:
            fin_output += ' '.join(line) + "\n"
        print(fin_output)

    def run(self):
        while True:
            self.update()
            time.sleep(0.2)
            self.view.update()
            time.sleep(0.2)
