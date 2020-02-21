def insertionsort(array):
    """
    sort the array using the insert sort algorithm
    """
    index_start = len(array)-1
    while index_start > 0:
        for i in range(index_start):
            while array[index_start] < array[i]:
                swap(array,i,index_start)
        index_start -= 1

def swap(array,i,j):
    """
    swap 2 elements in an array
    """
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp
