def contains_duplicate(arr):
    """ Given an array of integers, find if the array contains any duplicates.

    Returns true if any value appears at least twice in the array, and it should return false 
    if every element is distinct.
    """


    visited = {}

    for item in arr:
        if item not in visited:
            visited[item] = True
        else:
            return True
    
    return False
