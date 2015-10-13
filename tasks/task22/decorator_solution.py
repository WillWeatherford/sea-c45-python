
def p_wrapper(func):
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return '<p>{}</p>'.format(result)
    return wrapped
