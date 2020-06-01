def find_recursive(number):
    if number == 1:
        return number
        
    return number * find_recursive(number - 1)

def find_iterative(number):
    result = 1
    
    while number > 1:
        result = result * number
        number = number - 1
    
    return result