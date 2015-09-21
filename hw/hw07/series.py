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

if __name__ == '__main__':
    assert(fibonacci(0) == 0)
    assert(fibonacci(1) == 1)
    assert(fibonacci(2) == 1)
    assert(fibonacci(3) == 2)
    assert(fibonacci(4) == 3)
    assert(fibonacci(5) == 5)
    assert(fibonacci(6) == 8)
    assert(fibonacci(7) == 13)
    assert(lucas(0) == 2)
    assert(lucas(1) == 1)
    assert(lucas(2) == 3)
    assert(lucas(3) == 4)
    assert(lucas(4) == 7)
    assert(lucas(5) == 11)
    assert(lucas(6) == 18)
    assert(lucas(7) == 29)
    assert(sum_series(0, 10, 20) == 10)
    assert(sum_series(1, 10, 20) == 20)
    assert(sum_series(2, 10, 20) == 30)
    assert(sum_series(3, 10, 20) == 50)
    assert(sum_series(4, 10, 20) == 80)
    assert(sum_series(5, 10, 20) == 130)
    assert(sum_series(6, 10, 20) == 210)
    assert(sum_series(7, 10, 20) == 340)
