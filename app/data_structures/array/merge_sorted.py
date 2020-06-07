def merge_sorted(arr1, arr2):
    """ Given two sorted arrays, merge them in a single sorted array
    
    """

    result = []
    pos_x = 0
    pos_y = 0

    while pos_x < len(arr1) or pos_y < len(arr2):
        if pos_y >= len(arr2) or (pos_x < len(arr1) and arr1[pos_x] < arr2[pos_y]):
            result.append(arr1[pos_x])
            pos_x = pos_x + 1
        else:
            result.append(arr2[pos_y])
            pos_y = pos_y + 1
    
    return result
