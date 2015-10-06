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
