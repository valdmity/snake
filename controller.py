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

    def handle_event(self, key):
        if key in self.dictionary_direction_by_key:
            self.game_engine.snake.change_dir(self.dictionary_direction_by_key[key])
        elif key == pygame.K_e:
            self.game_engine.snake.eat()
