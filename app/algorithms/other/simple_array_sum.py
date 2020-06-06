def simple_array_sum(ar):
    """ Given an array of integers, find the sum of its elements.

    For example, if the array ar = [1, 2, 3], 1+2+3 = 6, so return 6

    Input Format
        The first line contains an integer, n, denoting the size of the array.
        The second line contains n space-separated integers representing the array's elements.

    Output Format
        Print the sum of the array's elements as a single integer.
        
    """


    return sum(ar)

if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = simple_array_sum(ar)
    print(result)