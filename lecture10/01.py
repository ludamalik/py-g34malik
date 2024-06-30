# -*- coding: utf-8 -*-
import math

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.set_r(r)

    def length(self):
        """Returns the circumference of the circle."""
        return 2 * math.pi * self.r

    def square(self):
        """Returns the area of the circle."""
        return math.pi * self.r ** 2

    def set_r(self, r):
        """Sets the radius of the circle."""
        if r <= 0:
            raise AssertionError("Radius must be a positive number!")
        self.r = r

c = Circle(3, 4, 1)
print(c.length(), c.square())

try:
    c.set_r(-1)
except AssertionError as e:
    print(e)


