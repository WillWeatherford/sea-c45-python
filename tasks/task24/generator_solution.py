'''
Generator solutions
'''


def intsum():
    '''
    yields a sequence where each number is the sum of n + 1
    '''
    n = 0
    y = 0
    while True:
        yield y
        n += 1
        y += n


def intsum2():
    pass


def doubler():
    y = 1
    while True:
        yield y
        y *= 2


def fib(y=1):
    while True:
        if y <= 1:
            yield y
        else:
            yield fib(y - 1).next() + fib(y - 2).next()
        y += 1


def prime():
    print 'running prime'
    y = 2
    while True:
        for n in range(2, y):
            if y % n == 0:
                break
        else:
            yield y
        y += 1
