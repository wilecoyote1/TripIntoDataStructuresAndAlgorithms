import sys
sys.path.append('../')

from factorial import factorial, factorial_recursive

array = [3,4,6]
for v in array:
    print(f" factorial of {v} is {factorial(v)}")
    print(f" factorial recursive of {v} is {factorial_recursive(v)}")