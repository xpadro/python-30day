def hammingWeight(n: int) -> int:
    ''' Returns the amount of 1 bits the given number has (Hamming weight)

    '''


    binary = bin(n)[2:]
    count = 0
    
    for element in binary:
        if element == "1":
            count = count + 1
    
    return count