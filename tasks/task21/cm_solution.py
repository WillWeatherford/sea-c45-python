import sys
import time
# from contextlib import contextmanager


class Timer(object):
    """
    Context manager to give the elapse time to run some code.
    """
    def __init__(self, out=sys.stdout, handle_error=True):
        if not hasattr(out, 'write') or not callable(out.write):
            raise AttributeError('{} object has no write method; not suitable '
                                 'as out parameter for Timer'.format(type(out)))
        self.out = out
        self.handle_error = handle_error
        self.time = None
        self.time_to_run = None

    def __enter__(self):
        if self.time is None:
            self.time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__(%s, %s, %s)' % (exc_type, exc_val, exc_tb))
        if self.time is not None:
            self.time_to_run = time.time() - self.time
            self.write(
                'This code took {} seconds to run.\n'.format(self.time_to_run))
        return self.handle_error

    def write(self, content):
        self.out.write(content)


if __name__ == '__main__':
    with open('out.txt', 'w') as f:
        with Timer(f) as t:
            for i in range(100000):
                i = i ** 20
