def find_unpaired_element(arr):
    found_occurrences = {}
    
    for el in arr:
        if el in found_occurrences:
            # E.g. We already paired two '1' and we received a third '1'. This one will be unpaired
            if found_occurrences[el] == True:
                found_occurrences[el] = False
            else:
                found_occurrences[el] = True
        else:
            found_occurrences[el] = False
    
    for k, v in found_occurrences.items():
        if not v:
            return k
    
    return None
