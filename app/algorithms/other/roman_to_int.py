def to_int(roman):
    """ Converts a roman numeral into an integer

    """


    dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0

    for i, value in enumerate(roman):
        if i < len(roman) - 1:
            if value == "I" and (roman[i+1] == "V" or roman[i+1] == "X"):
                total = total - 1
            elif value == "X" and (roman[i+1] == "L" or roman[i+1] == "C"):
                total = total - 10
            elif value == "C" and (roman[i+1] == "D" or roman[i+1] == "M"):
                total = total - 100
            else:
                total = total + dict[value]
        else:
            total = total + dict[value]
    
    return total

        
