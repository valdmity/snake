class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.x * 7369 + self.y

vector_up = Vector(0, 1)
vector_down = Vector(0, -1)
vector_right = Vector(1, 0)
vector_left = Vector(-1, 0)
vector_zero = Vector(0, 0)
