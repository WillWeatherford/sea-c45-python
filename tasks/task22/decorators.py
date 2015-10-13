# -*- coding: utf-8 -*-
import time


class Memoize:
    """
    memoize decorator from avinash.vora
    http://avinashv.net/2008/04/python-decorators-syntactic-sugar/

    logs a result for given args to its function into its "memoized" dict
    attribute, to save time and resources running that function with those args
    in the future.
    """
    def __init__(self, function):  # runs when memoize class is called
        self.function = function
        self.memoized = {}

    def __call__(self, *args):  # runs when memoize instance is called
        try:
            return self.memoized[args]
        except KeyError:
            self.memoized[args] = self.function(*args)
            return self.memoized[args]


def substitute(a_function):
    """return a different function than the one supplied"""
    def new_function(*args, **kwargs):
        return "I'm not that other function"
    return new_function


def logged_func(func):
    def logged(*args, **kwargs):
        print("Function %r called" % func.__name__)
        if args:
            print("\twith args: %r" % (args, ))
        if kwargs:
            print("\twith kwargs: %r" % kwargs)
        result = func(*args, **kwargs)
        print("\tResult --> %r" % result)
        return result
    return logged


def timed_func(func):
    def timed(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print("time expired: %s" % elapsed)
        return result
    return timed


@logged_func
def add(a, b, multiplier=1):
    return (a + b) * multiplier


@logged_func
@timed_func
@Memoize
def sum2x(n):
    return sum(2 * i for i in range(n))


if __name__ == '__main__':
    add(1, 2)
    add(4, 5, multiplier=2)
    sum2x(100)
    sum2x(1000)
    sum2x(10000)
    sum2x(100000)
    sum2x(1000000)
    sum2x(1000000)
    sum2x(10000000)
    sum2x(10000000)
