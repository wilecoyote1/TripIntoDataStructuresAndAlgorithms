import random


def generateRandomIntArray(size=10, min=0, max=10):
    """
    return a random array 
    """
    array = []
    for i in range(size):
        array.append(random.randint(min, max))
    return array


def generateOrderIntArray(size=10, min=0, max=10):
    array = generateRandomIntArray(size, min, max)
    array.sort()
    return array
