def rotate(arr, pos):
    if len(arr) == 0:
        return arr
        
    for i in range(pos):
        arr.insert(0, arr.pop())
    
    return arr
