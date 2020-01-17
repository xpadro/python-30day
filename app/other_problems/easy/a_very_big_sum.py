""" Calculate and print the sum of the elements in an array

Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.
"""

def aVeryBigSum(ar):
    return sum(ar)


if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)
    print(result)