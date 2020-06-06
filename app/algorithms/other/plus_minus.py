def plus_minus(arr):
    """ Given an array of integers, calculates the fractions of its elements that are positive, negative, and are zeros

    Output:
        Print the decimal value of each fraction on a new line.

    For example, given the array arr = [1, 1, 0, -1, -1]. there are 5 elements, two positive, two negative and one zero.
    Their ratios would be:
        2/5 = 0.4 
        2/5 = 0.4
        1/5 = 0.2

    """


    totals = [0, 0, 0]

    for el in arr:
        if el > 0:
            totals[0] = totals[0] + 1
        elif el < 0:
            totals[1] = totals[1] + 1
        else:
            totals[2] = totals[2] + 1
    
    return [x / len(arr) for x in totals]


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = plus_minus(arr)
    for x in result:
        print(x)