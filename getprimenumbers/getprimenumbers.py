import sys
sys.path.insert(0, '../isprime/')

from isprime import isprime

def getprimenumbers(max):
    primenumbers = []
    """
    return all the prime numbers under max
    """
    for i in range(3,max):
        if isprime(i):
            primenumbers.append(i)
    return primenumbers
