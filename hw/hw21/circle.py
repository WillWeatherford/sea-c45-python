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
        self.diameter = radius * 2
        self.area = math.pi * radius ** 2

    def _get_d(self):
        return self._diameter

    def _set_d(self, value):
        self._diameter = value
        self.radius = value / 2
        self.area = math.pi * (value / 2) ** 2

    def _del_d(self):
        del self._diameter

    diameter = property(_get_d, _set_d, _del_d, doc='docstring')
