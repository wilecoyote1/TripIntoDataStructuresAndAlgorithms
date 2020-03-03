import sys
sys.path.append('../')

from insertionsort import insertionsort
from utils.Fonctions import generateRandomIntArray

array = [6, 10, 5, 4, 7, 10, 9, 7, 8, 8]
insertionsort(array)
print(array)

array = generateRandomIntArray(40,0,100)
print(array)
insertionsort(array)
print(array)


