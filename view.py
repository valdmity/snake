import pygame
from objects.map_cell import MapCell


class View:
    def __init__(self, game_engine):
        self.map_width, self.map_height = game_engine.map_size
        self.scale = 25
        self.font = pygame.font.SysFont('Arial Black', 25)
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
        pygame.display.set_caption("python ^.^")
        pygame.display.set_icon(pygame.image.load("snake.png"))

    def update(self):
        self.surface.fill(pygame.Color("#212121"))
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
        text = "Score: " + str(self.game_engine.snake.points) + "   HP: " + str(self.game_engine.snake.health)
        self.surface.blit(self.font.render(text, True, (199, 199, 199)), (self.scale * 0.2, (self.map_height - 0.25) * self.scale))
        pygame.display.update()

    def set_mode(self, s):
        """
        Создает окно заданного размера
        :param s: размеры окна в клетках
        :return: "холст" окна
        """
        size = [s[0], s[1]+1]
        border_color = [200, 200, 200]
        surface = pygame.display.set_mode([size[0] * self.scale, size[1] * self.scale])
        for i in range(0, size[0]):
            pygame.draw.line(surface, border_color, [i * self.scale, 0], [i * self.scale, size[1] * self.scale])
        for i in range(0, size[1]):
            pygame.draw.line(surface, border_color, [0, i * self.scale], [size[0] * self.scale, i * self.scale])
        return surface

    def draw_point(self, surface, color, pos):
        """
        Закрашивает клеточку
        :param surface: поверхность (окно, например)
        :param color: цвет
        :param pos: координаты клетки
        """
        pygame.draw.rect(surface, color, [pos[1] * self.scale, pos[0] * self.scale, self.scale, self.scale])

    def game_over(self):
        self.surface.fill(pygame.Color("#263238"))
        image = pygame.image.load("game_over.png")
        width_scale = self.map_width * self.scale / 4
        image = pygame.transform.scale(image, (width_scale, 93 * width_scale / image.get_width()))
        self.surface.blit(image, (self.map_width * self.scale * 0.5 - image.get_width() / 2,
                                  self.map_height * self.scale * 0.5 - image.get_height() / 2))

        # self.surface.blit(self.font.render("Game Over", True, (150, 150, 150)),
        #                  (self.map_width * self.scale * 0.45,
        #                   self.map_height * self.scale * 0.5))
        pygame.display.update()
