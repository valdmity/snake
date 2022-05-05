# import eventmanager
import threading
import model
import view
import controller
import pygame


if __name__ == '__main__':
    game_engine = model.GameEngine()
    contrl = controller.Controller(game_engine)
    graphic = view.View(game_engine)
    threading.Thread(target=game_engine.run).start()
    threading.Thread(target=contrl.run).start()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
