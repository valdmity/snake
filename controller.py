import datetime
import time
import pygame
from objects.vector import *


class Controller:
    def __init__(self, game_engine):
        self.game_engine = game_engine
        self.dictionary_direction_by_key = {
            pygame.K_w: vector_down, pygame.K_s: vector_up,
            pygame.K_d: vector_right, pygame.K_a: vector_left,
            pygame.K_UP: vector_down, pygame.K_DOWN: vector_up,
            pygame.K_RIGHT: vector_right, pygame.K_LEFT: vector_left}
        self.pressed_keys = set()
        self.last_eat = time.time()

    def handle_key(self):
        for key in self.pressed_keys:
            if key in self.dictionary_direction_by_key:
                self.game_engine.snake.change_dir(self.dictionary_direction_by_key[key])
            elif key == pygame.K_e and time.time() - self.last_eat > 0.1:
                self.last_eat = time.time()
                self.game_engine.spawn_food()

    def handle_keydown(self, key):
        self.pressed_keys.add(key)

    def handle_keyup(self, key):
        self.pressed_keys.remove(key)
