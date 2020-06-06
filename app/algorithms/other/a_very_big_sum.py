def a_very_big_sum(ar):
    """ Calculate and print the sum of the elements in an array

    Input Format

        The first line of the input consists of an integer n.
        The next line contains n space-separated integers contained in the array.

    Output Format

        Print the integer sum of the elements in the array.
        
    """


    return sum(ar)


if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = a_very_big_sum(ar)
    print(result)