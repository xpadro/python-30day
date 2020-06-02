#O(n^2)
def sort(arr):
    length = len(arr)

    for i in range(length):
        min_element = None
        min_pos = None

        for j in range(i, length):
            if min_element is None or arr[j] < min_element:
                min_element = arr[j]
                min_pos = j
        
        temp = arr[i]
        arr[i] = arr[min_pos]
        arr[min_pos] = temp
    
    return arr
