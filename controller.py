import time
import pygame
from objects.vector import *


class Controller:
    def __init__(self, game_engine):
        self.game_engine = game_engine

    def handle_event(self, key):
        if key == pygame.K_w:
            self.game_engine.snake.change_dir(vector_down)
        elif key == pygame.K_s:
            self.game_engine.snake.change_dir(vector_up)
        elif key == pygame.K_d:
            self.game_engine.snake.change_dir(vector_right)
        elif key == pygame.K_a:
            self.game_engine.snake.change_dir(vector_left)
        elif key == pygame.K_e:
            self.game_engine.snake.eat()
