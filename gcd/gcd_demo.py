from gcd import gcd, euclide, euclide_recursive

tests = [(64,24),(758,306),(96,36)]
for test in tests:
    print(f"the greatest common divisor of {test[0]} and {test[1]} is {gcd(test[0],test[1])}")
    print(f"using the recursive euclidian {euclide_recursive(test[0],test[1])}")
    print(f"using the euclidian {euclide(test[0],test[1])}")