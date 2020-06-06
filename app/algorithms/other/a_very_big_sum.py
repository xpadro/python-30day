""" Calculate and print the sum of the elements in an array

Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.

Input Format

    The first line of the input consists of an integer n.
    The next line contains n space-separated integers contained in the array.

Output Format

    Print the integer sum of the elements in the array.
"""
def aVeryBigSum(ar):
    return sum(ar)


if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)
    print(result)