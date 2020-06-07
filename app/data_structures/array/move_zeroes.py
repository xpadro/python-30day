def move_zeroes(arr):
    ''' Given an array, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

    Example:

        Input: [0,1,0,3,12]
        Output: [1,3,12,0,0]

    Note:

        You must do this in-place without making a copy of the array.
        Minimize the total number of operations.
        
    '''


    first_num = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            temp = arr[first_num]
            arr[first_num] = arr[i]
            arr[i] = temp
            first_num = first_num + 1
    
    return arr



