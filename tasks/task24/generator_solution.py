'''
Generator solutions
'''


def intsum():
    '''
    yields a sequence of sums of the count in the sequence
    '''
    n = 0
    y = 0
    while True:
        yield y
        n += 1
        y += n


def intsum2(y=0):
    '''
    alternative way to calculate intsum using sum(range(n + 1))
    '''
    n = 0
    while True:
        yield sum(range(n + 1))
        n += 1


def doubler():
    '''
    yields a sequence where each number is double the previous number
    '''
    y = 1
    while True:
        yield y
        y *= 2


def fib(y=1):
    '''
    yields a sequence where each number is the sum of the previous two
    numbers
    '''
    while True:
        if y <= 1:
            yield y
        else:
            yield fib(y - 1).next() + fib(y - 2).next()
        y += 1


def prime():
    '''
    yields a sequence where every number is divisble only by itself and 1
    '''
    y = 2
    while True:
        for n in range(2, y):
            if y % n == 0:
                break
        else:
            yield y
        y += 1

if __name__ == '__main__':
    g = intsum2()
    g.next()
    g.next()
    g.next()
    g.next()
    g.next()
    g.next()
    g.next()
