def find_recursive(number):
    """ Given a number, it calculates its factorial

    Solution is recursive: O(n)

    """
    
    if number == 1:
        return number
        
    return number * find_recursive(number - 1)

def find_iterative(number):
    """ Given a number, it calculates its factorial

    Solution is iterative: O(n)

    """    

    
    result = 1
    
    while number > 1:
        result = result * number
        number = number - 1
    
    return result