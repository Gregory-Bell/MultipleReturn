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

An example of a multiple return function.
Sometimes you just want the greatest common denominator of the two integers

>>> extended_gcd(45, 99)
9

But sometimes you want more information (like for RSA)

>>> values(extended_gcd(45, 99))
GcdResult(gcd=9, bezout_coefficients=(-2, 1), quotients=(-5, -11))
"""
import collections

from multiplereturn import *


@multiplereturn
def extended_gcd(a, b):
    """Returns the greatest common denominator of its arguments, the Bezout coefficients, and the quotients
    :param a: an integer
    :param b: an integer
    """
    gcd_result = collections.namedtuple('GcdResult', ['gcd', 'bezout_coefficients', 'quotients'])
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a
    while r != 0:
        quotient = old_r // r
        (old_r, r) = (r, old_r - quotient * r)
        (old_s, s) = (s, old_s - quotient * s)
        (old_t, t) = (t, old_t - quotient * t)
    return gcd_result(old_r, (old_s, old_t), (t, -s))
