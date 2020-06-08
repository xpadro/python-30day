def find_majority(arr):
    """ Finds the element that appears more than n/2 times

    """


    target = len(arr) / 2
    values = {}

    for element in arr:
        if element in values.keys():
            values[element] = values[element] + 1
            if values[element] >= target:
                return element
        else:
            values[element] = 1
