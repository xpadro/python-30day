def reverse_array(arr):
    """ Reverses the content of an array
    
    """

    
    result = []

    for item in reversed(arr):
        result.append(item)

    return ' '.join(map(str, result))

if __name__ == '__main__':
    arr_count = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = reverse_array(arr)
    print(result)