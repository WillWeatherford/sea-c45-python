def fibonacci(n, m=0, l=1):
    '''
    Returns the nth number from the Fibonacci sequence.

    Example: fibonacci(0) == 0
             fibonacci(1) == 1
    '''
    if n <= 0:
        return m
    else:
        return fibonacci(n - 1, l, m + l)

def lucas(n):
    return 0

def sum_series(n):
    return 0
