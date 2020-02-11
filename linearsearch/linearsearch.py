# linearsearch.py
# lenearsearch in python
# return the index where we found the element
# return -1 if not found
def linearsearch(array, find):
    for i in range(len(array)):
        if array[i] == find:
            return i
    return -1