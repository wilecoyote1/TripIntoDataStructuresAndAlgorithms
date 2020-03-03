def bubblesort(array):
    """
    sort the array using the bubble sort algorithm
    """
    permutation = True
    while permutation:
        permutation = False
        for i in range(len(array)-1):
            if (array[i+1]<array[i]):
                permutation = True
                swap(array,i,i+1)

def swap(array,i,j):
    """
    swap 2 elements in an array
    """
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp
