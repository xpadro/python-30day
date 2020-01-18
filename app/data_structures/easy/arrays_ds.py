""" Given an array, A, of N integers, print each element in reverse order as a single line of space-separated integers.

Input Format

    The first line contains an integer, N (the number of integers in A).
    The second line contains N space-separated integers describing A.

Output Format

    Print all N integers in A in reverse order as a single line of space-separated integers.
"""
def reverseArray(a):
    result = []

    for el in reversed(a):
        result.append(el)

    return ' '.join(map(str, result))

if __name__ == '__main__':
    arr_count = int(input())
    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)
    print(res)