def is_valid(s: str, t:str) -> bool:
    """ Checks whether the two strings are anagrams or not

    """


    if len(s) != len(t):
        return False

    s = sorted(s)
    t = sorted(t)

    for i, value in enumerate(s):
        if t[i] != value:
            return False
    
    return True
