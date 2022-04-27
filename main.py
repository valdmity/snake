# import eventmanager
import threading
import model
import view
import controller


if __name__ == '__main__':
    game_engine = model.GameEngine()
    contrl = controller.Controller(game_engine)
    graphic = view.View(game_engine)
    t1 = threading.Thread(target=game_engine.run)
    t2 = threading.Thread(target=contrl.run)
    t1.start()
    t2.start()
