def find(s):
    """ Returns the index of the first unique char in the string

    """

    found = {}

    for index, value in enumerate(s):
        if value in found:
            found[value] = -1
        else:
            found[value] = index
    
    for index in found.values():
        if index != -1:
            return index
    
    return -1
