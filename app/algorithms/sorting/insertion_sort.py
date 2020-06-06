def sort(arr):
    """ Insertion Sort implementation

    Complexity: O(n^2)
    When list is almost sorted: O(n)
    
    """

    length = len(arr)

    for i in range(length):
        if arr[i] < arr[0]:
            arr.insert(0, arr.pop(i))

        for j in range(1, i):
            if arr[i] > arr[j-1] and arr[i] < arr[j]:
                arr.insert(j, arr.pop(i))

    return arr         


