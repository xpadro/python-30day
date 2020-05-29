def binary_gap(num):
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
