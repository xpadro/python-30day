def binary_gap(num):
    """ Returns the maximum amount of consecutive zeros in the binary representation of 'number'

    In order to count, the amount of zeros have to have a starting 1 and an ending 1:

        Valid: 010001. Result = 3
        Invalid: 01000. Result = 0

    """


    binary = bin(num)[2:]

    max_count = 0

    count = -1
    for element in binary:
        if element == "1":
            if count > max_count:
                max_count = count

            count = 0
        else:
            if count > -1:
                count = count + 1
    
    return max_count
