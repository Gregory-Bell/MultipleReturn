import collections

from multiplereturn import *


@multiplereturn
def extended_gcd(a, b):
    """
    >>> extended_gcd(45, 99)
    9
    >>> values(extended_gcd(45, 99)).bezout_coefficients
    """
    
    GcdResult = collections.namedtuple('GcdResult', ['gcd', 'bezout_coefficients', 'quotients'])
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a
    while r != 0:
        quotient = old_r // r
        (old_r, r) = (r, old_r - quotient * r)
        (old_s, s) = (s, old_s - quotient * s)
        (old_t, t) = (t, old_t - quotient * t)
    return GcdResult(old_r, (old_s, old_t), (t, -s))
