def is_happy(n):
    """ Returns True if n is a happy number

    """

        
    if n == 1:
        return True
        
    results = []

    while n != 1:
        total = 0

        for str_n in str(n):
            total = total + int(str_n)**2

        if total == 1:
            return True
        elif total in results:
            return False
        else:
            results.append(total)
            n = total
