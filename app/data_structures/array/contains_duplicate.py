'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false 
if every element is distinct.
'''
def contains_duplicate(arr):
    visited = {}

    for item in arr:
        if item not in visited:
            visited[item] = True
        else:
            return True
    
    return False
