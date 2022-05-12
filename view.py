import pygame
from objects.map_cell import MapCell


class View:
    def __init__(self, game_engine):
        self.map_width, self.map_height = game_engine.map_size
        self.scale = 25
        self.surface = self.set_mode(game_engine.map_size)
        self.game_engine = game_engine
        self.game_engine.view = self
        self.dict_colors_by_point_type = {MapCell.snake_tail: pygame.Color("#4caf50"),
                                          MapCell.snake_pre_tail: pygame.Color("#43a047"),
                                          MapCell.snake_body: pygame.Color("#388e3c"),
                                          MapCell.snake_head: pygame.Color("#2e7d32"),
                                          MapCell.food: pygame.Color("#e91e63"),
                                          MapCell.wall: pygame.Color("#455a64"),
                                          MapCell.speed_food: pygame.Color("#00bcd4"),
                                          MapCell.neg_speed_food: pygame.Color("#e57373")}
        pygame.display.set_caption("snake ^.^")
        pygame.display.set_icon(pygame.image.load("snake.png"))


    def update(self):
        # pygame.display.flip()
        for w in range(self.map_width):
            for h in range(self.map_height):
                point = self.game_engine.map[h][w]
                pos = [h, w]
                if point in self.dict_colors_by_point_type:
                    self.draw_point(self.surface,
                                    self.dict_colors_by_point_type[point],
                                    pos)
                else:
                    self.draw_point(self.surface,
                                    pygame.Color("#263238"),
                                    pos)
        for seg in self.game_engine.snake.get_segmets():
            pos = [seg.pos.y, seg.pos.x]
            self.draw_point(self.surface,
                            self.dict_colors_by_point_type[seg.segment_type],
                            pos)

        pygame.display.update()

    def set_mode(self, size):
        """
        Создает окно заданного размера
        :param size: размеры окна в клетках
        :param scale: размер клеток (10 пикс. по дефолту)
        :return: "холст" окна
        """
        border_color = [200, 200, 200]
        surface = pygame.display.set_mode([size[0] * self.scale, size[1] * self.scale])
        for i in range(0, size[0]):
            pygame.draw.line(surface, border_color, [i * self.scale, 0], [i * self.scale, size[1] * self.scale])
        for i in range(0, size[1]):
            pygame.draw.line(surface, border_color, [0, i * self.scale], [size[0] * self.scale, i * self.scale])
        return surface

    def fill(self, screen_color):
        """
        Заливает окно цветом
        :param screen_color: цвет окна
        :param scale: размер клеток (10 пикс. по дефолту)
        """
        self.surface.fill(screen_color)
        w, h = self.surface.get_size()
        for i in range(0, w):
            pygame.draw.line(self.surface, [200, 200, 200], [i * self.scale, 0], [i * self.scale, h * self.scale])
        for i in range(0, h):
            pygame.draw.line(self.surface, [200, 200, 200], [0, i * self.scale], [w * self.scale, i * self.scale])

    def draw_point(self, surface, color, pos):
        """
        Закрашивает клеточку
        :param surface: поверхность (окно, например)
        :param color: цвет
        :param pos: координаты клетки
        :param scale: размер клеток (10 пикс. по дефолту)
        """
        pygame.draw.rect(surface, color, [pos[1] * self.scale, pos[0] * self.scale, self.scale, self.scale])

