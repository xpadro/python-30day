def first_recurring_char(arr):
    """ Given an array, it should return the first number that gets repeated.
    
    For example:

        [2, 5, 1, 2, 3, 5, 1, 2, 4] = 2
        [2, 1, 1, 2, 3, 5, 1, 2, 4] = 1
        [2, 3, 4, 5] = None
        
    """


    found_nums = {}

    for item in arr:
        if item in found_nums:
            return item
        else:
            found_nums[item] = True
    
    return None