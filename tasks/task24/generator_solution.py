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

# intsum2
# doubler
# fib
# prime
