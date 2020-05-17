'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the 
largest sum and return its sum.

Example:

    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6

    Explanation: [4,-1,2,1] has the largest sum = 6.
'''
def max_subarray(arr):
    max_sum = curr_sum = 0

    for i in range(len(arr)):
        curr_sum = curr_sum + arr[i]

        if curr_sum < 0:
            curr_sum = 0
        else:
            if curr_sum > max_sum:
                max_sum = curr_sum
    
    return max_sum