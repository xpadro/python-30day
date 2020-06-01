def find_recursive(number):
    return __do_find_recursive(1, number)

def __do_find_recursive(total, number):
    if number == 1:
        return total

    return __do_find_recursive(total*number, number - 1)
    

def find_iterative(number):
    result = 1
    
    while number > 1:
        result = result * number
        number = number - 1
    
    return result