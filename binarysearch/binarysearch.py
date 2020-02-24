def binarysearch(array, value):
    """
    search the value in the array, return -1 if not found
    the array is ordered
    """
    idx_min = 0
    idx_max = len(array)
    while idx_min < idx_max:
        mid = int((idx_max - idx_min) / 2) + idx_min
        if value == array[mid]:
            return mid
        if value < array[mid]:
            idx_max = mid
        else:
            idx_min = mid + 1
    return -1


def recursive(array, value):
    return _recursive(array, value, 0, len(array))


def _recursive(array, value, idx_min, idx_max):
    if idx_min >= idx_max:
        return -1
    mid = int((idx_max - idx_min) / 2) + idx_min
    if value == array[mid]:
        return mid
    if value < array[mid]:
        return _recursive(array, value, idx_min, mid)
    else:
        return _recursive(array, value, mid+1, idx_max)