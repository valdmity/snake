import random

from objects.snake import *
from objects.vector import *
from objects.map_parser import *
import time
import pygame

# noinspection PyTypeChecker
sym_by_direction = dict([[vector_zero, '*'],
                         [vector_left, '←'],
                         [vector_right, '→'],
                         [vector_up, '↓'],
                         [vector_down, '↑']])
level0 = [' ' * 5] * 5
level1 = ['                                   ',
          '                        ####       ',
          '                           #       ',
          '                           #       ',
          '                                   ',
          '                                   ',
          '                       #           ',
          '                      ###          ',
          '                       #           ',
          '               ###                 ',
          '       #       ##                  ',
          '      ####                         ',
          '                                   ']


class GameEngine:
    def __init__(self):
        self.map = parse_map(level1)
        self.map_size = [len(self.map[0]), len(self.map)]
        self.snake = Snake(self, Vector(1, 1))
        self.view = None
        self.stop_flag = False
        self.empty_cells = set()
        for x in range(self.map_size[0]):
            for y in range(self.map_size[1]):
                if self.map[y][x] == MapCell.empty:
                    self.empty_cells.add(Vector(x, y))
        self.spawn_food()
        self.spawn_food()
        self.spawn_food()

    def update(self):
        self.snake.move()

    def update_map(self, updates):
        for upd in updates:
            x, y = upd[0].x, upd[0].y
            self.map[y][x] = upd[1]

    def draw(self, dir_flag=False):
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

    def spawn_food(self):
        self.empty_cells.add(self.snake.head.pos)
        not_available_cells = set()
        for seg in self.snake.get_segmets():
            not_available_cells.add(seg.pos)
        available_cells = self.empty_cells - not_available_cells
        if self.empty_cells:
            spawn_pos = list(available_cells)[random.randrange(0, len(available_cells))]
            self.map[spawn_pos.y][spawn_pos.x] = [MapCell.food,
                                                  MapCell.food,
                                                  MapCell.food,
                                                  MapCell.food,
                                                  MapCell.speed_food,
                                                  MapCell.neg_speed_food][random.randrange(0, 6)]

    def run(self):
        while not self.stop_flag:
            pygame.time.delay(self.snake.move_delays[self.snake.move_delay_index])
            self.update()
            self.view.update()
            # self.draw() # debug
