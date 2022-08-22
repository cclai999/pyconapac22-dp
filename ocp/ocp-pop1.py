# open for extension, close for modification, procedural programming
from typing import List


class Circle(object):
    def __init__(self, point, radius):
        self.center = point
        self.radius = radius

class Rectangle(object):
    def __init__(self, point, height, width):
        self.top_left = point
        self.height = height
        self.width = width

def draw_circle(circle):
    print('drawing circle:', circle)

def draw_rectangle(rectangle):
    print('drawing rectangle:', rectangle)


def draw_all_shapes(shapes: List):
    for shape in shapes:
        if isinstance(shape, Circle):
            draw_circle(shape)
        elif isinstance(shape, Rectangle):
            draw_rectangle(shape)
