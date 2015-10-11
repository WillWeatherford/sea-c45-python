#!/usr/bin/env python

"""
Simple iterator examples
"""


class IterateMe1(object):
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like xrange(4) )
    """
    def __init__(self, stop=5):
        self.current = -1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


class IterateMe2(object):
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like xrange(4) )
    """
    def __init__(self, start, stop, step=1):
        self.current = start
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.current = int(self.start)
        return self

    def __next__(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


if __name__ == "__main__":

    print("first version")
    for i in IterateMe1():
        print(i)
    print("second version")
    it = IterateMe2(2, 20, 2)
    for i in it:
        if i > 10:
            break
        print(i)
    print('picking iterator back up')
    for i in it:
        print(i)
