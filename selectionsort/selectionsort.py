def selectionsort(array):
    """
    sort the array using the insert sort algorithm
    """
    index_start = 0
    while index_start < len(array):
        index_min = index_start
        for i in range(index_start+1, len(array)):
            if array[i] < array[index_min]:
                index_min = i
        swap(array,index_min, index_start)
        index_start += 1

def swap(array,i,j):
    """
    swap 2 elements in an array
    """
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp
