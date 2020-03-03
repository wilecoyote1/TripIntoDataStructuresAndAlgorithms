import sys
sys.path.append('../')

from utils.Fonctions import generateOrderIntArray
from binarysearch import binarysearch, recursive

array = generateOrderIntArray(20,0,20)
print(array)
print(binarysearch(array, 7))
print(recursive(array, 7))
