def decomposenumber(number):
    """
    return the number decompose
    """
    numbers = []
    rest = number
    while rest != 1:
        for i in range(2, rest+1):
            if rest % i == 0:
                numbers.append(i)
                rest = rest // i
                break
    return numbers