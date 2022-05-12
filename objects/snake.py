import model
from objects.map_cell import *
from objects.vector import *


class SnakeSegment:
    def __init__(self, pos, segment, direction, next_segment=None):
        self.dir = direction
        self.pos = pos
        self.segment_type = segment
        self.next_segment = next_segment


class Snake:
    def __init__(self, game_engine, head_pos):
        self.game_engine = game_engine
        self.map = game_engine.map
        self.head = self.tail = None
        self.new_head_dir = vector_zero
        self.health = 3
        self.move_delays = [40, 45, 50, 60, 70, 80, 100, 150, 200, 250, 350]
        self.move_delay_index = 8
        self.is_segments_updated = True
        self.segments = None
        self.create_snake(head_pos)

    def create_snake(self, head_pos):
        self.head = SnakeSegment(head_pos, MapCell.snake_head, vector_zero)
        pre_tail = SnakeSegment(head_pos, MapCell.snake_pre_tail, vector_zero, self.head)
        self.tail = SnakeSegment(head_pos, MapCell.snake_tail, vector_zero, pre_tail)
        self.move_delay_index = 8
        self.is_segments_updated = True
        self.segments = None

    def move_tail(self, new_tail):
        self.tail = new_tail
        self.tail.segment_type = MapCell.snake_tail
        if self.tail.next_segment is not None and self.tail.next_segment.segment_type != MapCell.snake_head:
            self.tail.next_segment.segment_type = MapCell.snake_pre_tail

    def move_head(self, new_head):
        self.head.segment_type = MapCell.snake_body
        self.head.next_segment = new_head
        self.head = new_head

    def check_mapcell(self, pos):
        if self.map[pos.y][pos.x] == MapCell.food:
            self.map[pos.y][pos.x] = MapCell.empty
            self.eat()
            return
        if self.map[pos.y][pos.x] == MapCell.speed_food:
            self.move_delay_index -= 1 if self.move_delay_index > 0 else 0
            self.map[pos.y][pos.x] = MapCell.empty
            self.eat()
        if self.map[pos.y][pos.x] == MapCell.neg_speed_food:
            self.move_delay_index += 1 if self.move_delay_index < len(self.move_delays) - 1 else 0
            self.map[pos.y][pos.x] = MapCell.empty
            self.eat()
        if self.map[pos.y][pos.x] == MapCell.wall:
            self.create_snake(pos)
            self.health -= 1
            return
        ssegment = self.get_segment_by_pos(pos)
        if ssegment is not None and ssegment.segment_type in [MapCell.snake_body, MapCell.snake_pre_tail]:
            self.move_tail(ssegment)

    def move(self):
        self.head.dir = self.new_head_dir
        if self.head.dir == vector_zero:
            return

        nxt_p = self.head.pos + self.head.dir
        if nxt_p.x < 0 or nxt_p.x >= self.game_engine.map_size[0] or nxt_p.y < 0 or nxt_p.y >= self.game_engine.map_size[1]:
            nxt_p = Vector((nxt_p.x + self.game_engine.map_size[0]) % self.game_engine.map_size[0],
                           (nxt_p.y + self.game_engine.map_size[1]) % self.game_engine.map_size[1])

        self.check_mapcell(nxt_p)

        self.move_tail(self.tail.next_segment)
        self.move_head(SnakeSegment(nxt_p, MapCell.snake_head, self.head.dir))
        self.is_segments_updated = True

    def eat(self, grow_food_after_eat=True):
        old_tail = self.tail
        self.tail = SnakeSegment(old_tail.pos, MapCell.snake_tail, self.tail.dir, old_tail)
        old_tail.segment_type = MapCell.snake_pre_tail
        if grow_food_after_eat:
            self.game_engine.spawn_food()

    def get_segment_by_pos(self, pos):
        for s in self.get_segmets():
            if s.pos == pos:
                return s
        return None

    def get_segmets(self):
        if not self.is_segments_updated:
            return self.segments
        segments_pos = []
        cur_segment = self.tail
        while cur_segment is not None:
            segments_pos.append(cur_segment)
            cur_segment = cur_segment.next_segment
        self.is_segments_updated = False
        self.segments = segments_pos
        return segments_pos

    def change_dir(self, new_dir):
        if self.head.dir != -new_dir and self.head.dir != new_dir:
            self.new_head_dir = new_dir
