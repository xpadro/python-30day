#O(2^n)
def find_recursive(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1

    return find_recursive(number - 1) + find_recursive(number - 2)

#O(n)
def find_iterative(number):
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