import sys
sys.path.append('../')

from getprimenumbers import getprimenumbers

max = 100
print(f"under {max} this is the prime numbers : {getprimenumbers(max)}")