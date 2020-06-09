def find_single(arr):
    """ Find the only element that doesn't appear twice in the array

    Restriction: Do not use extra memory

    Solution with extra memory can be found in odd_occurrences.py

    Example: [a, b, c, b, a]

    Bear in mind that:
    
        x XOR 0 = x
        x XOR x = 0

    So we can apply XOR to the array:

        XOR [a, b, c, b, a] = (a XOR a) XOR (b XOR b) XOR c = 0 XOR 0 XOR c = c

    """


    result = 0

    for element in arr:
        result = result ^ element
    
    return result
