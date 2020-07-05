def is_power_of_three(n):
    """ Returns true if n is a power of three

    """

    power = 0
    result = 0

    while result < n:
        result = 3 ** power

        if result == n:
            return True

        power = power + 1
    
    return False