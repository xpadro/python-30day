from math import floor

def sort(arr):
    if len(arr) == 1:
        return arr
    
    #Split arr into left and right
    middle = floor(len(arr) / 2)
    left = arr[0:middle]
    right = arr[middle:]

    return __merge_sort(sort(left), sort(right))

    

def __merge_sort(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index = left_index + 1
        else:
            result.append(right[right_index])
            right_index = right_index + 1

    return result + left[left_index:] + right[right_index:]
    


arr = [1, 2, 3, 4, 5, 6]
sort(arr)