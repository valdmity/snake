import os


class View:
    def __init__(self, game_engine):
        self.game_engine = game_engine
        self.game_engine.view = self

    def update(self):
        # os.system('cls')
        self.game_engine.draw()
