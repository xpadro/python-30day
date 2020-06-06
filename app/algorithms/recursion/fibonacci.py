def find_recursive(number):
    """ Calculates the Fibonacci sequence number of the given position

    Solution is recursive: O(2^n)

    """


    if number == 0:
        return 0
    elif number == 1:
        return 1

    return find_recursive(number - 1) + find_recursive(number - 2)

def find_iterative(number):
    """ Calculates the Fibonacci sequence number of the given position

    Solution is recursive: O(n)

    """


    first = 0
    second = 1

    if number == 0:
        return 0
    elif number == 1:
        return 1

    index = 2
    current = 0
    while index <= number:
        current = first + second
        first = second
        second = current
        index = index + 1


    return current