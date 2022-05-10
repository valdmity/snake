# import eventmanager
import threading
import model
import view
import pygame
from objects.vector import *


if __name__ == '__main__':
    pygame.init()
    game_engine = model.GameEngine()
    graphic = view.View(game_engine)
    t1 = threading.Thread(target=game_engine.run)
    t1.start()
    # threading.Thread(target=contrl.run).start()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.K_w:
                game_engine.snake.change_dir(vector_down)
            elif event.type == pygame.K_s:
                game_engine.snake.change_dir(vector_up)
            elif event.type == pygame.K_d:
                game_engine.snake.change_dir(vector_right)
            elif event.type == pygame.K_a:
                game_engine.snake.change_dir(vector_left)
            elif event.type == pygame.K_e:
                game_engine.snake.eat()
            elif event.type == pygame.QUIT:
                pygame.quit()
