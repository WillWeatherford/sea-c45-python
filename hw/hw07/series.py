def fibonacci(n):
    '''
    Returns the nth number from the Fibonacci sequence.

    Example: fibonacci(0) == 0
             fibonacci(1) == 1
    '''
    return sum_series(n, 0, 1)


def lucas(n):
    '''
    Returns the nth number from the Lucas numbers.

    Example: lucas(0) == 2
             lucas(1) == 1
             lucas(3) == 3
    '''
    return sum_series(n, 2, 1)


def sum_series(n, seq1=0, seq2=1):
    '''
    Returns the nth in a sequence starting with seq1 and seq2.
    '''
    if n <= 0:
        return seq1
    else:
        return sum_series(n - 1, seq2, seq1 + seq2)
