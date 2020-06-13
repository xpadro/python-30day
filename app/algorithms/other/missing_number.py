def find(nums) -> int:
    """ Given a sequence of distinct numbers from 0 to n, finds the missing one

    [0, 1, 2, 4] returns 3

    """

    total = 0
    for i in range(len(nums) + 1):
        total = total + i
    
    current = sum(nums)

    return total - current