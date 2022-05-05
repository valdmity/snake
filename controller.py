import time
import pygame
from objects.vector import *


class Controller:
    def __init__(self, game_engine):
        self.game_engine = game_engine

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.K_w:
                    self.game_engine.snake.change_dir(vector_down)
                elif event.type == pygame.K_s:
                    self.game_engine.snake.change_dir(vector_up)
                elif event.type == pygame.K_d:
                    self.game_engine.snake.change_dir(vector_right)
                elif event.type == pygame.K_a:
                    self.game_engine.snake.change_dir(vector_left)
                elif event.type == pygame.K_e:
                    self.game_engine.snake.eat()
            time.sleep(0.01)
