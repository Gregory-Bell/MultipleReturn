from threading import local

_local = local()


# noinspection PyPep8Naming
class multiplereturn(object):
    """
    multiplereturn(function) -> function

    Convert a function that returns a tuple into a multiple return function

    A multiple return function returns a tuple, but the caller only recieves
    the first element of the tuple, unless it wraps the function call with
    all_results(). The expected usage is like this:

    >>> @multiplereturn
    ... def divide(x, y):
    ...     return x // y, x % y
    >>> divide(5, 3)
    1
    >>> all_results(divide(5, 3))
    (1, 2)
    """

    def __init__(self, f):
        self.__f = f

    def __call__(self, *args, **kwargs):
        result = self.__f.__call__(*args, **kwargs)
        assert isinstance(result, tuple), "A Multiple Return function must return a tuple."

        _local.long_result = result
        return result[0]


def all_results(multiple_return_function_call):
    """
    Get all results from a multiple return function.
    Usage:

    >>> f = multiplereturn(lambda : (1, 2))
    >>> f()
    1
    >>> all_results(f())
    (1, 2)
    """
    __all_results_usage_error = ValueError("all_results must be used on the result of a multiple return function")

    if not hasattr(_local, "long_result"):
        raise __all_results_usage_error

    result = _local.long_result

    if multiple_return_function_call != result[0]:
        raise __all_results_usage_error

    del _local.long_result

    return result