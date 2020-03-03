import sys
sys.path.append('../getdivisors')

from getdivisors import getdivisors

def gcd(a,b):
    """
    return the greatest common divisor
    """
    divisors_a = getdivisors(a)
    divisors_b = getdivisors(b)
    max = 1
    for divisor_a in divisors_a:
        if divisor_a in divisors_b and divisor_a>max:
            max = divisor_a
    return max

def euclide(a, b):
    """
    return the greatest common divisor with the euclidian method
    """
    while b != 0:
        rest = a % b
        a = b
        b = rest
    return a

def euclide_recursive(a, b):
    """
    return the greatest common divisor with the euclidian method
    """
#    if b == 1:
#        return 1
    rest = a % b
    if rest == 0:
        return b
    else:
        return euclide_recursive(b,rest)