# open for extension, close for modification, object-oriented programming
from abc import ABC, abstractmethod
from typing import List


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, point, radius):
        self.center = point
        self.radius = radius

    def draw(self):
        print('drawing circle:', self)


class Rectangle(Shape):
    def __init__(self, point, height, width):
        self.top_left = point
        self.height = height
        self.width = width

    def draw(self):
        print('drawing rectangle:', self)


class Square(Shape):
    def __init__(self, point, side):
        self.top_left = point
        self.side = side

    def draw(self):
        print('drawing square:', self)


def draw_all_shapes(shapes: List[Shape]):
    for shape in shapes:
        shape.draw()


if __name__ == '__main__':
    draw_all_shapes([Circle((0, 0), 1),
                     Rectangle((1, 1), 1, 1),
                     Square((2, 2), 1)])