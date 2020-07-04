def max_subarray(nums):
    """ Given an integer array, find the contiguous subarray (containing at least one number) which has the 
    largest sum and return its sum.

    Example:

        Input: [-2,1,-3,4,-1,2,1,-5,4],
        Output: 6

        Explanation: [4,-1,2,1] has the largest sum = 6.
    """


    if nums is None or len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]

    curr_sum = nums[0]
    max_sum = nums[0]
            
    for n in range(1, len(nums)):

        if curr_sum + nums[n] > nums[n]:
            curr_sum = curr_sum + nums[n]
        else:
            curr_sum = nums[n]

        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum