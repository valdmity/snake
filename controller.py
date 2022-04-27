import time
import keyboard
from objects.vector import *


class Controller:
    def __init__(self, game_engine):
        self.game_engine = game_engine
        print('aboba')

    def run(self):
        while True:
            try:
                if keyboard.is_pressed('w'):
                    self.game_engine.snake.change_dir(vector_down)
                if keyboard.is_pressed('s'):
                    self.game_engine.snake.change_dir(vector_up)
                if keyboard.is_pressed('d'):
                    self.game_engine.snake.change_dir(vector_right)
                if keyboard.is_pressed('a'):
                    self.game_engine.snake.change_dir(vector_left)
                if keyboard.is_pressed('e'):
                    self.game_engine.snake.eat()
                    time.sleep(0.1)
                time.sleep(0.05)
            except():
                pass
