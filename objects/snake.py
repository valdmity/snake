from objects.map_cell import *
from objects.vector import *


class SnakeSegment:
    def __init__(self, pos, segment, direction, next_segment=None):
        self.dir = direction
        self.pos = pos
        self.segment_type = segment
        self.next_segment = next_segment


class Snake:
    def __init__(self, level, head_pos):
        self.level = level
        self.map = level.map
        self.head = self.tail = None
        self.create_snake(head_pos)
        self.new_head_dir = vector_zero
        self.size = 2

    def create_snake(self, head_pos):
        self.head = SnakeSegment(head_pos, MapCell.snake_head, vector_zero)
        pre_tail = SnakeSegment(head_pos, MapCell.snake_pre_tail, vector_zero, self.head)
        self.tail = SnakeSegment(head_pos, MapCell.snake_tail, vector_zero, pre_tail)

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
        if self.map[pos.y][pos.x] == MapCell.wall:
            self.create_snake(pos)
            return
        ssegment = self.get_segment_by_pos(pos)
        if ssegment is not None and ssegment.segment_type in [MapCell.snake_body, MapCell.snake_pre_tail]:
            self.move_tail(ssegment)

    def move(self):
        self.head.dir = self.new_head_dir
        if self.head.dir == vector_zero:
            return
        nxt_p = self.head.pos + self.head.dir
        if nxt_p.x < 0 or nxt_p.x >= self.level.map_size[0] or nxt_p.y < 0 or nxt_p.y >= self.level.map_size[1]:
            nxt_p = Vector((nxt_p.x + self.level.map_size[0]) % self.level.map_size[0],
                           (nxt_p.y + self.level.map_size[1]) % self.level.map_size[1])

        self.check_mapcell(nxt_p)

        self.move_tail(self.tail.next_segment)
        self.move_head(SnakeSegment(nxt_p, MapCell.snake_head, self.head.dir))

    def eat(self):
        old_tail = self.tail
        self.tail = SnakeSegment(old_tail.pos, MapCell.snake_tail, self.tail.dir, old_tail)
        old_tail.segment_type = MapCell.snake_pre_tail
        self.size += 1

    def get_segment_by_pos(self, pos):
        for s in self.get_segmets():
            if s.pos == pos:
                return s
        return None

    def get_segmets(self):
        segments_pos = []
        cur_segment = self.tail
        while cur_segment is not None:
            segments_pos.append(cur_segment)
            cur_segment = cur_segment.next_segment
        return segments_pos

    def change_dir(self, new_dir):
        if self.head.dir != -new_dir and self.head.dir != new_dir:
            self.new_head_dir = new_dir
