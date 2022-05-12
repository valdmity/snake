import datetime
import time
import pygame
from objects.vector import *


class Controller:
    def __init__(self, game_engine):
        self.game_engine = game_engine
        self.pressed_keys = set()
        self.last_eat = time.time()

    def handle_key(self):
        for key in self.pressed_keys:
            if key == pygame.K_w:
                self.game_engine.snake.change_dir(vector_down)
            elif key == pygame.K_s:
                self.game_engine.snake.change_dir(vector_up)
            elif key == pygame.K_d:
                self.game_engine.snake.change_dir(vector_right)
            elif key == pygame.K_a:
                self.game_engine.snake.change_dir(vector_left)
            elif key == pygame.K_e and time.time() - self.last_eat > 0.1:
                self.last_eat = time.time()
                self.game_engine.snake.eat()
            elif key == pygame.K_p:
                print("pygame залупа")

    def handle_keydown(self, key):
        self.pressed_keys.add(key)

    def handle_keyup(self, key):
        self.pressed_keys.remove(key)
