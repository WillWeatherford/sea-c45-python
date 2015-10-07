#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    def __init__(self, radius):
        '''
        Initialize a Circle object with a given radius parameter.
        '''
        self.radius = radius
        self._diameter = float(radius) * 2
        self._area = float(radius) ** 2 * math.pi

        # for f in ['__add__', '__eq__', '__ge__', '__gt__',
        #           '__le__', '__lt__', '__ne__']:
        #     setattr(self, f,
        #             lambda self, other:
        #                 getattr(self.radius, f)(other.radius))

    def __str__(self):
        return 'Circle with radius: {:.6f}'.format(self.radius)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __mul__(self, n):
        return Circle(self.radius * n)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __radd__(self, other):
        if other == 0:
            return self.radius
        else:
            return self.__add__(other.radius)

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
        self._diameter = value
        self._area = math.pi * (value / 2) ** 2

    @diameter.deleter
    def diameter(self):
        del self._diameter

    @property
    def area(self):
        return self._area

    @area.deleter
    def area(self):
        del self._area
