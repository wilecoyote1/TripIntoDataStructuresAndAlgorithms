from getdivisors import getdivisors

numbers = [0,2,15,40,45,60,100,200]
for number in numbers:
    print(f"the divisors of {number} are {getdivisors(number)}")