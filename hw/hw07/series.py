def fibonacci(n, seq1=0, seq2=1):
    '''
    Returns the nth number from the Fibonacci sequence.

    Example: fibonacci(0) == 0
             fibonacci(1) == 1
    '''
    if n <= 0:
        return seq1
    else:
        return fibonacci(n - 1, seq2, seq1 + seq2)


def lucas(n):
    '''
    Returns the nth number from the Lucas numbers.

    Example: lucas(0) == 2
             lucas(1) == 1
    '''
    return fibonacci(n, 2, 1)


def sum_series(n, m, l):
    return 0
