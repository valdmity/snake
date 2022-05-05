import pygame
from objects.map_cell import MapCell


class View:
    def __init__(self, game_engine):
        pygame.init()
        self.size = game_engine.map_size
        self.surface = self.set_mode(self.size)
        self.game_engine = game_engine
        self.game_engine.view = self
        self.dict_colors_by_point_type = {MapCell.snake_tail: pygame.Color("green"),
                                          MapCell.snake_body: pygame.Color("green"),
                                          MapCell.snake_head: pygame.Color("green"),
                                          MapCell.snake_pre_tail: pygame.Color("green"),
                                          MapCell.food: pygame.Color("red"),
                                          MapCell.wall: pygame.Color("gray")}

    def update(self):
        self.fill(pygame.Color("black"))
        game_map = self.game_engine.map
        width, height = self.size
        pygame.display.flip()
        for w in range(width):
            for h in range(height):
                point = game_map[h][w]
                pos = [h, w]
                if point in self.dict_colors_by_point_type:
                    self.draw_point(self.surface,
                                    self.dict_colors_by_point_type[point],
                                    pos)
                else:
                    self.draw_point(self.surface,
                                    pygame.Color("black"),
                                    pos)
        pygame.display.update()

    def set_mode(self, size, scale=10):
        """
        Создает окно заданного размера
        :param size: размеры окна в клетках
        :param scale: размер клеток (10 пикс. по дефолту)
        :return: "холст" окна
        """
        border_color = [200, 200, 200]
        surface = pygame.display.set_mode([size[0] * scale, size[1] * scale])
        for i in range(0, size[0]):
            pygame.draw.line(surface, border_color, [i * scale, 0], [i * scale, size[1] * scale])
        for i in range(0, size[1]):
            pygame.draw.line(surface, border_color, [0, i * scale], [size[0] * scale, i * scale])
        return surface

    def fill(self, screen_color, scale=10):
        """
        Заливает окно цветом
        :param screen_color: цвет окна
        :param scale: размер клеток (10 пикс. по дефолту)
        """
        self.surface.fill(screen_color)
        w, h = self.surface.get_size()
        for i in range(0, w):
            pygame.draw.line(self.surface, [200, 200, 200], [i * scale, 0], [i * scale, h * scale])
        for i in range(0, h):
            pygame.draw.line(self.surface, [200, 200, 200], [0, i * scale], [w * scale, i * scale])

    def draw_point(self, surface, color, pos, scale=10):
        """
        Закрашивает клеточку
        :param surface: поверхность (окно, например)
        :param color: цвет
        :param pos: координаты клетки
        :param scale: размер клеток (10 пикс. по дефолту)
        """
        pygame.draw.rect(surface, color, [pos[0] * scale, pos[1] * scale, scale, scale])
