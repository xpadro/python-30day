def arrays_reverse(arr):
    '''
    Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.

    Input Format

    The first line contains an integer, N (the size of our array).
    The second line contains N space-separated integers describing array A's elements.
    '''

    result = ""
    for i in reversed(arr):
        result = result + str(i) + " "
    
    print(result.rstrip())


n = int(input())

arr = list(map(int, input().rstrip().split()))

arrays_reverse(arr)
