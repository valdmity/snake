# import eventmanager
import threading
import model
import view
import pygame
import controller
from objects.vector import *


if __name__ == '__main__':
    pygame.init()
    game_engine = model.GameEngine()
    graphic = view.View(game_engine)
    controller = controller.Controller(game_engine)

    threading.Thread(target=game_engine.run).start()
    stop_flag = False

    while not stop_flag:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                controller.handle_event(event.key)
            elif event.type == pygame.QUIT:
                game_engine.stop_flag = stop_flag = True
                break
    pygame.time.delay(1000)
    pygame.quit()
