import random

def generateRandomIntArray(size=10 ,min=0, max=10):
    """
    return a random array 
    """
    array = []
    for i in range(size):
        array.append(random.randint(min,max))
    return array
