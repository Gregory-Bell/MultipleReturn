"""
    Multiple Return
    Copyright (C) 2014 Gregory S. Bell

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from threading import local

VALUE_ERROR = ValueError("values must be used on the result of a multiple return function")

_local = local()


# noinspection PyPep8Naming
class multiplereturn(object):
    """
    multiplereturn(function) -> function

    Convert a function that returns a tuple into a multiple return function

    A multiple return function returns a tuple, but the caller only recieves
    the first element of the tuple, unless it wraps the function call with
    values(). The expected usage is like this:

    >>> @multiplereturn
    ... def divide(x, y):
    ...     return x // y, x % y
    >>> divide(5, 3)
    1
    >>> values(divide(5, 3))
    (1, 2)
    """

    def __init__(self, f):
        self.__f = f

    def __call__(self, *args, **kwargs):
        result = self.__f.__call__(*args, **kwargs)
        assert isinstance(result, tuple), "A Multiple Return function must return a tuple."

        _local.long_result = result
        return result[0]


def values(multiple_return_function_call):
    """
    :param multiple_return_function_call: a function call like f(x) where f is a function decorated with @multiplereturn
    Usage:

    >>> f = multiplereturn(lambda : (1, 2))
    >>> f()
    1
    >>> values(f())
    (1, 2)
    """
    try:
        result = _local.long_result
    except AttributeError:
        raise VALUE_ERROR

    if multiple_return_function_call != result[0]:
        raise VALUE_ERROR

    del _local.long_result

    return result