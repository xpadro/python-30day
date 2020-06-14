from collections import Counter

def find_intersection(nums1, nums2):
    """ Finds the intersection between two arrays

    """


    result = []
    c1 = Counter(nums1)
    c2 = Counter(nums2)

    for element in (c1&c2).elements():
        result.append(element)

    return result