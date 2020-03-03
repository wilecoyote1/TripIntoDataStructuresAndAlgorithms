import sys
sys.path.append('../')

from bubblesort import bubblesort
from utils.Fonctions import generateRandomIntArray

array = [6, 10, 5, 4, 7, 10, 9, 7, 8, 8]
bubblesort(array)
print(array)

array = generateRandomIntArray(100,0,100)
print(array)
bubblesort(array)
print(array)


