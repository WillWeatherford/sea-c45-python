'''
Test that the decorators in decorator_solution are working correctly.
'''


from decorator_solution import p_wrapper


@p_wrapper
def wrapped_func(a_string):
    return a_string


def test_p_wrapper():
    assert wrapped_func('') == '<p></p>'
    assert wrapped_func('test') == '<p>test</p>'
