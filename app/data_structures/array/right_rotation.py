def rotate(arr, pos):
    """ Shifts array's elements n units to the right.

    For example, given arr=[1, 2, 3, 4, 5] and n=2, then the result would be:

        [3, 4, 5, 1, 2]
    """


    if len(arr) == 0:
        return arr
        
    for i in range(pos):
        arr.insert(0, arr.pop())
    
    return arr
